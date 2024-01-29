# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Slot, Qt, QPoint
from ui_form import Ui_MainWindow


from path_handler import PathHandler
from ABP.time_domain import TimeDomain
from ABP.frequency_domain import FrequencyDomain


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.centralwidget = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.buttons()
        self.connect_checkbox()
        self.connect_action()
        self.to_analyze = []
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 20px;")
        self.ui.scrollArea.setWidget(self.label)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.old_pos = self.pos()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            delta = QPoint(event.globalPos() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        pass




    def buttons(self):
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton = self.ui.analyze_button.clicked.connect(self.check_values)

    def check_values(self):
        if len(self.to_analyze) == 0:
            self.label.setText("No values to compute")

        else:
            print(self.to_analyze)
            self.label.setText("The computed domains are " + ", ".join([str(n) for n in self.to_analyze]))
    def connect_checkbox(self):
        self.ui.time_checkbox.stateChanged.connect(self.on_time_checkbox_state_changed)
        self.ui.frequency_checkbox.stateChanged.connect(self.on_frequency_checkbox_state_changed)

    def on_time_checkbox_state_changed(self, state):
        if state:
            self.to_analyze.append("time")
        else:
            self.to_analyze.remove("time")

    def on_frequency_checkbox_state_changed(self, state):
        if state:
            self.to_analyze.append("frequency")
        else:
            self.to_analyze.remove("frequency")

    def connect_action(self):
        self.ui.actionClose.triggered.connect(self.close)
        self.ui.actionSave_to_file.triggered.connect(self.save_to_file)

    def save_to_file(self):
        print("save to file")







if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
