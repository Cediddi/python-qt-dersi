from PySide2 import QtWidgets

from CustomQUiLoader import UiLoader


class MyWidget(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        UiLoader().loadUi('mainwindow.ui', self)
        self.sonradan_isler()
        self.ekran_buffer = []

    def sonradan_isler(self):
        self.bir.clicked.connect(lambda :self.yaz("1"))
        self.iki.clicked.connect(lambda :self.yaz("2"))
        self.uc.clicked.connect(lambda :self.yaz("3"))
        self.dort.clicked.connect(lambda :self.yaz("4"))
        self.bes.clicked.connect(lambda :self.yaz("5"))
        self.alti.clicked.connect(lambda :self.yaz("6"))
        self.yedi.clicked.connect(lambda :self.yaz("7"))
        self.sekiz.clicked.connect(lambda :self.yaz("8"))
        self.dokuz.clicked.connect(lambda :self.yaz("9"))
        self.sifir.clicked.connect(lambda :self.yaz("0"))

    def yaz(self, deger):
        self.ekran_buffer.append(deger)
        self.cikti.setText("".join(self.ekran_buffer))

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MyWidget()
    window.show()
    app.exec_()
