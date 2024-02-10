from PyQt6.QtWidgets import *

import traceback


def showException(exception):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Critical)
    msg.setWindowTitle("Fehler")
    msg.setText(type(exception).__name__)
    msg.setInformativeText(str(exception))
    msg.setDetailedText("".join(traceback.format_exception(type(exception), exception, exception.__traceback__)))
    msg.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    msg.show()
    exit_code = msg.exec()


def showInfo(title: str, text: str):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Information)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.show()
    exit_code = msg.exec()


def showConfirmation(title: str, text: str):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Question)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    msg.show()
    return msg.exec()
