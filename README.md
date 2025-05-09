# AI-Powered Mental Health Therapy Support Chatbot

This is a Proof of Concept (PoC) for an AI-powered chatbot designed to support patients in-between therapy sessions. Inspired by Cognitive Behavioral Therapy (CBT) techniques, the system offers a conversational interface for self-assessment, journaling, and mood tracking — all powered by large language models.

> ⚠️ This is a prototype for demonstration and research purposes only. It is **not intended for clinical use**.

# Team Members
This practicum project for **Columbia University’s QMSS GR5053 course** was developed by **Arete Song, Boyan Sun, Chenchen Li, Dyuthi Dinesh, Jimin Oh, Ruixuan Zhao, and Yuge Yan**.  

Guided by **Professor Benjamin Kinsella**.

---
## Documentations
Click here to check out the [**Technical Requirements Document**](Documents/Technical_Requirements_Document.pdf/) and [**Presentation**](Documents/LLM_Therapy_Companion.pdf/).

---
## Features

### ✅ Use Case 1: CBT Therapy Simulation  
- Guided conversations mirroring CBT techniques
- Reflection prompts + identification of cognitive distortions
- Responds with supportive, non-judgmental feedback
- Click on here to check out the **interactive dashboard demo** [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://01simpletherapistpy-ge5dpxndetvtwf5iazhr4n.streamlit.app/).

### ✅ Use Case 2: Intake Assessment  
- Walks users through PHQ-9 and GAD-7  
- Scores and interprets mental health indicators  
- Gently responds based on results, including soft risk alerts
- Click here to check out the **interactive dashboard demo** [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://02intakeselfassessmentpy-4ymcdbzvuzghxhhaskfpxk.streamlit.app/)

### ✅ Use Case 3: Journaling and Mood Reflection  
- Offers a guided, CBT-inspired daily journaling experience  
- Promotes self-reflection, mood tracking, pattern recognition, and emotional awareness
- Click on here to check out the **interactive dashboard demo** [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://03journaling.streamlit.app/)

---

## Tech Stack

| Component               | Description                                        |
|-------------------------|----------------------------------------------------|
| LLM Backbone          | [OpenAI GPT-4o](https://openai.com/research/gpt-4o-system-card) (adaptable to Claude, Llama, etc.) |
| Frontend Framework    | [Streamlit](https://streamlit.io) – for chatbot UI |
| Config Management     | `.env` file for API key and environment settings   |
| Dependency Handling   | `requirements.txt` for pip install                 |

---

## Application Structure

```bash
.
├── 01_simple_therapist.py      # CBT-style chatbot simulation
├── 02_self_assessment.py       # PHQ-9 and GAD-7 conversational assessment
├── 03_journaling.py            # Guided journaling chatbot module
├── requirements.txt            # Required Python packages
└── .env                        # Environment variables (not in the repo)
```

## Intent of the PoC
- Prototype AI-assisted between-session support for patients
- Scaffold therapy-like interactions through natural language
- Explore feasibility of structured conversations in behavioral health
- Demonstrate integration into clinical workflows (supporting therapists)

## Limitations
⚠️ This PoC is an early-stage prototype designed to explore feasibility, not a production-ready system.
- No User Authentication or Identity Management
- No Persistent Data Storage
- Lack of Role-Based Access Control
- No Treatment Plan Management or Progress Tracking

## Proposed System Architecture
To move from a PoC to a clinically viable product, more features and architectural considerations would be required, click here to check out the [**Proposed System Architecture**](Proposed_System_Architecture/) .

