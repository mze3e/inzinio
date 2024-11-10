import streamlit as st

# Step 1: Welcome and Introduction
st.title("Personalized Learning Assistant")
st.write("Welcome! This app will help you learn a topic by recommending learning techniques suited to your style.")

# Step 2: Input Topic
topic = st.text_input("What topic would you like to learn?")

# Step 3: Learning Style Questionnaire
st.write("Tell us a bit about your learning style:")
learning_style = st.selectbox("Preferred Learning Style", ("Visual", "Auditory", "Kinesthetic"))
goal = st.selectbox("Learning Goal", ("Quick Review", "Mastery", "Exam Preparation"))
time_commitment = st.slider("How much time can you commit per day? (minutes)", 10, 120, 30)

# Step 4: Recommend Techniques Based on Learning Style
if st.button("Get Learning Recommendations"):
    st.write(f"### Recommended Techniques for Learning **{topic}**")
    
    if learning_style == "Visual":
        st.write("- **Mind Maps**: Organize ideas visually to better understand relationships.")
        st.write("- **Memory Palace (Loci Method)**: Visualize information in familiar locations for stronger recall.")
        st.write("- **Flashcards**: Use the Leitner system to review key facts and concepts.")
    
    elif learning_style == "Auditory":
        st.write("- **Mnemonics**: Create memorable auditory cues for complex information.")
        st.write("- **Active Recall with Explanation**: Record yourself explaining concepts aloud.")
        st.write("- **SQ3R Method**: Survey, question, and read material, then recite and review verbally.")

    elif learning_style == "Kinesthetic":
        st.write("- **Practice Exams**: Simulate hands-on practice by taking quizzes or mock exams.")
        st.write("- **Feynman Technique**: Teach back the topic in your own words as if explaining it to someone else.")
        st.write("- **Interleaved Practice**: Switch between different subtopics to reinforce learning.")

    st.write("Each technique is tailored to your style and can improve retention and understanding. Try incorporating these into your study routine!")

# Step 5: Additional Options and Tracking (Placeholder)
st.write("### Coming Soon!")
st.write("In future versions, we'll add features like spaced repetition, progress tracking, and more!")

