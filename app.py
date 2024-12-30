import streamlit as st

# Initialize question list
questions = []

def add_question(question, option1, option2, option3, option4, correct_option):
    questions.append({
        "question": question,
        "options": [option1, option2, option3, option4],
        "answer": correct_option
    })
    st.success("Question Added Successfully!")

# Streamlit UI
st.title("Quiz Application")

# Section to add questions
st.header("Add Questions")
question_text = st.text_input("Enter the question:")
option1 = st.text_input("Option 1:")
option2 = st.text_input("Option 2:")
option3 = st.text_input("Option 3:")
option4 = st.text_input("Option 4:")
correct_option = st.number_input("Correct Option (1-4):", min_value=1, max_value=4, step=1)

if st.button("Add Question"):
    if question_text and option1 and option2 and option3 and option4:
        add_question(question_text, option1, option2, option3, option4, correct_option)
    else:
        st.error("Please fill in all fields!")

# Section to start quiz
if questions:
    st.header("Start Quiz")
    score = 0
    for i, q in enumerate(questions, 1):
        st.write(f"Q{i}: {q['question']}")
        selected_option = st.radio(f"Options for Q{i}:", q["options"], key=f"q{i}")
        if st.button(f"Submit Answer for Q{i}", key=f"submit{i}"):
            if q["options"].index(selected_option) + 1 == q["answer"]:
                st.success("Correct!")
                score += 1
            else:
                st.error(f"Wrong! The correct answer is {q['options'][q['answer'] - 1]}")

    st.write(f"Your final score is {score} out of {len(questions)}.")
