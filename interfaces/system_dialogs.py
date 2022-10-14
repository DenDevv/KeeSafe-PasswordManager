from PyQt5 import QtWidgets


class SystemDialog():
    def dialog_handler(self, title, message, icon, buttons):
        dialog = QtWidgets.QMessageBox()
        dialog.setWindowTitle(title)
        dialog.setText(message)
        dialog.setIcon(icon)
        dialog.setStandardButtons(buttons)
        dialog.exec_()