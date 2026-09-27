"""
Multiple-Choice Quiz Game
A simple command-line quiz that asks random questions, tracks the score,
and shows a summary with the wrong answers at the end.

Concepts covered:
- Lists of dictionaries (structured data)
- The random module
- Loops and conditionals
- Functions and basic scoring logic
"""

import random

QUESTIONS = [
    {
        "question": "What does 'print()' do in Python?",
        "options": ["A. Deletes a variable", "B. Displays output", "C. Starts a loop", "D. Imports a module"],
        "answer": "B",
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C",
    },
    {
        "question": "What data type is the result of 5 / 2 in Python 3?",
        "options": ["A. int", "B. float", "C. str", "D. bool"],
        "answer": "B",
    },
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["A. func", "B. def", "C. function", "D. lambda"],
        "answer": "B",
    },
    {
        "question": "What does len([1, 2, 3]) return?",
        "options": ["A. 2", "B. 3", "C. 4", "D. Error"],
        "answer": "B",
    },
    {
        "question": "Which of these creates an empty dictionary?",
        "options": ["A. {}", "B. []", "C. ()", "D. \"\""],
        "answer": "A",
    },
]


def ask_question(q):
    print(q["question"])
    for option in q["options"]:
        print(" ", option)

    answer = input("Your answer (A/B/C/D): ").strip().upper()
    return answer == q["answer"]


def run_quiz(num_questions=5):
    questions = QUESTIONS.copy()
    random.shuffle(questions)
    questions = questions[:num_questions]

    score = 0
    missed = []

    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}/{len(questions)}")
        correct = ask_question(q)
        if correct:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer was {q['answer']}.")
            missed.append(q["question"])

    print("\n==== Quiz Complete ====")
    print(f"Score: {score}/{len(questions)}")

    if missed:
        print("\nQuestions you missed:")
        for m in missed:
            print(" -", m)
    else:
        print("Perfect score! Well done.")


def main():
    print("Welcome to the Python Quiz Game!")
    while True:
        try:
            n = int(input(f"How many questions? (1-{len(QUESTIONS)}): "))
            n = max(1, min(n, len(QUESTIONS)))
            break
        except ValueError:
            print("Please enter a valid number.")

    run_quiz(n)

    again = input("\nPlay again? (y/n): ").strip().lower()
    if again == "y":
        main()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
