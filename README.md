# JIT Cloudlet-Based Chatbot Application for Music Festivals


## Getting Started
### Launch application
To run the server, `python3 app.py`

## Overview
This project leverages the innovative Just-in-Time (JIT) Cloudlet architecture to develop edge-native applications. Our primary application is an Avicii-themed chatbot assistant, designed for use at music festivals.

## Motivation
Our goal is to create applications that require high computation, bandwidth, and low latency. Utilizing JIT Cloudlet architecture, this project demonstrates the development and deployment of edge-native applications, showcasing their real-world effectiveness.

## Chatbot Application Features
- **Purpose**: Assists festival-goers with information about the festival, including performers, schedule, and stage locations.
- **Backed by Two LLMs**: The application integrates two specialized Large Language Model backends for accurate, context-specific responses.

### Large Language Models
1. **GODEL**:
   - [Github link](https://github.com/microsoft/GODEL)
   - Open-source model by Microsoft.
   - Trained on 551 million parameters.
   - Provides solid performance without needing internet connectivity.
   - Integrated within the same container as our application backend.

2. **GPT-3.5-Turbo**:
   - [Github Link](https://github.com/openai/openai-python)
   - From OpenAI, behind ChatGPT.
   - Contains 175 Billion trainable parameters.
   - Highly effective but requires a reliable internet connection.

## Open Source Components
- **[Langchain](https://github.com/langchain-ai/langchain)**: Framework for LLM-based applications.
- **[Dash](https://github.com/plotly/dash)**: For building web applications.
- **Hugging-face Embeddings & Sentence-transformers**: For language processing.
- **GODEL**: For goal-oriented dialog systems.

## Innovation
- **Privacy-Focused Cloud Model**: Data remains private to the cloudlet machine, enhancing data privacy.
- **Selective Data Masking**: Exchanges only tokens with APIs, keeping sensitive data within premises.

## Challenges
- **Documentation and Development**: Langchain's documentation required us to explore the codebase for optimal use.
- **NVIDIA-CUDA and ARM Architecture Compatibility**: Standardizing the base image for compatibility and efficiency was challenging.

## Future Work
- **GODEL Fine-Tuning**: To demonstrate robustness without cloud-based services.
- **Improving Temporal Coherence**: For smoother real-time output.

---

This README provides a concise overview of the JIT Cloudlet-based chatbot application, highlighting its motivation, features, technology stack, innovations, challenges, and future work directions.

