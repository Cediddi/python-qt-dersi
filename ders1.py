from PySide2 import QtWidgets

app = QtWidgets.QApplication()
window = QtWidgets.QWidget()

text_input = QtWidgets.QLineEdit(window)
text_input.setPlaceholderText("Adınız?")

button = QtWidgets.QPushButton(window)
button.clicked.connect(app.quit)
button.setDisabled(True)


def button_callback():
    text = text_input.text()
    button.setText(f"Sana Da Merhaba Ey {text}")
    text_input.setDisabled(True)
    button.setDisabled(False)


main_layout = QtWidgets.QVBoxLayout(window)
main_layout.addWidget(text_input)
main_layout.addWidget(button)

text_input.returnPressed.connect(button_callback)

window.setLayout(main_layout)
window.show()
app.exec_()
