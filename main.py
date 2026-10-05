import sys
import ollama
import json
import os
from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QTextEdit,QPushButton

class DesktopAI(QWidget):
    def __init__(self):
        super().__init__()
        self.messages = []
        self.filename = "conversation.json"
        self.initUI()
        self.load_message()

    def initUI(self):
        self.setWindowTitle("Desktop AI")
        self.setGeometry(300,150,800,500)

        self.input_box = QLineEdit(self)
        self.input_box.setPlaceholderText("Enter Message")
        self.input_box.setGeometry(50,50,700,40)

        self.response_box = QTextEdit(self)
        self.response_box.setGeometry(50,100,700,300)

        self.send_button = QPushButton("Send",self)
        self.send_button.setGeometry(300,420,200,40)
        self.send_button.clicked.connect(self.send_message)


    def send_message(self):
        message = self.input_box.text().strip()
        if message:
            self.messages.append({"role":"user","content":message})
            response = ollama.chat(
                model = "qwen2.5:0.5b",
                messages = self.messages
            )
            answer = response["message"]["content"]
            self.messages.append({"role":"assistant","content":answer})
            self.save_message()
            self.response_box.append("You:" + message)
            self.response_box.append("Assistant:" + answer)
            self.input_box.clear()

    def save_message(self):
        with open(self.filename, "w") as file:
            json.dump(self.messages,file)

    def load_message(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.messages = json.load(file)

            for message in self.messages:
                if message["role"] == "user":
                    self.response_box.append("You:" + message["content"])

                else:
                    self.response_box.append("Assistant:" + message["content"])






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DesktopAI()
    window.show()
    sys.exit(app.exec_())




