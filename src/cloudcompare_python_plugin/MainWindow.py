from PySide6.QtWidgets import QMainWindow

from .main_window_ui import Ui_MainWindow
from . import __about__


class MainWindow(QMainWindow):
    """The GUI Application."""

    def __init__(
        self,
        parent = None,
    ):
        """Construct the GUI Application.

        Parameters
        ----------
        parent : Optional[QWidget]
            An optional parent. Should be None if run as standalone but could
            be a parent QWidget from the base application if run as a plugin

        """
        super().__init__(parent)
        self.inc = 1
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(f"CloudCompare Python Plugin v{__about__.__version__}")

        # Click on pushButton
        self.ui.pushButton.clicked.connect(self._increase_spinbox)

        # Click on radioButton
        self.ui.radioButton.clicked.connect(self._display_message)

        # Click on radioButton_2
        self.ui.radioButton_2.clicked.connect(self._display_message_2)

        # Click on checkBox
        self.ui.checkBox.clicked.connect(self._checked)

    def _increase_spinbox(self):
        self.ui.spinBox.setValue(self.ui.spinBox.value() + self.inc)

    def _display_message(self):
        self.ui.plainTextEdit.appendPlainText("radioButton clicked")

    def _display_message_2(self):
        self.ui.plainTextEdit.appendPlainText("radioButton_2 clicked")

    def _checked(self):
        if self.ui.checkBox.isChecked():
            self.inc = 2
        else:
            self.inc = 1
        self.ui.plainTextEdit.appendPlainText(f"increment set to {self.inc}")
