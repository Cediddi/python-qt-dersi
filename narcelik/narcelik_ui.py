from PySide2 import QtWidgets

from narcelik import narcelik_uic
app = QtWidgets.QApplication()


class MyWidget(narcelik_uic.Ui_Form):
    def __init__(self):
        super().__init__()
        self.main_widget = QtWidgets.QWidget()
        self.setupUi(self.main_widget)
        self.retranslateUi(self.main_widget)
        self.pushButton_6.clicked.connect(app.exit)

    def show(self):
        self.main_widget.show()


def main():
    window = MyWidget()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
