
document.addEventListener("DOMContentLoaded", updatePage);

const signs = ["Schere", "Stein", "Papier"]
let user_sign = ""
let computer_sign = ""
let user_score = 0
let computer_score = 0
let number = 0;
let exit = false;



async function runGame() {   
    
    document.getElementById('rungame').style.visibility = `hidden`; 
        while (user_score < 3 && computer_score < 3 && exit!=true) {  
            number = 0

            /* countdown */
            for (let i = 0; i < 3; i++) {
                document.getElementById('user_sign_img').innerHTML = ``
                document.getElementById('computer_sign_img').innerHTML = ``
                await new Promise(resolve => setTimeout(resolve, 1000));
                let countdown = signs[i]
                document.getElementById('result').innerText = ` ${countdown}...`;
                if (countdown === "Schere") {
                    document.getElementById('number').innerHTML = `<img src="../static/img/Schere.svg" alt="Schere" class="responsive"></img>`;
                }
                else if (countdown === "Stein") {
                document.getElementById('number').innerHTML = `<img src="../static/img/Stein.svg" alt="Stein" class="responsive"></img>`;
                }
                else {
                    document.getElementById('number').innerHTML = `<img src="../static/img/Papier.svg" alt="Papier" class="responsive"></img>`;
                    }
                }

            await new Promise(resolve => setTimeout(resolve, 2000)); 
            await getCurrentSign();

            /* 5 Sekunden Aufschub, falls kein Zeichen erkannt wird: */
            let startTime = Date.now();
            let actualTime = startTime;
            number = 3
            while ((actualTime-startTime<5000) && user_sign === "kein Zeichen") {
                document.getElementById('result').innerText = ``;
                actualTime = Date.now();
                document.getElementById('number').innerText = `Halte deine Hand im angegebenen Bereich unter den Sensor!`;
                document.getElementById('user_sign').innerText = `Warte auf dein Zeichen...`;
                await getCurrentSign();
                }
            /* Zum zweiten Mal 3 Sekunden Aufschub, am Ende Spielabbruch */
            for (let i = 3; i >= 0; i--) {
                if (user_sign !== "kein Zeichen" || (actualTime - startTime >= 10000)) {
                    break;
                }
                document.getElementById('number').style.fontSize = "5rem"
                document.getElementById('number').innerText = `${i}`;
                let screen = document.getElementById('play_screen');
                screen.style.backgroundColor = "#e36a00";
                await new Promise(resolve => setTimeout(resolve, 1000));
                actualTime = Date.now();
                await getCurrentSign();
                }

            if (user_sign === "Keine Verbindung") {
                await new Promise(resolve => setTimeout(resolve, 1000)); 
                exit = true;
                document.getElementById('replay').style.visibility = 'visible';
                document.getElementById('number').innerText = "Keine Verbindung möglich."
            }

            else if(user_sign!="kein Zeichen") {
            document.getElementById('result').innerText = ``;
            document.getElementById('number').innerText = " ";
            let screen = document.getElementById('play_screen')
            screen.style.backgroundColor = "#007cc1"
            getComputerSign();
            await new Promise(resolve => setTimeout(resolve, 1000)); 
            await getScore(user_score, computer_score);
            await new Promise(resolve => setTimeout(resolve, 3000)); 
            await updateScore(user_score, computer_score);

                if (user_score === 3) {
                    document.getElementById('number').innerText = `Du hast gegen den Computer gewonnen! 
                    Das Spiel ist zu Ende.`;
                    document.getElementById('result').innerHTML = `<img src="../static/img/Stern.svg" alt="Ergebnis" class="responsive-small"></img>`;
                    document.getElementById('replay').style.visibility = 'visible';
                }
                else if (computer_score === 3) {
                    document.getElementById('number').innerText = `Leider hast du gegen den Computer verloren...  
                    Das Spiel ist zu Ende.`;
                    document.getElementById('result').innerHTML = `<img src="../static/img/Smiley.svg" alt="Ergebnis" class="responsive"></img>`;
                    document.getElementById('replay').style.visibility = 'visible';
                }
            }
            else
            {   
                await new Promise(resolve => setTimeout(resolve, 1000)); 
                exit = true;
                document.getElementById('replay').style.visibility = 'visible';
                document.getElementById('number').style.fontSize = "1.75rem"

                document.getElementById('number').innerText = "Leider hast du die Zeit verpasst."
                document.getElementById('user_sign').innerText = ``;
            }
        } 
}

