import ipywidgets as widgets
from IPython.display import display, clear_output

# Initialize the question list
questions = []

# Function to add a question
def add_question(question_text, option1, option2, option3, option4, correct_option):
    questions.append({
        "question": question_text,
        "options": [option1, option2, option3, option4],
        "answer": correct_option
    })
    print("Question Added Successfully!")

# Input widgets for adding questions
question_input = widgets.Text(description="Question:")
option1_input = widgets.Text(description="Option 1:")
option2_input = widgets.Text(description="Option 2:")
option3_input = widgets.Text(description="Option 3:")
option4_input = widgets.Text(description="Option 4:")
correct_option_input = widgets.BoundedIntText(value=1, min=1, max=4, description="Correct Opt:")
add_button = widgets.Button(description="Add Question")

# Function to handle button clicks for adding questions
def on_button_clicked(b):
    if question_input.value.strip() and option1_input.value.strip() and option2_input.value.strip() and \
       option3_input.value.strip() and option4_input.value.strip():
        add_question(
            question_input.value,
            option1_input.value,
            option2_input.value,
            option3_input.value,
            option4_input.value,
            correct_option_input.value
        )
        question_input.value = ''
        option1_input.value = ''
        option2_input.value = ''
        option3_input.value = ''
        option4_input.value = ''
        correct_option_input.value = 1
    else:
        print("Please fill in all fields!")

add_button.on_click(on_button_clicked)

# Display widgets for adding questions
display(question_input, option1_input, option2_input, option3_input, option4_input, correct_option_input, add_button)

# Function to run the quiz
def run_quiz():
    score = 0  # Initial score
    clear_output()  # Clear the output for clean quiz display

    # Show questions one by one
    for i, q in enumerate(questions, 1):
        print(f"Q{i}: {q['question']}")
        answer_widget = widgets.RadioButtons(
            options=[f"Option {idx + 1}: {opt}" for idx, opt in enumerate(q["options"])],
            description='Choose:',
            disabled=False
        )
        display(answer_widget)

        submit_button = widgets.Button(description="Submit Answer")

        # Handle submission of answer
        def on_submit_clicked(button, question=q, widget=answer_widget):
            nonlocal score
            if widget.value == f"Option {question['answer']}: {question['options'][question['answer'] - 1]}":
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {question['options'][question['answer'] - 1]}")
            button.disabled = True  # Disable submit button after use

        submit_button.on_click(on_submit_clicked)
        display(submit_button)

    # Show final score after all questions are answered
    def show_score(button):
        print(f"\nYour final score is {score} out of {len(questions)}!")

    finish_button = widgets.Button(description="Finish Quiz")
    finish_button.on_click(show_score)
    display(finish_button)

# Button to start the quiz after adding questions
start_quiz_button = widgets.Button(description="Start Quiz")
start_quiz_button.on_click(lambda b: run_quiz())
display(start_quiz_button)
