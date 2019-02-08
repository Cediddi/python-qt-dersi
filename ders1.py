from PySide2 import QtWidgets
app = QtWidgets.QApplication()

label = QtWidgets.QLabel()
label.setText("Merhaba Dünya")
label.show()

app.exec_()