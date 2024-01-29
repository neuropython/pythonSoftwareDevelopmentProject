# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Slot, Qt, QPoint
from ui_form import Ui_MainWindow
import ast


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

            # read the path and change it to the correct format
            path = self.path.replace("file:///", "")
            path = path.replace("/", "\\")

            # change the file names to the correct format
            lst = ast.literal_eval(self.file_names)

            # create the path handler object
            founded_files = PathHandler(path, lst).all_alaized_names

            self.label.setText("Founded files" + ", ".join([str(n) for n in founded_files]))



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

    def save_to_file(self):
        print("save to file")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
