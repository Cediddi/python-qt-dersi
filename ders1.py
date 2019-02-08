from PySide2 import QtCore, QtWidgets

app = QtWidgets.QApplication()

text_input = QtWidgets.QLineEdit()
text_input.setPlaceholderText("Adınız?")
text_input.show()

button = QtWidgets.QPushButton()
button.clicked.connect(app.quit)


def button_callback():
    text = text_input.text()
    button.setText(f"Sana Da Merhaba Ey {text}")
    text_input.hide()
    button.show()


text_input.returnPressed.connect(button_callback)

app.exec_()
