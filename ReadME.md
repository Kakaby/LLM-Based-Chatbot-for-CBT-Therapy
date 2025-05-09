                                           ┌──────────────────────────┐
                                           │     Patient Interface    │  ← Streamlit-based Chatbot UI
                                           └────────────┬─────────────┘
                                                        │
                                             Conversational Flow (LLM)
                                                        │
                                       ┌────────────────▼─────────────────┐
                                       │         CBT Chatbot (LLM API)    │  ← OpenAI GPT-4o / Claude / Llama
                                       └────────────┬─────────────┬───────┘
                                                    │             │
                                            ┌───────▼──────┐ ┌────▼────────┐ 
    # How the chatbot "remember" previous   │ Memory Handler││Emotion      │  ← Natural Language Processing
      interactions                          │ (Contextual   ││Detection/   │  # Emotion Detection: Identifying moods like sadness，
                                            │ Memory        || Cognition   |    anxiety, anger, etc.
                                            |Logic)         ││ Tagger      │  # Cognition Tagging: Recognizing cognitive distortions 
                                            └───────┬───────┘ └────────────┘   (e.g., catastrophizing, overgeneralization).
                                                    │
                                         ┌──────────▼──────────┐
                                         │    Database Layer   │  ← PostgreSQL / Firebase / FAISS / Pinecone
                                         └──────────┬──────────┘  # Interfaces with a database like one of the above. allows the retrieval 
                                                    |             of the past converesations, supporting context continuity needs between sessions.  
                                                    │
                                         ┌──────────▼──────────┐
                                         │ Therapist Dashboard │  ← Ties directly into memory handler and database component
                                         └─────────────────────┘  # Progress reports, flagged risks, mood trends
