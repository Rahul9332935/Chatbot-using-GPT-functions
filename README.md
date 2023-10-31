# Chatbot-using-GPT-functions
# Chatbot with OpenAI GPT-3.5 Turbo

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [License](#license)

## Introduction

Welcome to the Chatbot with OpenAI GPT-3.5 Turbo project! This is a web-based chatbot application that leverages the power of OpenAI's GPT-3.5 Turbo model. It allows users to have real-time conversations with an AI chatbot.

## Features

- **Real-Time Chat**: Engage in conversations with an AI chatbot in real time.
- **Chat Interface**: Messages are displayed in a chat-like interface for a natural interaction experience.
- **Typing Indicator**: The bot simulates typing, creating a more engaging conversation.
- **Automatic Scrolling**: The chat interface automatically scrolls to show the latest messages.

## Tech Stack

- **Backend**: The backend of this application is powered by Flask, a lightweight web framework for Python.
- **AI Model**: We use the OpenAI GPT-3.5 Turbo model for generating chatbot responses.
- **Frontend**: The frontend interface is built using HTML for structure and JavaScript for real-time interaction and UI updates.

## Getting Started

Follow these steps to get started with the Chatbot:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Rahul9332935/Chatbot-using-GPT-functions.git

2. Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt

3. Create an OpenAI account and obtain an API key.

Update the Flask app configuration with your OpenAI API key. Open the app.py file and set your API key:

     ```python
  
    # Update your OpenAI API key here
    OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
    W_API="YOUR WEATHER API KEY

4. Start the Flask app:

    ```bash
   python app.py
Open a web browser and access the application at http://localhost:8080.

## Usage

To use the chatbot:

1. Enter a message in the input field and click "Send" to initiate a conversation with the chatbot.
2. The chat history is displayed in a chat-like interface, and the bot's responses are shown with a typing effect.
3. The `run_conversation` function is a powerful feature of this chatbot. It can track real-time weather information. When you ask about the weather, the chatbot fetches and displays the current weather for a given location.

### Example:

```markdown
User: What's the weather in San Francisco?
Bot: The weather in San Francisco is currently 72°F.

