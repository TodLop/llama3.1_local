# Llama3.1 Chat Application

This is a simple GUI application built using PyQt5 that allows you to chat with the Llama3.1 model from Ollama. The application is designed to provide a user-friendly, WhatsApp-like interface for interacting with the model running locally.

## Features

- **Chat Interface:** A clean and intuitive interface inspired by WhatsApp, allowing easy interaction with the Llama3.1 model.
- **Asynchronous Processing:** Uses `QThread` to handle requests and responses asynchronously, ensuring the GUI remains responsive during conversations.
- **Real-time Messaging:** Type and send messages in real-time, with responses displayed in a chat-like format.

## Prerequisites

- **Python 3.x**: Make sure you have Python 3 installed on your system.
- **PyQt5**: Install PyQt5 using pip:
  ```bash
  pip install PyQt5

Ollama: Ensure that the Ollama library is installed and properly configured to run the Llama3.1 model locally. You can install the library with:
