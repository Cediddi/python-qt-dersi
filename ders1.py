from PySide2 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def build(self):
        self.setCentralWidget(QtWidgets.QWidget())

        self.build_widgets()
        self.build_layout()
        self.build_events()

    def button_callback(self):
        text = self.text_input.text()
        self.button.setText(f"Sana Da Merhaba Ey {text}")
        self.text_input.setDisabled(True)
        self.button.setDisabled(False)

    def build_widgets(self):
        self.text_input = QtWidgets.QLineEdit(self.centralWidget())
        self.text_input.setPlaceholderText("Adınız?")

        self.button = QtWidgets.QPushButton(self.centralWidget())
        self.button.setDisabled(True)

    def build_layout(self):
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.text_input)
        self.main_layout.addWidget(self.button)

        self.centralWidget().setLayout(self.main_layout)

    def build_events(self):
        self.text_input.returnPressed.connect(self.button_callback)
        self.button.clicked.connect(app.quit)


app = QtWidgets.QApplication()
window = MainWindow()
window.build()
window.show()
app.exec_()
