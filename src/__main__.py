import sys

from PySide6.QtWidgets import QApplication

from cloudcompare_python_plugin.MainWindow import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_widget = MainWindow()
    app_widget.show()
    app.exec()
