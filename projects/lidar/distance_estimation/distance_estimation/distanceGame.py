import sys
import statistics
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QPushButton, QLabel, QListWidget, 
                             QStackedWidget, QFrame, QGraphicsOpacityEffect)
from PyQt5.QtCore import Qt, QRect, QPropertyAnimation, QEasingCurve, QTimer
from PyQt5.QtGui import QFont, QColor, QPainter, QPen, QBrush
from depth_game import get_computed_distance  # Importe la fonction du premier fichier

# ==========================================================
# GRAPHIQUE DE DÉVIATION (%) - UNIDIRECTIONNEL (TOUT POSITIF)
# ==========================================================
class GraphiqueDirectionnel(QWidget):
    def __init__(self):
        super().__init__()
        self.classement = []
        self.valeur_reelle = 0

    def set_data(self, classement, valeur_reelle):
        self.classement = classement
        self.valeur_reelle = valeur_reelle
        self.update()

    def paintEvent(self, event):
        if not self.classement or self.valeur_reelle <= 0:
            return

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        largeur = self.width()
        hauteur = self.height()
        marge_gauche = 80 
        marge_basse = 100 # Augmenté pour les noms inclinés
        marge_haute = 40
        marge_droite = 40
        
        # Ici, l'axe X (bas) est la ligne de base (0%)
        ligne_base_y = hauteur - marge_basse
        hauteur_utile_graph = hauteur - marge_basse - marge_haute
        largeur_utile = largeur - marge_gauche - marge_droite

        # --- CALCUL DES DÉVIATIONS (%) ---
        data_plot = []
        max_abs_dev_pc = 10 
        for nom, val in self.classement:
            # On prend directement la valeur absolue pour le calcul de l'échelle
            dev_percentage = abs(((val - self.valeur_reelle) / self.valeur_reelle) * 100)
            data_plot.append((nom, dev_percentage))
            if dev_percentage > max_abs_dev_pc:
                max_abs_dev_pc = dev_percentage

        # Arrondir l'échelle vers le haut
        max_echelle = ((int(max_abs_dev_pc) // 10) + 1) * 10

        # --- TITRE DE L'AXE Y ---
        painter.save()
        painter.setPen(QColor("#89b4fa"))
        painter.setFont(QFont("Segoe UI", 10, QFont.Bold))
        painter.translate(25, hauteur // 2)
        painter.rotate(-90)
        painter.drawText(-60, 0, "ERROR % (ABS)")
        painter.restore()

        # --- DESSIN DES AXES ---
        pen_axes = QPen(QColor("#45475a"), 2)
        painter.setPen(pen_axes)
        # Axe Y
        painter.drawLine(marge_gauche, marge_haute, marge_gauche, ligne_base_y)
        # Axe X (Ligne 0% - Réalité)
        painter.setPen(QPen(QColor("#a6e3a1"), 3))
        painter.drawLine(marge_gauche, ligne_base_y, largeur - marge_droite, ligne_base_y)
        
        painter.setPen(QColor("#a6e3a1"))
        painter.setFont(QFont("Segoe UI", 8, QFont.Bold))
        painter.drawText(largeur - 130, ligne_base_y + 20, "REAL MEASURE")

        # Graduations Axe Y (Uniquement vers le haut)
        painter.setFont(QFont("Segoe UI", 8))
        steps = 5 
        for i in range(steps + 1):
            percent = (max_echelle / steps) * i
            y = ligne_base_y - int((percent / max_echelle) * hauteur_utile_graph)
            
            # Lignes de fond horizontales
            painter.setPen(QPen(QColor("#313244"), 1))
            painter.drawLine(marge_gauche, y, largeur - marge_droite, y)
            
            # Graduations
            painter.setPen(QColor("#585b70"))
            painter.drawLine(marge_gauche - 5, y, marge_gauche, y)
            
            painter.setPen(QColor("#bac2de"))
            painter.drawText(marge_gauche - 45, y + 5, f"{int(percent)}%")

        # --- DESSIN DES BARRES (Toutes vers le haut) ---
        nb = len(data_plot)
        pas_x = largeur_utile // (nb + 1) if nb > 0 else largeur_utile

        for i, (nom, dev_pc) in enumerate(data_plot):
            x = marge_gauche + (i + 1) * pas_x
            bar_height = int((dev_pc / max_echelle) * hauteur_utile_graph)
            bar_height = max(bar_height, 4) # Visibilité min
            
            # Rectangle de la barre
            rect = QRect(x - 15, ligne_base_y - bar_height, 30, bar_height)
            
            # Couleur : plus l'erreur est grande, plus on peut changer la teinte si voulu
            # Ici on reste sur le bleu thématique du projet
            painter.setBrush(QBrush(QColor("#89b4fa")))
            painter.setPen(Qt.NoPen)
            painter.drawRoundedRect(rect, 4, 4)

            # Texte du pourcentage (Absolu et Positif)
            painter.setPen(QColor("#89b4fa"))
            painter.setFont(QFont("Segoe UI", 9, QFont.Bold))
            painter.drawText(x - 15, ligne_base_y - bar_height - 10, f"{dev_pc:.1f}%")

            # Nom du joueur
            painter.save()
            painter.setPen(QColor("#cdd6f4"))
            painter.setFont(QFont("Segoe UI", 9))
            painter.translate(x, ligne_base_y + 15)
            painter.rotate(45)
            painter.drawText(0, 10, nom)
            painter.restore()

# =========================
# GESTIONNAIRE PRINCIPAL
# =========================
class GestionnaireJeu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Distance Master Pro")
        self.resize(1200, 850)
        self.showFullScreen()
        
        self.scores_cumules = {} 
        self.estimations = []
        self.valeur_reelle = 0 

        self.setStyleSheet("""
            QWidget { background-color: #1e1e2e; color: #cdd6f4; font-family: 'Segoe UI', Arial; }
            QLineEdit { 
                background-color: #313244; border: 2px solid #45475a; 
                border-radius: 12px; padding: 15px; font-size: 22px; 
            }
            QLineEdit:focus { border: 2px solid #89b4fa; }
            QPushButton { 
                background-color: #89b4fa; color: #1e1e2e; border-radius: 12px; 
                padding: 15px; font-weight: bold; font-size: 18px; 
            }
            QPushButton:hover { background-color: #b4befe; }
            QListWidget { 
                background-color: #313244; border-radius: 15px; padding: 10px; 
                border: none; font-size: 20px; 
            }
            QListWidget::item { 
                background-color: #45475a; margin: 5px; padding: 12px; border-radius: 8px; 
            }
            QLabel#titre { font-size: 42px; font-weight: bold; color: #89b4fa; margin-bottom: 10px; }
            QLabel#label_info { font-size: 18px; font-weight: bold; color: #a6e3a1; letter-spacing: 3px; }
        """)

        self.layout_principal = QVBoxLayout()
        self.stack = QStackedWidget()
        self.stack.addWidget(self.creer_page_saisie())
        self.stack.addWidget(self.creer_page_resultats())
        self.layout_principal.addWidget(self.stack)
        self.setLayout(self.layout_principal)

    def creer_page_saisie(self):
        page = QWidget()
        layout = QVBoxLayout(page); layout.setContentsMargins(60, 40, 60, 40)
        header = QHBoxLayout(); header.addStretch()
        btn_fermer = QPushButton("✕"); btn_fermer.setFixedSize(50, 50)
        btn_fermer.setStyleSheet("background-color: #f38ba8; color: #1e1e2e; font-size: 22px; border-radius: 25px;")
        btn_fermer.clicked.connect(self.close); header.addWidget(btn_fermer); layout.addLayout(header)

        content = QHBoxLayout(); content.setSpacing(80)
        zone_gauche = QVBoxLayout()
        label_titre = QLabel("YOUR GUESS ?"); label_titre.setObjectName("titre")
        
        self.input_nom = QLineEdit(); self.input_nom.setPlaceholderText("Player name...")
        self.input_valeur = QLineEdit(); self.input_valeur.setPlaceholderText("Estimated value (cm)...")
        
        btn_ajouter = QPushButton("ADD YOUR ESTIMATION"); btn_ajouter.clicked.connect(self.ajouter_estimation)
        btn_play = QPushButton("SEE THE RESULTS")
        btn_play.setStyleSheet("background-color: #a6e3a1; font-size: 24px; margin-top: 30px; color: #1e1e2e;")
        btn_play.clicked.connect(self.aller_aux_resultats)
        
        zone_gauche.addStretch(); zone_gauche.addWidget(label_titre); zone_gauche.addWidget(self.input_nom)
        zone_gauche.addWidget(self.input_valeur); zone_gauche.addWidget(btn_ajouter); zone_gauche.addWidget(btn_play); zone_gauche.addStretch()
        
        zone_droite = QVBoxLayout()
        lbl_list = QLabel("LIST OF PLAYERS"); lbl_list.setStyleSheet("font-size: 22px; font-weight: bold; color: #fab387;")
        self.liste_estim = QListWidget()
        self.btn_reset_scores = QPushButton("RESET TOURNAMENT")
        self.btn_reset_scores.setStyleSheet("background-color: #f38ba8; color: #1e1e2e; margin-top: 10px; font-size: 14px; padding: 10px;")
        self.btn_reset_scores.clicked.connect(self.confirmer_reset_scores)
        
        zone_droite.addWidget(lbl_list); zone_droite.addWidget(self.liste_estim); zone_droite.addWidget(self.btn_reset_scores)
        content.addLayout(zone_gauche, 3); content.addLayout(zone_droite, 2); layout.addLayout(content)
        return page

    def creer_page_resultats(self):
        page = QWidget()
        layout = QVBoxLayout(page); layout.setContentsMargins(30, 20, 30, 30)
        header = QHBoxLayout()
        btn_retour = QPushButton("NEXT ROUND"); btn_retour.setFixedWidth(150)
        btn_retour.setStyleSheet("background-color: #fab387; color: #1e1e2e;")
        btn_retour.clicked.connect(self.reinitialiser_jeu)
        header.addWidget(btn_retour); header.addStretch()
        btn_fermer = QPushButton("✕"); btn_fermer.setFixedSize(40, 40)
        btn_fermer.setStyleSheet("background-color: #f38ba8; border-radius: 20px;")
        btn_fermer.clicked.connect(self.close); header.addWidget(btn_fermer); layout.addLayout(header)
        
        content = QHBoxLayout(); content.setSpacing(30)
        zone_gauche = QVBoxLayout()
        lbl_real_hint = QLabel("REAL MEASURE"); lbl_real_hint.setObjectName("label_info"); lbl_real_hint.setAlignment(Qt.AlignCenter)
        zone_gauche.addWidget(lbl_real_hint)
        self.label_mesure = QLabel("0.0"); self.label_mesure.setFixedSize(260, 260)
        self.label_mesure.setAlignment(Qt.AlignCenter)
        self.label_mesure.setStyleSheet("background-color: #1e1e2e; border: 10px solid #a6e3a1; border-radius: 130px; font-size: 90px; font-weight: bold; color: #a6e3a1;")
        zone_gauche.addWidget(self.label_mesure, alignment=Qt.AlignCenter)
        
        self.graphique = GraphiqueDirectionnel(); self.graphique.setMinimumHeight(420)
        self.graphique.setStyleSheet("background-color: #313244; border-radius: 20px;")
        zone_gauche.addWidget(self.graphique)
        
        layout_stats = QHBoxLayout(); layout_stats.setSpacing(25)
        style_card = "QFrame { background-color: #313244; border-radius: 20px; border: 2px solid #45475a; }"
        style_val = "font-size: 52px; font-weight: bold; color: #a6e3a1; background: transparent; border: none;"
        style_lbl = "font-size: 16px; color: #89b4fa; font-weight: bold; background: transparent; border: none; letter-spacing: 2px;"
        
        self.card_acc = QFrame(); self.card_acc.setStyleSheet(style_card)
        vbox1 = QVBoxLayout(self.card_acc); self.val_acc = QLabel("0%"); self.val_acc.setStyleSheet(style_val)
        self.val_acc.setAlignment(Qt.AlignCenter); self.lbl_acc_title = QLabel("GROUP ACCURACY")
        self.lbl_acc_title.setStyleSheet(style_lbl); self.lbl_acc_title.setAlignment(Qt.AlignCenter)
        vbox1.addWidget(self.val_acc); vbox1.addWidget(self.lbl_acc_title)
        
        self.card_const = QFrame(); self.card_const.setStyleSheet(style_card)
        vbox2 = QVBoxLayout(self.card_const); self.val_const = QLabel("0%")
        self.val_const.setStyleSheet(style_val.replace("#a6e3a1", "#fab387")); self.val_const.setAlignment(Qt.AlignCenter)
        lbl_const = QLabel("GROUP CONSISTENCY"); lbl_const.setStyleSheet(style_lbl); lbl_const.setAlignment(Qt.AlignCenter)
        vbox2.addWidget(self.val_const); vbox2.addWidget(lbl_const)
        
        layout_stats.addWidget(self.card_acc); layout_stats.addWidget(self.card_const); zone_gauche.addLayout(layout_stats)
        
        zone_droite = QVBoxLayout()
        lbl_standings = QLabel("ROUND STANDINGS"); lbl_standings.setObjectName("titre"); lbl_standings.setStyleSheet("font-size: 28px;")
        self.liste_classement = QListWidget(); zone_droite.addWidget(lbl_standings); zone_droite.addWidget(self.liste_classement)
        content.addLayout(zone_gauche, 2); content.addLayout(zone_droite, 1); layout.addLayout(content)
        return page

    def ajouter_estimation(self):
        nom = self.input_nom.text().strip()
        valeur = self.input_valeur.text().strip()
        if nom and valeur:
            try:
                val = float(valeur)
                self.estimations.append((nom, val))
                if nom not in self.scores_cumules: self.scores_cumules[nom] = 0
                self.liste_estim.addItem(f"👤 {nom} (Total: {self.scores_cumules[nom]} pts)  ➔  {valeur} cm")
                self.input_nom.clear(); self.input_valeur.clear(); self.input_nom.setFocus()
            except ValueError: pass

    def aller_aux_resultats(self):
        if not self.estimations: return
        mesure_mm = get_computed_distance()
        if mesure_mm is None: return
        
        self.valeur_reelle = mesure_mm / 10 
        self.label_mesure.setText(f"{self.valeur_reelle:.1f}")
        
        classement = sorted(self.estimations, key=lambda x: abs(x[1] - self.valeur_reelle))
        self.liste_classement.clear(); ecarts = []; all_accuracies = []
        
        for i, (nom, val) in enumerate(classement):
            ecart = abs(val - self.valeur_reelle); ecarts.append(ecart)
            accuracy = max(0, min(100, 100 - (ecart / self.valeur_reelle * 100 if self.valeur_reelle > 0 else 0)))
            all_accuracies.append(accuracy)
            
            pts = 5 if i == 0 else 3 if i == 1 else 1 if i == 2 else 0
            self.scores_cumules[nom] += pts
            medaille = "🏆 " if i == 0 else "🥈 " if i == 1 else "🥉 " if i == 2 else "▫️ "
            self.liste_classement.addItem(f"{medaille} {nom} | {val} cm (+{pts} pts)\n🎯 Accuracy: {accuracy:.1f}% | Total: {self.scores_cumules[nom]} pts")
            
        avg_acc = sum(all_accuracies) / len(all_accuracies)
        std_dev = statistics.stdev(ecarts) if len(ecarts) > 1 else 0.0
        # On exprime la constance en % par rapport à la valeur réelle pour rester cohérent
        const_pc = (std_dev / self.valeur_reelle * 100) if self.valeur_reelle > 0 else 0
        
        self.val_acc.setText(f"{avg_acc:.1f}%"); self.val_const.setText(f"{const_pc:.1f}%")
        self.graphique.set_data(classement, self.valeur_reelle); self.animer_transition(1)

    def confirmer_reset_scores(self):
        if self.btn_reset_scores.text() == "RESET TOURNAMENT":
            self.btn_reset_scores.setText("ARE YOU SURE?")
            QTimer.singleShot(3000, lambda: self.btn_reset_scores.setText("RESET TOURNAMENT"))
        else:
            self.scores_cumules = {}; self.estimations = []; self.liste_estim.clear()
            self.btn_reset_scores.setText("RESET TOURNAMENT")

    def animer_transition(self, index):
        self.eff = QGraphicsOpacityEffect(self.stack); self.stack.setGraphicsEffect(self.eff)
        self.anim = QPropertyAnimation(self.eff, b"opacity")
        self.anim.setDuration(400); self.anim.setStartValue(0); self.anim.setEndValue(1); self.anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.stack.setCurrentIndex(index); self.anim.start()

    def reinitialiser_jeu(self):
        self.estimations = []; self.liste_estim.clear(); self.liste_classement.clear()
        self.animer_transition(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = GestionnaireJeu(); fenetre.show(); sys.exit(app.exec_())