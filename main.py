import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from pynvml import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lion")
        icon_path = os.path.join(getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__))), "Lion.ico")
        self.setWindowIcon(QIcon(icon_path))
        self.resize(QSize(200, 50))
        
        instructions = QPushButton("Instructions")
        instructions.setMinimumSize(QSize(200, 50))
        instructions.setToolTip("Click to get instructions")
        instructions.clicked.connect(self.instructions)

        layout = QVBoxLayout()
        layout.addWidget(instructions)
        self.setLayout(layout)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

    def instructions(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("Instructions")
        success_btn = QDialogButtonBox(QDialogButtonBox.Ok)
        success_btn.setCenterButtons(True)
        success_btn.accepted.connect(dlg.accept)
        layout = QVBoxLayout(dlg)
        layout.addWidget(QLabel("How to use Lion? \n" "Type in 'Drivers' to get GPU Drivers info. \n" "Type in 'GPU' to get GPU name. \n" "Type in 'Memory' to get Memory info. \n" "Type in 'CPU' to get CPU info."))
        layout.addWidget(success_btn)
        dlg.setLayout(layout)
        icon_path = os.path.join(getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__))), "Lion.ico")
        dlg.setWindowIcon(QIcon(icon_path))
        dlg.exec()


app = QApplication([])

window = MainWindow()
window.show()

app.exec()