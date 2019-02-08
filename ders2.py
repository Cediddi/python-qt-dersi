from PySide2 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def build(self):
        self.setCentralWidget(QtWidgets.QWidget())

        self.build_widgets()
        self.build_layout()
        self.build_events()

    def build_widgets(self):
        pass

    def build_layout(self):
        self.main_layout = QtWidgets.QLayout()

        self.centralWidget().setLayout(self.main_layout)

    def build_events(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.build()
    window.show()
    app.exec_()
