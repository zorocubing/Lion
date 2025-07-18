import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from pynvml import *

user_input = None

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lion")
        icon_path = os.path.join(getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__))), "Lion.ico")
        self.setWindowIcon(QIcon(icon_path))
        self.setMaximumSize(QSize(200, 40))
        
        self.instructions = QPushButton("?")
        self.instructions.setFixedSize(QSize(40, 40))
        self.instructions.setToolTip("How to use")
        self.instructions.clicked.connect(self.Instructions)

        self.text_box = QLineEdit()
        self.text_box.setPlaceholderText("Enter command...")
        self.text_box.setFixedSize(QSize(200, 40))
        self.text_box.returnPressed.connect(self.command)

        layout = QGridLayout()
        layout.addWidget(self.instructions, 3, 3, Qt.AlignRight | Qt.AlignBottom)
        layout.addWidget(self.text_box, 3, 2, Qt.AlignLeft | Qt.AlignBottom)
        layout.setAlignment(Qt.AlignBottom)
        layout.setAlignment(Qt.AlignTop)
        self.setLayout(layout)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

    def Instructions(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("How to use")
        success_btn = QDialogButtonBox(QDialogButtonBox.Ok)
        success_btn.setCenterButtons(True)
        success_btn.accepted.connect(dlg.accept)
        layout = QVBoxLayout(dlg)
        layout.addWidget(QLabel("How to use Lion \n" "Enter 'Drivers' to get GPU Drivers info. \n" "Enter 'GPU' to get GPU name. \n" "Enter 'CPU' to get CPU info. \n" "Enter 'RAM' to get RAM info."))
        layout.addWidget(success_btn)
        dlg.setLayout(layout)
        icon_path = os.path.join(getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__))), "Lion.ico")
        dlg.setWindowIcon(QIcon(icon_path))
        dlg.exec()

    def command(self):
        global user_input
        user_input = self.text_box.text().strip().lower()
        dlg = QDialog(self)
        dlg.setWindowTitle("Command Result")
        success_btn = QDialogButtonBox(QDialogButtonBox.Ok)
        success_btn.setCenterButtons(True)
        success_btn.accepted.connect(dlg.accept)
        layout = QVBoxLayout(dlg)
        layout.addWidget(QLabel(user_input))
        layout.addWidget(success_btn)
        dlg.setLayout(layout)
        icon_path = os.path.join(getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__))), "Lion.ico")
        dlg.setWindowIcon(QIcon(icon_path))
        dlg.exec()

app = QApplication([])

window = MainWindow()
window.show()

app.exec()