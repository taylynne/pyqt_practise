# learning about singnals and how they work with pqt

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


def greeting():
    """Slot function"""
    if msg.text():
        msg.setText("")
    else:
        msg.setText("<h2>Hello there, beautiful world!</h2><br> What's up")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Signals & Slots")
layout = QVBoxLayout()

btn = QPushButton("Greet")
btn.clicked.connect(greeting) # this connects clicked to greeting()

layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec())