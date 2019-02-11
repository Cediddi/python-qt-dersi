from PySide2 import QtWidgets

from CustomQUiLoader import UiLoader
from narcelik import narcelik_rcc


class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        UiLoader().loadUi('untitled.ui', self)
        self.pushButton_6.clicked.connect(app.exit)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MyWidget()
    window.show()
    app.exec_()
