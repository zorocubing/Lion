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
        self.resize(QSize(200, 40))
        
        instructions = QPushButton("?")
        instructions.setFixedSize(QSize(40, 40))
        instructions.setToolTip("How to use")
        instructions.clicked.connect(self.instructions)

        text_box = QLineEdit()
        text_box.setPlaceholderText("Type here...")
        text_box.setFixedSize(QSize(200, 40))

        layout = QGridLayout()
        layout.addWidget(instructions, 3, 3, Qt.AlignRight | Qt.AlignBottom)
        layout.addWidget(text_box, 3, 2, Qt.AlignLeft | Qt.AlignBottom)
        layout.setAlignment(Qt.AlignBottom)
        layout.setAlignment(Qt.AlignTop)
        self.setLayout(layout)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

    def instructions(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("How to use")
        success_btn = QDialogButtonBox(QDialogButtonBox.Ok)
        success_btn.setCenterButtons(True)
        success_btn.accepted.connect(dlg.accept)
        layout = QVBoxLayout(dlg)
        layout.addWidget(QLabel("How to use Lion \n" "Type in 'Drivers' to get GPU Drivers info. \n" "Type in 'GPU' to get GPU name. \n" "Type in 'Memory' to get Memory info. \n" "Type in 'CPU' to get CPU info."))
        layout.addWidget(success_btn)
        dlg.setLayout(layout)
        icon_path = os.path.join(getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__))), "Lion.ico")
        dlg.setWindowIcon(QIcon(icon_path))
        dlg.exec()


app = QApplication([])

window = MainWindow()
window.show()

app.exec()