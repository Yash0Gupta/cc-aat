import streamlit as st

# Initialize the question list
questions = []

# Function to add a question
def add_question(question_text, option1, option2, option3, option4, correct_option):
    questions.append({
        "question": question_text,
        "options": [option1, option2, option3, option4],
        "answer": correct_option
    })

# Streamlit input fields for adding multiple questions
st.title("Quiz Application")

# Display current questions
if questions:
    st.write("### Current Questions:")
    for i, q in enumerate(questions, 1):
        st.write(f"**Q{i}:** {q['question']}")

# Adding multiple questions functionality
question_input = st.text_input("Question:")
option1_input = st.text_input("Option 1:")
option2_input = st.text_input("Option 2:")
option3_input = st.text_input("Option 3:")
option4_input = st.text_input("Option 4:")
correct_option_input = st.number_input("Correct Option (1-4)", min_value=1, max_value=4, value=1)

# Button to add the question
if st.button("Add Question"):
    if question_input.strip() and option1_input.strip() and option2_input.strip() and \
       option3_input.strip() and option4_input.strip():
        add_question(
            question_input,
            option1_input,
            option2_input,
            option3_input,
            option4_input,
            correct_option_input
        )
        # Clear the inputs after adding
        question_input = ''
        option1_input = ''
        option2_input = ''
        option3_input = ''
        option4_input = ''
        correct_option_input = 1
    else:
        st.warning("Please fill in all fields!")

# Once at least one question is added, allow to start the quiz
if len(questions) > 0:
    if st.button("Start Quiz"):
        score = 0  # Initial score

        # Loop through each question and display it
        for i, q in enumerate(questions, 1):
            st.write(f"**Q{i}:** {q['question']}")
            
            # Radio buttons to select an option
            answer = st.radio(
                "Choose an option:",
                [f"Option 1: {q['options'][0]}", f"Option 2: {q['options'][1]}",
                 f"Option 3: {q['options'][2]}", f"Option 4: {q['options'][3]}"],
                key=f"q{i}"  # Unique key for each question
            )
            
            # Check the answer
            if answer == f"Option {q['answer']}: {q['options'][q['answer'] - 1]}":
                st.success("Correct!")
                score += 1
            else:
                st.error(f"Wrong! The correct answer was: {q['options'][q['answer'] - 1]}")

        # Show final score after all questions are answered
        st.write(f"Your final score is {score} out of {len(questions)}!")
