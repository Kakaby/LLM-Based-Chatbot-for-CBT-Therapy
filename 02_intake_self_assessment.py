import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI

load_dotenv()

# -------------------------------------------------------------------
# NOTE: This prompt contains the self-assessment logic and instructions.
#       GPT is expected to guide the user through the 5 questions,
#       compute a total score, and then continue the conversation.
# -------------------------------------------------------------------
st.title("Therapy Intake Self-Assessment")
# Warm intro message
st.markdown("""
👋 **Welcome to your self-check-in space**

This chatbot is here to support you using CBT tools and evidence-based screening.  
We'll go through a short **intake self-assessment** using the PHQ-9 (for depression) and GAD-7 (for anxiety).

Type **"I'm ready"** when you feel comfortable to begin 💬
""")

# Define questions and answer options
phq9 = [
    "Little interest or pleasure in doing things?",
    "Feeling down, depressed, or hopeless?",
    "Trouble falling or staying asleep, or sleeping too much?",
    "Feeling tired or having little energy?",
    "Poor appetite or overeating?",
    "Feeling bad about yourself — or that you are a failure or have let yourself or your family down?",
    "Trouble concentrating on things, such as reading or watching TV?",
    "Moving or speaking so slowly that other people could have noticed? Or the opposite — being so fidgety or restless?",
    "Thoughts that you would be better off dead, or of hurting yourself in some way?",
]

gad7 = [
    "Feeling nervous, anxious, or on edge?",
    "Not being able to stop or control worrying?",
    "Worrying too much about different things?",
    "Trouble relaxing?",
    "Being so restless that it's hard to sit still?",
    "Becoming easily annoyed or irritable?",
    "Feeling afraid as if something awful might happen?",
]

response_scale = ["Not at all", "Several days", "More than half the days", "Nearly every day"]
response_values = {"Not at all": 0, "Several days": 1, "More than half the days": 2, "Nearly every day": 3}

# Store session state
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.phase = "waiting"  # can be "waiting", "phq", "gad", "done"
    st.session_state.responses = []

# Chat history UI
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Say something to begin...")

# Handle chatbot flow
if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    assistant_response = ""

    # Start assessment
    if st.session_state.phase == "waiting" and "ready" in user_input.lower():
        st.session_state.phase = "phq"
        st.session_state.step = 0
        assistant_response = f"Great 🌿 Let's begin with the PHQ-9. Over the last 2 weeks, how often have you been bothered by the following:\n\n**{phq9[0]}**\nOptions: {', '.join(response_scale)}"

    elif st.session_state.phase == "phq":
        if user_input in response_scale:
            st.session_state.responses.append(response_values[user_input])
            st.session_state.step += 1
            if st.session_state.step < len(phq9):
                assistant_response = f"**{phq9[st.session_state.step]}**\nOptions: {', '.join(response_scale)}"
            else:
                st.session_state.phase = "gad"
                st.session_state.step = 0
                assistant_response = f"Thanks for sharing that 💛\n\nNow let's do the GAD-7. Again, in the last 2 weeks, how often have you been bothered by:\n\n**{gad7[0]}**\nOptions: {', '.join(response_scale)}"
        else:
            assistant_response = f"Please choose from: {', '.join(response_scale)}"

    elif st.session_state.phase == "gad":
        if user_input in response_scale:
            st.session_state.responses.append(response_values[user_input])
            st.session_state.step += 1
            if st.session_state.step < len(gad7):
                assistant_response = f"**{gad7[st.session_state.step]}**\nOptions: {', '.join(response_scale)}"
            else:
                st.session_state.phase = "done"
                assistant_response = "Thanks for completing the check-in. Let me review your responses... 🧾"
        else:
            assistant_response = f"Please choose from: {', '.join(response_scale)}"

    elif st.session_state.phase == "done":
        phq_total = sum(st.session_state.responses[:9])
        gad_total = sum(st.session_state.responses[9:])
        assistant_response += f"\n\n**PHQ-9 Score:** {phq_total}/27"
        if phq_total <= 4:
            assistant_response += "\n✅ Minimal depression symptoms."
        elif phq_total <= 9:
            assistant_response += "\nℹ️ Mild symptoms. Consider monitoring or reflecting further."
        elif phq_total <= 14:
            assistant_response += "\n⚠️ Moderate symptoms. Therapy may be helpful."
        elif phq_total <= 19:
            assistant_response += "\n🚨 Moderately severe. Please consider professional support."
        else:
            assistant_response += "\n❗ Severe depression symptoms. Seeking support is strongly recommended."

        assistant_response += f"\n\n**GAD-7 Score:** {gad_total}/21"
        if gad_total <= 4:
            assistant_response += "\n✅ Minimal anxiety symptoms."
        elif gad_total <= 9:
            assistant_response += "\nℹ️ Mild anxiety. Keep an eye on your stress levels."
        elif gad_total <= 14:
            assistant_response += "\n⚠️ Moderate anxiety. Talking with a professional might help."
        else:
            assistant_response += "\n❗ Severe anxiety symptoms. Support is strongly recommended."

        if st.session_state.responses[8] > 0:
            assistant_response += "\n\n🚨 You indicated experiencing distressing thoughts. If you're feeling unsafe, please reach out to a mental health professional or call a crisis line immediately. You're not alone 💛"

        assistant_response += "\n\n🧘 Thank you for reflecting with me today. I'm here if you'd like to talk more."

    # Display assistant message
    if assistant_response:
        st.chat_message("assistant").markdown(assistant_response)
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
