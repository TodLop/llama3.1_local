import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QLabel, QScrollArea
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import ollama

class OllamaWorker(QThread):
    response_received = pyqtSignal(str)

    def __init__(self, message):
        super().__init__()
        self.message = message

    def run(self):
        try:
            response = ollama.chat(model="llama3.1", messages=[
                {'role': 'user', 'content': self.message},
            ])
            if 'message' in response:
                assistant_response = response['message']['content']
                self.response_received.emit(assistant_response)
            else:
                self.response_received.emit("Error in fetching response.")
        except Exception as e:
            self.response_received.emit(f"Error: {str(e)}")

class WhatsAppLikeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Chat with Llama3.1')
        self.setGeometry(100, 100, 500, 550)

        # Main widget and layout
        self.central_widget = QWidget(self)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.setCentralWidget(self.central_widget)

        # Chat display area
        self.scroll_area = QScrollArea(self)
        self.chat_widget = QWidget()
        self.chat_layout = QVBoxLayout(self.chat_widget)
        self.scroll_area.setWidget(self.chat_widget)
        self.scroll_area.setWidgetResizable(True)
        self.main_layout.addWidget(self.scroll_area)

        # Input area and button at the bottom
        self.bottom_layout = QHBoxLayout()
        self.message_input = QTextEdit(self)
        self.message_input.setPlaceholderText('Enter your message here...')
        self.message_input.installEventFilter(self)
        self.send_button = QPushButton('Send Message', self)
        self.send_button.clicked.connect(self.send_message)
        self.bottom_layout.addWidget(self.message_input)
        self.bottom_layout.addWidget(self.send_button)
        self.main_layout.addLayout(self.bottom_layout)

        # Set up initial layout for the chat
        self.chat_layout.setAlignment(Qt.AlignTop)
        self.chat_layout.addStretch()
        self.chat_widget.setLayout(self.chat_layout)

    def eventFilter(self, source, event):
        if event.type() == event.KeyPress and source is self.message_input:
            if event.key() == Qt.Key_Return and not event.modifiers() & Qt.ShiftModifier:
                self.send_message()
                return True
            elif event.key() == Qt.Key_Return and event.modifiers() & Qt.ShiftModifier:
                cursor = self.message_input.textCursor()
                cursor.insertText('\n')
                return True
        return super().eventFilter(source, event)

    def send_message(self):
        user_message = self.message_input.toPlainText().strip()
        if user_message:
            self.display_message(user_message, is_user=True)
            self.message_input.clear()
            self.send_request_to_ollama(user_message)

    def send_request_to_ollama(self, message):
        self.worker = OllamaWorker(message)
        self.worker.response_received.connect(self.handle_response)
        self.worker.start()

    def handle_response(self, response):
        self.display_message(response, is_user=False)

    def display_message(self, message, is_user=True):
        message_label = QLabel(message)
        message_label.setWordWrap(True)
        message_label.setStyleSheet("QLabel { background-color : %s; color : %s; padding: 8px; border-radius: 15px; }"
                                    % ("#4886ff" if is_user else "#f0f0f0", "white" if is_user else "black"))
        if is_user:
            message_label.setAlignment(Qt.AlignRight)
        else:
            message_label.setAlignment(Qt.AlignLeft)
        self.chat_layout.addWidget(message_label)

def main():
    app = QApplication(sys.argv)
    ex = WhatsAppLikeApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