async function updatePage() {

    document.getElementById('user_sign_img').innerHTML = `<img src="../static/img/SpielstartLinks.svg" alt="Hand Spieler" class="responsive"></img>`;
    document.getElementById('computer_sign_img').innerHTML = `<img src="../static/img/SpielstartRechts.svg" alt="Hand Spieler" class="responsive"></img>`;
    document.getElementById('number').innerText = `Halte die Hand am Ende des Countdowns unter den Sensor. Klicke auf den Button, um zu starten. `;
    document.getElementById('replay').style.visibility = 'hidden';
    document.getElementById('user_score').innerHTML = ``;
    document.getElementById('computer_score').innerHTML = ``;
    document.getElementById('result').innerText = ``;
}

async function updateScore(user_score, computer_score) {

    if (computer_score === 1) {
        document.getElementById('computer_score').innerHTML = `<img src="../static/img/1Punkt.svg" alt="1 Punkt" class="responsive"></img>`;
    }
    else if (computer_score === 2) {
        document.getElementById('computer_score').innerHTML = `<img src="../static/img/2Punkte.svg" alt="1 Punkt" class="responsive"></img>`
    }
    else if (computer_score === 3) {
        document.getElementById('computer_score').innerHTML = `<img src="../static/img/3Punkte.svg" alt="1 Punkt" class="responsive"></img>`
    }
    else {
        document.getElementById('computer_score').innerHTML = ``
    }
    if (user_score === 1) {
        document.getElementById('user_score').innerHTML = `<img src="../static/img/1Punkt.svg" alt="1 Punkt" class="responsive"></img>`;
    }
    else if (user_score=== 2) {
        document.getElementById('user_score').innerHTML = `<img src="../static/img/2Punkte.svg" alt="1 Punkt" class="responsive"></img>`
    }
    else if (user_score === 3) {
        document.getElementById('user_score').innerHTML = `<img src="../static/img/3Punkte.svg" alt="1 Punkt" class="responsive"></img>`
    }
    else {
        document.getElementById('user_score').innerHTML = ``
    }
    document.getElementById('user_sign_img').innerHTML = ``
    document.getElementById('computer_sign_img').innerHTML = ``
    document.getElementById('computer_sign').innerText = ``;
    document.getElementById('user_sign').innerText = ``;
    document.getElementById('result').innerText = ``;
    document.getElementById('number').innerText = ``
    document.getElementById('replay').style.visibility = 'hidden';
}

async function getComputerSign() {

    const randomNumber = Math.floor(Math.random()*(signs.length))

    computer_sign = signs[randomNumber]
    document.getElementById('computer_sign').innerText = `Der Computer zeigt ${computer_sign}.`;
    let img = document.getElementById('computer_sign_img')
    setImg(computer_sign, img)

    return computer_sign;
}

async function getCurrentSign() {
    try {
        const response = await fetch('/getCurrentSign');
        const data = await response.json();
        user_sign = data.sign;
        if ((user_sign != "kein Zeichen") && (user_sign != "Keine Verbindung")) 
            {
            document.getElementById('user_sign').innerText = `Du zeigst ${user_sign}.`;
            let img = document.getElementById('user_sign_img');
            setImg(user_sign, img);
            return user_sign;
            }
            
    } catch (error) {
        console.error('Error getting current symbol:', error);
        return user_sign;
        
    }

};

async function setImg(sign, img) {

    if (sign === "Schere") {
        img.innerHTML = `<img src="../static/img/Schere.svg" alt="Schere" class="responsive"></img>`
    }
    else if (sign === "Stein") {
        img.innerHTML = `<img src="../static/img/Stein.svg" alt="Stein" class="responsive"></img>`
    }
    else {
        img.innerHTML = `<img src="../static/img/Papier.svg" alt="Papier" class="responsive"></img>`
    }
}

async function getScore() {

    if (user_sign === computer_sign) {
        document.getElementById('number').innerText = `Unentschieden!`
    }
    else if (
        ((user_sign === "Schere") && (computer_sign === "Papier")) 
        || ((user_sign === "Stein") && (computer_sign === "Schere"))
        || ((user_sign === "Papier") && (computer_sign === "Stein"))
            ) 
        {
        document.getElementById('number').innerText = `Gewonnen!`
        user_score += 1
    }
    else {
        document.getElementById('number').innerText = `Verloren!`

        computer_score += 1
    }

    return { user_score, computer_score };
    
}