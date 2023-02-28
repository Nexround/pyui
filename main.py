# import sys
from PySide6 import QtWidgets
from ui_pytools import Ui_MainWindow

class MyWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.show()
    app.exec()
    # sys.exit(app.exec())
