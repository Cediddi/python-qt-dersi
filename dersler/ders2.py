import datetime
import json
import os

from PySide2 import QtWidgets, QtCore, QtGui


class MainWindow(QtWidgets.QMainWindow):
    def build(self):
        self.setCentralWidget(QtWidgets.QWidget())

        self.build_widgets()
        self.build_layout()
        self.build_events()
        self.calculate_bmi()

    def calculate_bmi(self):
        boy = self.slider1.value()
        kilo = self.dial1.value()
        bmi = kilo / ((boy / 100) ** 2)
        self.line1.setText(f"{bmi:.03f}")

        colors = [QtCore.Qt.yellow, QtCore.Qt.green, QtCore.Qt.yellow, QtCore.Qt.red]
        data = {
            "Kadın": [(0, 19.1), (19.1, 25.8), (25.8, 27.3), (27.3, 32.2)],
            "Erkek": [(0, 20.7), (20.7, 26.4), (26.4, 27.8), (27.8, 31.1)],
            "Bebek": [(0, 15), (15, 19), (19, 25), (25, 35)],
        }
        degerler = data[self.combo1.currentText()]
        renk = QtCore.Qt.darkRed
        for index, (alt, ust) in enumerate(degerler):
            if alt < bmi < ust:
                renk = colors[index]
                break

        palette1 = QtGui.QPalette()
        palette1.setColor(palette1.Background, renk)
        self.line1.setAutoFillBackground(True)
        self.line1.setPalette(palette1)

    def reset(self):
        self.text1.clear()
        self.slider1.setValue(1)
        self.dial1.setValue(1)
        self.spin1.setValue(1)
        self.combo1.setCurrentIndex(0)

    def ac(self):

        file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(self, "Aç", os.path.expanduser("~/"),
                                                                     "Json File (*.json)")

        with open(file_name) as f:
            data = json.load(f)

        self.text1.setText(data["not"])
        self.slider1.setValue(data["boy"])
        self.dial1.setValue(data["kilo"])
        self.spin1.setValue(data["yas"])

        kategori_index = self.combo1.findData(data["kategori"])
        self.combo1.setCurrentIndex(kategori_index)


    def kaydet(self):
        file_name, file_type = QtWidgets.QFileDialog.getSaveFileName(self, "Kaydet", os.path.expanduser("~/"),
                                                                     "Json File (*.json)")

        not_ = self.text1.toPlainText()
        boy = self.slider1.value()
        kilo = self.dial1.value()
        yas = self.spin1.value()
        kategori = self.combo1.currentText()
        bmi = self.line1.text()
        tarih = datetime.datetime.now().isoformat()

        with open(file_name, "w") as f:
            json.dump({
                "not": not_,
                "boy": boy,
                "kilo": kilo,
                "yas": yas,
                "kategori": kategori,
                "bmi": bmi,
                "tarih": tarih,
            }, f)

    def build_widgets(self):
        self.label1 = QtWidgets.QLabel()
        self.label1.setText("Notlar:")

        self.label2 = QtWidgets.QLabel()
        self.label2.setText("Boyunuz:")

        self.label3 = QtWidgets.QLabel()
        self.label3.setText("Kilonuz:")

        self.label4 = QtWidgets.QLabel()
        self.label4.setText("Yaşınız:")

        self.label5 = QtWidgets.QLabel()
        self.label5.setText("BMI kategoriniz:")

        self.label6 = QtWidgets.QLabel()
        self.label6.setText("BMI:")

        self.text1 = QtWidgets.QTextEdit()

        self.line1 = QtWidgets.QLineEdit()
        self.line1.setDisabled(True)

        self.spin1 = QtWidgets.QSpinBox()
        self.spin1.setMinimum(1)
        self.spin1.setMaximum(100)

        self.lcd1 = QtWidgets.QLCDNumber()
        self.lcd1.display(1)

        self.lcd2 = QtWidgets.QLCDNumber()
        self.lcd2.display(1)

        self.slider1 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider1.setMinimum(1)
        self.slider1.setMaximum(300)
        self.slider1.setValue(1)

        self.dial1 = QtWidgets.QDial()
        self.dial1.setMinimum(1)
        self.dial1.setMaximum(300)
        self.dial1.setValue(1)

        self.combo1 = QtWidgets.QComboBox()
        self.combo1.addItem("Kadın")
        self.combo1.addItem("Erkek")
        self.combo1.addItem("Bebek")

        self.button1 = QtWidgets.QPushButton()
        self.button1.setText("Aç")

        self.button2 = QtWidgets.QPushButton()
        self.button2.setText("Kaydet")

        self.button3 = QtWidgets.QPushButton()
        self.button3.setText("Temizle")

    def build_layout(self):
        self.main_layout = QtWidgets.QVBoxLayout()

        self.layout1 = QtWidgets.QHBoxLayout()
        self.layout1.addWidget(self.lcd1)
        self.layout1.addWidget(self.slider1)

        self.layout2 = QtWidgets.QHBoxLayout()
        self.layout2.addWidget(self.lcd2)
        self.layout2.addWidget(self.dial1)

        self.layout3 = QtWidgets.QHBoxLayout()
        self.layout3.addWidget(self.label4)
        self.layout3.addWidget(self.spin1)

        self.layout4 = QtWidgets.QHBoxLayout()
        self.layout4.addWidget(self.label5)
        self.layout4.addWidget(self.combo1)

        self.layout5 = QtWidgets.QHBoxLayout()
        self.layout5.addWidget(self.label6)
        self.layout5.addWidget(self.line1)

        self.layout6 = QtWidgets.QHBoxLayout()
        self.layout6.addWidget(self.button1)
        self.layout6.addWidget(self.button2)
        self.layout6.addWidget(self.button3)

        self.main_layout.addWidget(self.label1)
        self.main_layout.addWidget(self.text1)
        self.main_layout.addWidget(self.label2)
        self.main_layout.addLayout(self.layout1)
        self.main_layout.addWidget(self.label3)
        self.main_layout.addLayout(self.layout2)
        self.main_layout.addLayout(self.layout3)
        self.main_layout.addLayout(self.layout4)
        self.main_layout.addLayout(self.layout5)
        self.main_layout.addLayout(self.layout6)

        self.centralWidget().setLayout(self.main_layout)

    def build_events(self):
        self.slider1.valueChanged.connect(self.lcd1.display)
        self.slider1.valueChanged.connect(self.calculate_bmi)
        self.dial1.valueChanged.connect(self.lcd2.display)
        self.dial1.valueChanged.connect(self.calculate_bmi)
        self.combo1.activated.connect(self.calculate_bmi)
        self.button1.clicked.connect(self.ac)
        self.button2.clicked.connect(self.kaydet)
        self.button3.clicked.connect(self.reset)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.build()
    window.show()
    app.exec_()
