# Create a Quiz which contains 10 Questions.Add multiple type, short answer, true/false, file upload type question in your quiz

import json


# Function to create a quiz
def create_quiz():
    quiz = {"questions": []}

    # Add multiple-choice question
    question1 = {
        "type": "multiple_choice",
        "text": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "correct_answer": "Paris",
    }
    quiz["questions"].append(question1)

    # Add short answer question
    question2 = {
        "type": "short_answer",
        "text": "What is the capital of Japan?",
        "correct_answer": "Tokyo",
    }
    quiz["questions"].append(question2)

    # Add true/false question
    question3 = {
        "type": "true_false",
        "text": "The Earth is flat.",
        "correct_answer": False,
    }
    quiz["questions"].append(question3)

    # Add file upload question
    question4 = {"type": "file_upload", "text": "Upload a picture of a cat."}
    quiz["questions"].append(question4)

    # Add more questions as needed...

    return quiz


# Function to save quiz to a file (JSON format)
def save_quiz_to_file(quiz, file_path):
    with open(file_path, "w") as file:
        json.dump(quiz, file, indent=2)


if __name__ == "__main__":
    # Create the quiz
    my_quiz = create_quiz()

    # Save the quiz to a file
    save_quiz_to_file(my_quiz, "quiz.json")

    print("Quiz created and saved successfully.")
