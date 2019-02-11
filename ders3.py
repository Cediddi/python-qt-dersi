from PySide2 import QtWidgets, QtCore
from data_conn import mesaj_al, mesaj_gonder

app = QtWidgets.QApplication()
window = QtWidgets.QWidget()
window.setStyleSheet("""
QWidget {
    font-size: 18pt;
    background-color: black;
    border-width: 1px;
    border-color: white;
    border-style: solid;
    color: white;
}
""")

text_area = QtWidgets.QTextEdit(window)
text_area.setReadOnly(True)
text_area.show()

msg_area = QtWidgets.QLineEdit(window)
msg_area.show()

timer = QtCore.QTimer()
timer.setInterval(3000)


def send_msg():
    response = mesaj_gonder("Umut", msg_area.text())
    if response["status"] == "OK":
        msg_area.clear()

def recv_msg():
    data = mesaj_al()["messages"]
    all_text = ""
    last_sender = None
    for d in data:
        if last_sender != d['sender']:
            last_sender = d['sender']
            all_text += "----\n"
        all_text += f"{d['sender']}: {d['message']}\n"
    text_area.setText(all_text)
    sb = text_area.verticalScrollBar()
    sb.setValue(sb.maximum())

timer.timeout.connect(recv_msg)
timer.start()
msg_area.returnPressed.connect(send_msg)

layout = QtWidgets.QVBoxLayout(window)
layout.addWidget(text_area)
layout.addWidget(msg_area)
window.setLayout(layout)
window.show()
app.exec_()
