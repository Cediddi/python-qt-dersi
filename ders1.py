from PySide2 import QtCore, QtWidgets

app = QtWidgets.QApplication()

label = QtWidgets.QLabel()
label.setText("Merhaba Dünya")
label.show()

button = QtWidgets.QPushButton()
button.setText("Sana Da Merhaba Ey Yazar")
button.clicked.connect(app.quit)

timer = QtCore.QTimer()
timer.singleShot(1000, lambda: (button.show(), label.hide()))

app.exec_()
