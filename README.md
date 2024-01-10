# llm-chat

## Overview
Our focus centered on managing a music festival, leading to the creation of our first application: an Avicii-themed chatbot assistant. This assistant, designed to help guests with inquiries about the festival, performers, schedule, and stage locations, is supported by two specialized Large Language Model (LLM) backends. These backends are expertly tailored to provide accurate and context-specific responses related to the music festival. <br>
One of our Large Language Models, named GODEL, is an open-source model developed by Microsoft for crafting goal-oriented dialog systems. It is integrated directly within the same container as our application backend. Trained on 551 million parameters, GODEL offers solid performance while eliminating the need for internet connectivity. <br>
The second model we use is the renowned GPT-3.5-Turbo from OpenAI, the driving force behind ChatGPT. With a significantly higher number of trainable parameters (175 Billion), this model excels in effectiveness. However, this efficiency comes at a price and requires a reliable internet connection, which can be a challenging dependency.

## Getting Started

### Prerequisites
yet to update stuff

### Launch application
To run the server, `python3 app.py`