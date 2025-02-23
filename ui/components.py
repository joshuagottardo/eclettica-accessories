from PySide6.QtWidgets import QMessageBox

class CustomMessageBox:
    def __init__(self, icon=QMessageBox.NoIcon, title="", text="", buttons=QMessageBox.Ok):
        self.icon = icon
        self.title = title
        self.text = text
        self.buttons = buttons

    def show(self):
        msg_box = QMessageBox()
        msg_box.setIcon(self.icon)
        msg_box.setWindowTitle(self.title)
        msg_box.setText(self.text)
        msg_box.setStandardButtons(self.buttons)
        return msg_box.exec()