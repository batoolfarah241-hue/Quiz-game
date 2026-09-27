# Python Quiz Game

A command-line multiple-choice quiz game. Questions are shuffled each round,
your score is tracked, and any missed questions are listed at the end.

## Features
- Randomized question order each time you play
- Choose how many questions you want to answer
- Score tracking
- Review of missed questions at the end
- Option to play again

## Concepts practiced
- Lists of dictionaries for structured data
- The `random` module (shuffling)
- Loops, conditionals, and functions
- Simple scoring logic

## How to run
```bash
python quiz_game.py
```

## Example
```
Welcome to the Python Quiz Game!
How many questions? (1-6): 3

Question 1/3
What does 'print()' do in Python?
  A. Deletes a variable
  B. Displays output
  C. Starts a loop
  D. Imports a module
Your answer (A/B/C/D): B
Correct!
```

## Ideas to extend it
- Load questions from a JSON or CSV file instead of hardcoding them
- Add a timer per question
- Save high scores to a file
