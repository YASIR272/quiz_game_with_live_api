import requests
import html
import random

# Get questions from API
def get_question():
    url = "https://opentdb.com/api.php?amount=5&category=18&difficulty=easy&type=multiple"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['results']
    else: 
        print(f"Failed to fetch data, status code: {response.status_code}")
        return []

# Present question to the user
def present_question(question, index):
    print(f"\nQuestion {index + 1}: {html.unescape(question['question'])}")
    choices = question['incorrect_answers'] + [question['correct_answer']]
    random.shuffle(choices)
    
    for i, choice in enumerate(choices):
        print(f"{i + 1}. {html.unescape(choice)}")
    
    return choices.index(question['correct_answer']) + 1

# Main function
def main():
    print("Welcome to the Quiz!\n")
    questions = get_question()
    if not questions:
        print("No questions available. Exiting.")
        return
    
    score = 0
    total_questions = len(questions)

    for i, question in enumerate(questions):
        correct_choice_number = present_question(question, i)
        user_answer = input("Your answer (enter number): ")
        try:
            user_answer = int(user_answer)
            if not (1 <= user_answer <= 4):
                print("Invalid input. Please enter a number between 1 and 4.\n")
                continue
            if user_answer == correct_choice_number:
                print("Correct!\n")
                score += 1
            else:
                print(f"Incorrect. Correct answer was option {correct_choice_number}.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")
    
    print(f"Quiz completed! Your score is: {score} / {total_questions}")
    if ((score/total_questions)*100) > 50:
        print("Great work You've passed the test")
    else: 
        print("You've failed the test, please study hard")
# To run the quiz
main()
