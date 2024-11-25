"le lien github est :https://github.com/BadreddineIheb/Test "
import socket
import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QMainWindow, QLineEdit, QPushButton, QApplication

class InterfaceGraphique(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)

        self.server = QLabel("serveur")
        self.text_server = QLineEdit("localhost")
        self.port = QLabel("port")
        self.text_port = QLineEdit("4200")
        self.NBR_Client_max = QLabel("Nombre de clients maximum")
        self.text_NBR = QLineEdit("5")
        self.connect = QPushButton("Démarrage du serveur")
        self.result_display = QLineEdit("")
        self.result_display.setEnabled(False)
        self.quit_button = QPushButton("Quitter")

        grid.addWidget(self.server, 0, 0)
        grid.addWidget(self.text_server, 0, 1)
        grid.addWidget(self.port, 1, 0)
        grid.addWidget(self.text_port, 1, 1)
        grid.addWidget(self.NBR_Client_max, 2, 0)
        grid.addWidget(self.text_NBR, 2, 1)
        grid.addWidget(self.connect, 3, 1)
        grid.addWidget(self.result_display, 4, 1, 1, 5)
        grid.addWidget(self.quit_button, 5, 1)

        self.quit_button.clicked.connect(self.actionQuitter)
        self.connect.clicked.connect(self.__demarrage)

        self.setWindowTitle("le serveur de tchat")
        self.resize(400, 150)
    def __demarrage(self):
        set.self.connect = QPushButton("arret du serveur")
        host = 'localhost'
        port = 4200
        server_socket = socket.socket()
        server_socket.bind((host, port))
        server_socket.listen(5)
        data = server_socket.recv(1024)

        while True:
            conn, addr = server_socket.accept()

            while True:
                self.result_display = QLineEdit(print(data))
                if not data:
                    break

                print(f"Reçu de {addr} : {data}")

                response = f"Le serveur a reçu : {data}"
                conn.send(response.encode())

            print(f"Connexion fermée avec {addr}")

    def actionQuitter(self):
            QCoreApplication.exit(0)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InterfaceGraphique()
    window.show()
    app.exec_()


