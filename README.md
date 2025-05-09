# 🧠 AI-Powered Therapy Support Chatbot

This is a Proof of Concept (PoC) for an AI-powered chatbot designed to support patients in-between therapy sessions. Inspired by Cognitive Behavioral Therapy (CBT) techniques, the system offers a conversational interface for self-assessment, journaling, and mood tracking — all powered by large language models.

> ⚠️ This is a prototype for demonstration and research purposes only. It is **not intended for clinical use** or to replace licensed mental health care.

---

## 🚀 Features

### ✅ Use Case 1: CBT Therapy Simulation  
- Chatbot guides users through reflective prompts  
- Identifies cognitive distortions (e.g., catastrophizing, mind reading)  
- Responds with supportive, non-judgmental feedback
- Click on here to check out the **interactive dashboard demo** [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://01simpletherapistpy-ge5dpxndetvtwf5iazhr4n.streamlit.app/).

### ✅ Use Case 2: Intake Assessment  
- Walks users through PHQ-9 and GAD-7  
- Scores and interprets mental health indicators  
- Gently responds based on results, including soft risk alerts
- Click here to check out the **interactive dashboard demo** [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://02intakeselfassessmentpy-4ymcdbzvuzghxhhaskfpxk.streamlit.app/)

### ✅ Use Case 3: Journaling and Mood Reflection  
- Offers a guided, CBT-inspired journaling experience  
- Promotes self-reflection, pattern recognition, and emotional awareness
- Click on here to check out the **interactive dashboard demo** [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]

---

## 🧰 Tech Stack

| Component               | Description                                        |
|-------------------------|----------------------------------------------------|
| 🧠 LLM Backbone          | [OpenAI GPT-4o](https://openai.com/research/gpt-4o-system-card) (adaptable to Claude, Llama, etc.) |
| 💬 Frontend Framework    | [Streamlit](https://streamlit.io) – for chatbot UI |
| 🔐 Config Management     | `.env` file for API key and environment settings   |
| 📦 Dependency Handling   | `requirements.txt` for pip install                 |

---

## 🧱 Application Structure

```bash
.
├── 01_simple_therapist.py      # CBT-style chatbot simulation
├── 02_self_assessment.py       # PHQ-9 and GAD-7 conversational assessment
├── 03_journaling.py            # Guided journaling chatbot module
├── requirements.txt            # Required Python packages
└── .env                        # Environment variables (not in the repo)
