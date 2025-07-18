import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from pynvml import *
import psutil

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
        self.text_box.returnPressed.connect(self.text_box.clear)

        layout = QGridLayout()
        layout.addWidget(self.instructions, 3, 3, Qt.AlignRight | Qt.AlignBottom)
        layout.addWidget(self.text_box, 3, 2, Qt.AlignLeft | Qt.AlignBottom)
        layout.setAlignment(Qt.AlignBottom)
        layout.setAlignment(Qt.AlignTop)
        self.setLayout(layout)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

    @staticmethod
    def bytes2human(n):
        symbols = ('B', 'KB', 'MB', 'GB', 'TB', 'PB')
        prefix = {}
        for i, s in enumerate(symbols):
            prefix[s] = 1 << (i * 10)
        for s in reversed(symbols):
            if n >= prefix[s]:
                value = float(n) / prefix[s]
                return '%.1f %s' % (value, s)
        return '%s B' % n

    @staticmethod
    def pprint_ntuple(nt):
        result = []
        for name in nt._fields:
            value = getattr(nt, name)
            if name != 'percent':
                value = MainWindow.bytes2human(value)
            result.append('{:<10} : {:>7}'.format(name.capitalize(), value))
        return '\n'.join(result)

    def Instructions(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("How to use")
        success_btn = QDialogButtonBox(QDialogButtonBox.Ok)
        success_btn.setCenterButtons(True)
        success_btn.accepted.connect(dlg.accept)
        layout = QVBoxLayout(dlg)
        layout.addWidget(QLabel("How to use Lion \n" "Enter 'GPU' to get GPU info. \n" "Enter 'CPU' to get CPU info. \n" "Enter 'RAM' to get RAM info."))
        layout.addWidget(success_btn)
        dlg.setLayout(layout)
        icon_path = os.path.join(getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__))), "Lion.ico")
        dlg.setWindowIcon(QIcon(icon_path))
        dlg.exec()

    def command(self):
        global user_input
        user_input = self.text_box.text().strip().lower()
        if user_input == "gpu":
            self.gpu_command()
        elif user_input == "cpu":
            self.cpu_command()
        elif user_input == "ram":
            self.ram_command()
        else:
            self.error_command()

    def gpu_command(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("GPU Command")
        success_btn = QDialogButtonBox(QDialogButtonBox.Ok)
        success_btn.setCenterButtons(True)
        success_btn.accepted.connect(dlg.accept)
        layout = QVBoxLayout(dlg)
        nvmlInit()
        device_count = nvmlDeviceGetCount()
        if device_count > 0:
            gpu_info = nvmlDeviceGetHandleByIndex(0)
            gpu_name = nvmlDeviceGetName(gpu_info)
            driver_version = nvmlSystemGetDriverVersion()
            utilization = nvmlDeviceGetUtilizationRates(gpu_info)
            layout.addWidget(QLabel(f"GPU Name: {gpu_name}"))
            layout.addWidget(QLabel(f"Driver Version: {driver_version}"))
            layout.addWidget(QLabel(f"GPU Usage: {utilization.gpu}%"))
            layout.addWidget(QLabel(f"VRAM Usage: {utilization.memory}%"))
            nvmlShutdown()
        else:
            layout.addWidget(QLabel("No GPU found."))
        layout.addWidget(success_btn)
        dlg.setLayout(layout)
        icon_path = os.path.join(getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__))), "Lion.ico")
        dlg.setWindowIcon(QIcon(icon_path))
        dlg.exec()

    def cpu_command(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("CPU Command")
        success_btn = QDialogButtonBox(QDialogButtonBox.Ok)
        success_btn.setCenterButtons(True)
        success_btn.accepted.connect(dlg.accept)
        layout = QVBoxLayout(dlg)
        cpu_usage = psutil.cpu_percent()
        layout.addWidget(QLabel(f"CPU Usage: {cpu_usage}%"))
        layout.addWidget(success_btn)
        dlg.setLayout(layout)
        icon_path = os.path.join(getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__))), "Lion.ico")
        dlg.setWindowIcon(QIcon(icon_path))
        dlg.exec()

    def ram_command(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("RAM Command")
        success_btn = QDialogButtonBox(QDialogButtonBox.Ok)
        success_btn.setCenterButtons(True)
        success_btn.accepted.connect(dlg.accept)
        layout = QVBoxLayout(dlg)
        ram_info = psutil.virtual_memory()
        ram_text = "RAM Information \n" + MainWindow.pprint_ntuple(ram_info)
        label = QLabel(ram_text)
        label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        layout.addWidget(label)
        layout.addWidget(success_btn)
        dlg.setLayout(layout)
        icon_path = os.path.join(getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__))), "Lion.ico")
        dlg.setWindowIcon(QIcon(icon_path))
        dlg.exec()

    def error_command(self):
        global user_input
        user_input = self.text_box.text().strip().lower()
        dlg = QDialog(self)
        dlg.setWindowTitle("Error Command")
        success_btn = QDialogButtonBox(QDialogButtonBox.Ok)
        success_btn.setCenterButtons(True)
        success_btn.accepted.connect(dlg.accept)
        layout = QVBoxLayout(dlg)
        layout.addWidget(QLabel(f"Huh?! {user_input}? Be serious! \n" "Please enter 'GPU', 'CPU', or 'RAM'."))
        layout.addWidget(success_btn)
        dlg.setLayout(layout)
        icon_path = os.path.join(getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__))), "Lion.ico")
        dlg.setWindowIcon(QIcon(icon_path))
        dlg.exec()

app = QApplication([])

window = MainWindow()
window.show()

app.exec()