# Ptero Glide // Applications of Finite Automata
<div align = "center">
  <img src = "images/ui/ptero-glide.gif" alt = "Demo"/>
</div>
<br> Ptero Glide is a simple endless runner game where players control a pterodactyl gliding through a vibrant landscape. The objective is to dodge various obstacles, all while maintaining momentum and speed.
<br>
<div align = "center">
  <br>▰▰▰▰▰▰▰▰▰▰▰▰ this project is for  CS313 class Applications of Finite Automata ▰▰▰▰▰▰▰▰▰▰▰▰
</div>

## Table of Contents
1. [Project Description](#project-description)
2. [FSM Design](#fsm-design)
3. [Installation Guide](#installation-guide)
4. [Gameplay](#gameplay)
5. [Credits](#credits)

## Project Description
Ptero Glide is a simple endless runner game where players control a pterodactyl gliding through a vibrant landscape. Like the Chrome Dino game, which this game is inspired on. The objective is to achieve the highest score possible while navigating through various obstacles, all while maintaining momentum and speed. As the player progresses, the game introduces dynamic elements, including background changes based on score milestones (e.g., after reaching 300 and 600 points) that enhance the visual experience. Once the player reaches or adds up to a hundred points the speed of the game is multiplied, making it challenging and even more exciting. This project was built using Python's Pygame library.

## FSM Design
The FSM represents the game's states, showing how the game transitions between the menu, running, jumping, game over, and background changes as the player progresses. The DFA ensures the game is deterministic, with each state reacting to specific inputs. For example, the player can only transition from running to jumping with a jump input and can only restart the game after reaching the game over state.

<div align = "center">
  <br>╔══════════════════╗
  <br> <b> DFA VISUALIZATION </b>
  <br>╚══════════════════╝
  <br> <img src = "images/dfa_graph.png" alt = "DFA"/> 
  
</div>



<div align = "center">
  <br>╔══════════════════╗
  <br> <b> TRANSITION TABLE </b>
  <br>╚══════════════════╝
</div>
