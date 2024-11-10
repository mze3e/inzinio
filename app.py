import streamlit as st
import datetime

# Step 1: Welcome and Introduction
st.title("Personalized Learning Assistant")
st.write("Welcome! This app will help you learn a topic by recommending learning techniques suited to your style.")

# Step 2: Input Topic
topic = st.text_input("What topic would you like to learn?")

# Step 3: Interactive Learning Style Quiz
st.write("### Determine Your Learning Style")
learning_style_known = st.radio("Do you already know your learning style?", ("Yes", "No"))

if learning_style_known == "No":
    st.write("Answer a few questions to help us determine your learning style.")
    
    # Learning Style Quiz
    score_visual, score_auditory, score_kinesthetic = 0, 0, 0
    q1 = st.selectbox("When learning something new, do you prefer:", 
                      ["Seeing diagrams, charts, or written instructions", 
                       "Listening to explanations or discussions", 
                       "Engaging in hands-on activities or simulations"])
    if q1 == "Seeing diagrams, charts, or written instructions":
        score_visual += 1
    elif q1 == "Listening to explanations or discussions":
        score_auditory += 1
    else:
        score_kinesthetic += 1
    
    q2 = st.selectbox("If given a list to remember, would you:", 
                      ["Write it down or visualize it", 
                       "Repeat it aloud", 
                       "Use physical items or gestures to remember"])
    if q2 == "Write it down or visualize it":
        score_visual += 1
    elif q2 == "Repeat it aloud":
        score_auditory += 1
    else:
        score_kinesthetic += 1

    q3 = st.selectbox("When studying alone, do you prefer:", 
                      ["Using visuals like diagrams and notes", 
                       "Reading aloud or listening to recordings", 
                       "Hands-on practice or simulations"])
    if q3 == "Using visuals like diagrams and notes":
        score_visual += 1
    elif q3 == "Reading aloud or listening to recordings":
        score_auditory += 1
    else:
        score_kinesthetic += 1

    # Determine learning style
    if max(score_visual, score_auditory, score_kinesthetic) == score_visual:
        learning_style = "Visual"
    elif max(score_visual, score_auditory, score_kinesthetic) == score_auditory:
        learning_style = "Auditory"
    else:
        learning_style = "Kinesthetic"
else:
    learning_style = st.selectbox("Select your preferred learning style:", ["Visual", "Auditory", "Kinesthetic"])

# Step 4: Goal and Time Commitment
st.write("### Set Your Learning Goals")
goal = st.selectbox("Learning Goal", ("Quick Review", "Mastery", "Exam Preparation"))
time_commitment = st.slider("How much time can you commit per day? (minutes)", 10, 120, 30)

# Step 5: Display Recommended Techniques with Interactive Descriptions
if st.button("Get Learning Recommendations"):
    st.write(f"### Recommended Techniques for Learning **{topic}**")

    # Techniques based on learning style
    if learning_style == "Visual":
        st.write("#### Techniques for Visual Learners")
        if st.checkbox("Mind Maps"):
            st.write("Organize ideas visually to understand connections between concepts. Mind mapping helps structure concepts for better recall.")
        
        if st.checkbox("Memory Palace (Loci Method)"):
            st.write("Visualize information in familiar locations. The method helps in creating strong visual memory anchors.")
        
        if st.checkbox("Flashcards with Leitner System"):
            st.write("Use visually appealing flashcards and the Leitner system to optimize spaced repetition.")
        
        if st.checkbox("Color-Coding and Highlighting"):
            st.write("Use colors to organize and emphasize important information.")

    elif learning_style == "Auditory":
        st.write("#### Techniques for Auditory Learners")
        
        if st.checkbox("Mnemonics with Rhythm or Rhyme"):
            st.write("Create auditory cues to help with recall. Rhymes and rhythms help build strong memory associations.")
        
        if st.checkbox("Group Discussions"):
            st.write("Discuss topics with peers. Speaking out concepts helps reinforce understanding.")

    elif learning_style == "Kinesthetic":
        st.write("#### Techniques for Kinesthetic Learners")
        
        if st.checkbox("Practice Exams and Quizzes"):
            st.write("Take quizzes to reinforce knowledge through practice.")
        
        if st.checkbox("Hands-On Practice"):
            st.write("Engage in practical activities related to the topic for stronger memory retention.")
        
    # General Techniques for All Learners
    st.write("#### General Techniques for All Learners")
    if st.checkbox("Spaced Repetition"):
        st.write("Revisit material at intervals to improve long-term retention.")
    
    # Suggested Learning Plan Based on Time Commitment
    st.write("### Suggested Daily Learning Plan")
    if time_commitment <= 30:
        st.write(f"5-10 minutes on spaced repetition, then 10-20 minutes using {learning_style} techniques.")
    elif 30 < time_commitment <= 60:
        st.write(f"15-20 minutes on spaced repetition, 15-20 minutes on practice exams, and remaining time on {learning_style} techniques.")
    else:
        st.write(f"30 minutes on spaced repetition, 20 minutes on practice exams, and remaining time on {learning_style} techniques.")

# Step 6: Interactive Timer for Pomodoro Technique
st.write("### Focus Timer (Pomodoro Technique)")
pomodoro_timer = st.slider("Set Pomodoro timer (minutes)", 15, 60, 25)
if st.button("Start Timer"):
    st.write(f"Focus for {pomodoro_timer} minutes, then take a short break!")

# Step 7: Progress Tracker and Visualizations Placeholder
st.write("### Progress Tracking and Weekly Summary (Coming Soon!)")
st.write("In future updates, you'll be able to track time spent on each technique, set reminders, and see charts of your progress.")

# Step 8: Weekly Summary and Insights
if st.checkbox("Show Sample Weekly Summary"):
    st.write("**Progress this week:**")
    st.write("- **Spaced Repetition Sessions:** 5")
    st.write("- **Practice Exams Completed:** 3")
    st.write("- **Techniques Used:** Mind Maps, Flashcards, Group Discussions")
    st.write("**Tip:** Great job! Try increasing your practice exam sessions next week for even better retention.")

# Step 9: Gamified Milestones and Rewards
st.write("### Milestones and Rewards")
st.write("Earn rewards for reaching milestones in your learning journey!")
if st.checkbox("Track My First Milestone"):
    st.write("Congratulations! You've completed your first learning session! 🎉")

# Step 10: Learning Journal
st.write("### Learning Journal (Coming Soon!)")
st.write("Reflect on your learning journey, jot down insights, and track notes for each session.")