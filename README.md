Desktop AI

A simple desktop AI chatbot built with Python, PyQt5, and Ollama.

The application provides a graphical interface where users can send messages to a locally running AI model and receive responses. Conversation history is stored locally in a JSON file so that previous conversations can be loaded when the application starts.

Features

Simple PyQt5 graphical user interface

Local AI responses using Ollama

Uses the qwen2.5:0.5b model

Conversation history during the current session

Saves conversations to conversation.json

Loads previous conversations automatically

Prevents empty messages from being sent

Displays both user and assistant messages

Technologies Used

Python

PyQt5

Ollama

Qwen 2.5 0.5B

JSON

How It Works

The basic flow of the application is:

User

  ↓
PyQt5 GUI

  ↓
Python

  ↓
Ollama

  ↓
Qwen 2.5 0.5B

  ↓
Python

  ↓
PyQt5 GUI

Conversation history is maintained in self.messages and saved locally to:

conversation.json

When the application starts, it checks whether the conversation file exists. If it does, the previous conversation is loaded into the application.

Requirements

Install Python and Ollama, then install the required Python packages:

pip install PyQt5 ollama

You also need the Ollama model:

ollama pull qwen2.5:0.5b
Running the Application

Start the application with:

python main.py

Make sure Ollama is installed and available on your computer before running the application.

Project Structure
DesktopAI/
│

├── main.py

├── .gitignore

├── README.md

└── conversation.json

conversation.json contains local conversation history and should normally be excluded from GitHub if it contains personal conversations.

Learning Project

This project was created as a Python and PyQt5 learning project.

It demonstrates practical use of:

Classes and inheritance

PyQt5 widgets

Signals and slots

Methods

Lists and dictionaries

JSON file handling

Reading and writing files

Conditional statements

Conversation history

Local AI integration

Future Improvements

Possible future improvements include:

Clear conversation button

Delete conversation history

Multiple AI models

Better message formatting

Chat timestamps

Improved GUI design

Error handling for Ollama connection problems
Model selection from the GUI
Author

Okechukwu Igbelina

This project is part of my ongoing journey to learn Python, PyQt5, local AI, and desktop application development.