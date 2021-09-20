from PyQt5.QtWidgets import QMessageBox


class WarningQDialog(QMessageBox):
    def __init__(self, message, parents=None):
        super(WarningQDialog, self).__init__()
        self.message = message
        self.initUI(self.message)

    def initUI(self, message):
        self.warningdialog = QMessageBox.warning(self, "ERROR", self.message, QMessageBox.Abort)
