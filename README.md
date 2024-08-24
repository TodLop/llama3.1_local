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
- **Ollama**: Ensure that the Ollama library is installed and properly configured to run the Llama3.1 model locally. You can install the library with:
  ```bash
  pip install ollama

## Installation

1. **Clone the Repository:**
   -Clone this repository to your local machine:
     ```bash
     git clone https://github.com/TodLop/7zip-compression-tool-for-upnote.git
2. **Install Dependencies:**
   -Ensure all dependencies are installed by running:
   ```bash
     pip install -r requirements.txt
3. **Run the Application:**
   -Start the application by running the Python script:
   ```bash
   python llama3.1_chat_app.py

## Chat Interface

   - The main window will open, allowing you to enter your messages in the text box at the bottom.
   - Press 'Enter' or click the "Send Message" button to send your message to Llama3.1.
   - The response from Llama3.1 will appear on the left side of the char interface, while your messages appear on the right.

## Keyboard Shortcuts:
- Press 'Enter' to send a message.
- Press 'Shift + Enter' to add a new line within the message input field.

## Customization
- **UI Customization:**
  - You can modify the look and feel of the chat bubbles by changing the styles in the 'display_message' method in the code.
- **Model and API Settings:**
  - The script is currently configured to use the Llama3.1 model. You can modify the 'OllamaWorker' class if you wish to change the model or adjust API parameters.

---

This README.MD has been Created by OpenAI's GPT-4O.
