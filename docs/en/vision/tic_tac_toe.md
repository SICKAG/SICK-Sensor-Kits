# Tic Tac Toe

## Short Description

This challenge project focuses on analyzing a physical Tic Tac Toe board with the Vision Starter Kit.

The goal is to detect player moves on a paper-based game board and use the detected board state to play against a computer opponent or provide suggestions for the next move.

## Project Information

<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr style="background-color: #005aff; color: white;">
      <th style="padding: 8px; text-align: left;">Project type</th>
      <th style="padding: 8px; text-align: left;">Required knowledge level</th>
      <th style="padding: 8px; text-align: left;">Estimated duration</th>
      <th style="padding: 8px; text-align: left;">Additional hardware and software requirements</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td> <span class="project-badge challenge">Challenge Project</span></td>
      <td>Advanced</td>
      <td>4 Hours</td>
      <td>Paper, pen, scissors</td>
    </tr>
  </tbody>
</table>

<br>

![tictactoe](../images/tic_tac_toe.jpg)

## Challenge Goal

The goal of this project is to create a Vision Starter Kit application that can observe a physical Tic Tac Toe board and detect the current game state.

The system should recognize whether fields are empty or occupied and identify the symbols placed by the players.

Unlike a guided project, this challenge does not provide a complete step-by-step solution. Use your knowledge from previous Vision Starter Kit projects to develop your own approach.

---

## Problem Statement

A physical game board or a Tic Tac Toe playing field on a piece of paper should be observed by the Vision Starter Kit.

The system should detect player moves and make it possible to play against a computer opponent or display useful game information.

Possible goals:

- detect empty and occupied fields
- distinguish between different symbols
- evaluate the current board state
- determine valid moves
- suggest the best next move
- create a simple computer opponent

---

## Task

Create an application that analyzes a Tic Tac Toe board and interprets the current game state.

Your solution should include:

1. A physical Tic Tac Toe board or paper-based playing field
2. Image acquisition setup
3. Detection of board fields
4. Recognition of symbols or colors
5. Game state evaluation
6. Optional computer opponent or move suggestion
7. Optional dashboard or visualization

---

## Requirements

<div class="requirement-box">

<h3>Core Requirements</h3>

<ul>
  <li>Use the Vision Starter Kit to observe the game board.</li>
  <li>Detect the individual fields of the Tic Tac Toe board.</li>
  <li>Identify whether a field is empty or occupied.</li>
  <li>Distinguish between the two player symbols.</li>
  <li>Evaluate the current board state.</li>
  <li>Provide useful feedback for the next move or game result.</li>
</ul>

</div>

<div class="requirement-box optional">

<h3>Optional Extensions</h3>

<ul>
  <li>Add a computer opponent with different difficulty levels.</li>
  <li>Add a move suggestion or coaching mode.</li>
  <li>Create a dashboard for visualization.</li>
  <li>Detect invalid moves.</li>
  <li>Add automatic win detection.</li>
  <li>Use a robot arm to draw symbols.</li>
  <li>Use color-based symbol detection instead of shape-based detection.</li>
</ul>

</div>

---

## Suggested Approach

Use the following high-level approach as orientation:

1. Set up the Vision Starter Kit.
2. Prepare a paper-based Tic Tac Toe board.
3. Place the board in the sensor's field of view.
4. Configure image acquisition.
5. Define how the individual board fields should be detected.
6. Decide whether symbols should be detected by shape, color or position.
7. Train or configure the required tools in SICK Nova.
8. Test whether the board state is recognized reliably.
9. Add game logic to evaluate the board.
10. Add feedback, visualization or computer opponent logic.

---

## Possible Detection Strategies

There are different ways to solve this challenge.

<div class="strategy-grid">

  <div class="strategy-card">
    <h3>Symbol Classification</h3>
    <p>Classify the symbols in each field of the Tic Tac Toe board.</p>
    <p>Possible classes could be empty field, circle and cross.</p>
    <p>This approach is useful if the symbols are clearly visible and placed consistently inside the board fields.</p>
  </div>

  <div class="strategy-card">
    <h3>Color Detection</h3>
    <p>Use different colors for the two players and detect the color inside each field.</p>
    <p>Possible classes could be empty field, player 1 color and player 2 color.</p>
    <p>This can simplify the first version of the project, especially if symbol recognition is difficult.</p>
  </div>

  <div class="strategy-card">
    <h3>Fixed Field Analysis</h3>
    <p>Divide the camera image into nine fixed board areas and evaluate each area separately.</p>
    <p>This can be helpful if the board position is stable and does not move during the game.</p>
    <p>It also makes it easier to connect the detected field states with the Tic Tac Toe game logic.</p>
  </div>

</div>

---

## Game Logic Ideas

After detecting the board state, the application can evaluate the game.

Possible logic elements:

- check if a player has three symbols in a row
- check if the game is a draw
- detect invalid moves
- suggest the best possible next move
- implement a simple computer opponent
- add different difficulty levels

Possible feedback:

- current player turn
- valid or invalid move
- winning player
- draw
- suggested next move

---

## Hints

??? tip "Hint 1: Fix the board position"
    Try to keep the Tic Tac Toe board in a fixed position.  
    A stable board position makes field detection much easier.

??? tip "Hint 2: Start with color detection"
    If symbol recognition is difficult, start with colored symbols or colored paper pieces.  
    This can simplify the first version of the project.

??? tip "Hint 3: Use a reduced first version"
    Start by detecting only whether fields are empty or occupied.  
    Add symbol differentiation and game logic afterwards.

??? tip "Hint 4: Separate detection and game logic"
    First make sure the board state is detected reliably.  
    Then add the Tic Tac Toe game logic.

??? tip "Hint 5: Use previous projects as reference"
    If you are unsure how to classify objects or symbols, revisit the [guided classification](./classify_hex_nuts_screws.md) project.


---

## Example Project File

A prepared example project file is available here:

[tictactoe.zip](../files/tictactoe.zip){ .md-button .button-small}

---

## Expected Result

After completing this challenge, the Vision Starter Kit should be able to analyze a physical Tic Tac Toe board and identify the current game state.

A successful result means that:

- the board is detected reliably
- empty and occupied fields are recognized
- player symbols can be distinguished
- the current board state can be evaluated
- a game result or next move can be displayed
- the concept can be extended with a computer opponent or coaching mode

---

## Summary

In this challenge project, you applied vision-based detection to a physical board game.

You practiced how to:

- analyze a structured playing field
- detect symbols or colors
- evaluate a board state
- combine image analysis with game logic
- develop a more interactive application based on the Vision Starter Kit

This project is a good exercise for combining classification, logic and visualization in a playful use case.

---

## Next Steps

Continue with another Vision project or open the complete project files on GitHub.com.

<div class="next-step-buttons" markdown>

[Example Projects](./vision_example_projects.md){ .md-button .button-small }

[GitHub](https://github.com/SICKAG/SICK-Sensor-Starter-Kits){:target="_blank" .md-button .button-small}

</div>