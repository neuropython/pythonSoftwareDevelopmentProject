# This Python file uses the following encoding: utf-8
import sys
import pandas as pd
import time

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog
from PySide6.QtCore import Slot, Qt, QPoint
from ui_form import Ui_MainWindow

import ast
import webbrowser

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
        self.ui.scrollArea.setWidget(self.label)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.old_pos = self.pos()
        self.ui.actionSave_to_file.setDisabled(True)

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
        self.pushButton = self.ui.analyze_button.clicked.connect(self.download_data)
        self.pushButton = self.ui.analyze_button.clicked.connect(self.check_values)

    def check_values(self):
        if (len(self.sampling_rate) == 0 or len(self.file_names) == 0 or len(self.window_size) == 0
                or len(self.overlap) == 0 or len(self.path) == 0 or len(self.to_analyze) ==0 ):
            self.label.setText("Do not leave values empty")
            self.label.setStyleSheet("""
             color: #ff5757;
             font-size: 20px;
             """)
        else:
            self.label.setText("Analizing and the computed domains are " + ", ".join([str(n) for n in self.to_analyze]))
            self.label.setStyleSheet("""
             color: #00ff00;
             font-size: 20px;
             """)

            self.ui.actionSave_to_file.setDisabled(False)

            # read the path and change it to the correct format
            path = self.path.replace("file:///", "")
            path = path.replace("/", "\\")

            # change the file names to the correct format
            lst = ast.literal_eval(self.file_names)

            # create the path handler object
            try:
                ph = PathHandler(path, lst)
                founded_files = ph.all_alaized_files_names
                signals = ph.signals
            except Exception as e:
                self.label.setText(f"An error occurred: {e} - perhaps due to bad data format")
                self.label.setStyleSheet("""
                 color: #ff5757;
                    font-size: 20px;
                    """)


            self.label.setText("Founded files: \n" + "\n,".join([str(n) for n in founded_files]))

            time.sleep(5)

            current_text = ""

            for i,j in signals, founded_files:
                try:
                    if "time" in self.to_analyze:
                        td = TimeDomain(i)
                        current_text = current_text + f"Time domain: {td}" + "\n"
                except Exception as e:
                     current_text = f"An error occurred with signal (name) {j}: {e}" + "\n"
                try:
                    if "frequency" in self.to_analyze:
                        fd = FrequencyDomain(i, self.sampling_rate, self.window_size, self.overlap)
                        current_text = current_text + f"Frequency domain: {fd}" + "\n"
                except Exception as e:
                    current_text = current_text + f"An error occurred with signal (name) {j}: {e}" + "\n"

            self.label.setText(current_text)


    def download_data(self):
        self.sampling_rate = self.ui.samplingRateEditTxt.toPlainText()
        self.file_names = self.ui.fileNamesEditTxt.toPlainText()
        self.window_size = self.ui.windowSizeEditTxt.toPlainText()
        self.overlap = self.ui.overlapEditTxt.toPlainText()
        self.path = self.ui.plainTextEdit.toPlainText()


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
        self.ui.menuHow_to_use.triggered.connect(self.navigate)

    def save_to_file(self):
        print("save to file")
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        with open(file_name, "w") as f:
            f.write(self.label.text())

    def navigate(self):
        print("navigate")
        webbrowser.open(r"https://github.com/neuropython/pythonSoftwareDevelopmentProject/blob/main/README.md")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
