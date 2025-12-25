import random
import json
import time
import os

def load_questions():
    if not os.path.exists("questions.json"):
        print("Error: 'questions.json' not found.")                                                                                                                    
        return []  # Make sure this line is indented under the if
    try:
        with open("questions.json", "r") as f:
            data = json.load(f)
        return data.get("questions", [])
    except json.JSONDecodeError:
        print("Error: 'questions.json' is not a valid JSON file.")
        return []

def get_random_questions(questions, num_questions):
    if num_questions > len(questions):
        num_questions = len(questions)
    return random.sample(questions, num_questions)

def ask_question(question):
    print("\n" + question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i + 1}. {option}")

    while True:
        try:
            number = int(input("Select the correct number: "))
            if 1 <= number <= len(question["options"]):
                break
            else:
                print("Choice out of range. Try again.")
        except ValueError:
            print("Invalid input. Enter a number.")

    correct = question["options"][number - 1] == question["answer"]
    if correct:
        print("Correct!")
    else:
        print("Wrong! Correct answer:", question["answer"])
    return correct

questions = load_questions()
if not questions:
    exit()

while True:
    try:
        total_questions = int(input(f"Enter the number of questions (1-{len(questions)}): "))
        if 1 <= total_questions <= len(questions):
            break
        else:
            print("Number out of range.")
    except ValueError:
        print("Invalid input. Enter a number.")

random_questions = get_random_questions(questions, total_questions)
correct = 0
start_time = time.time()

for question in random_questions:
    if ask_question(question):
        correct += 1
    print("-----------------")

completed_time = time.time() - start_time
print("\nSummary")
print("Total Questions:", total_questions)
print("Correct Answers:", correct)
score_percent = round((correct / total_questions) * 100, 2)
print("Score:", f"{score_percent}%")
print("Time:", round(completed_time, 2), "seconds")
