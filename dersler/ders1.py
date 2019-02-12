from PySide2 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def build(self):
        self.setCentralWidget(QtWidgets.QWidget())

        self.build_widgets()
        self.build_layout()
        self.build_events()

    def return_pressed_callback(self):
        text = self.text_input.text()
        self.button.setText(f"Sana Da Merhaba Ey {text}")
        self.text_input.setDisabled(True)
        self.button.setDisabled(False)

    def button_clicked_callback(self):
        self.button.setDisabled(True)
        self.button.setText("Merhaba Dünya")
        self.text_input.clear()

    def reset_clicked_callback(self):
        self.text_input.setDisabled(False)
        self.text_input.clear()
        self.button.setDisabled(True)
        self.button.setText("---")

    def build_widgets(self):
        self.text_input = QtWidgets.QLineEdit(self.centralWidget())
        self.text_input.setPlaceholderText("Adınız?")

        self.button = QtWidgets.QPushButton(self.centralWidget())
        self.button.setText("---")
        self.button.setDisabled(True)

        self.reset_button = QtWidgets.QPushButton(self.centralWidget())
        self.reset_button.setText("Reset")

    def build_layout(self):
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.text_input)
        self.main_layout.addWidget(self.button)
        self.main_layout.addWidget(self.reset_button)

        self.centralWidget().setLayout(self.main_layout)

    def build_events(self):
        self.text_input.returnPressed.connect(self.return_pressed_callback)
        self.button.clicked.connect(self.button_clicked_callback)
        self.reset_button.clicked.connect(self.reset_clicked_callback)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.build()
    window.show()
    app.exec_()
