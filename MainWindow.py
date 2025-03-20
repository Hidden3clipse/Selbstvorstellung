from PyQt6.QtWidgets import QMainWindow
from CentralWidget import CentralWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Meine Präsentation")
        self.setGeometry(100, 100, 800, 400)  # Größe des Fensters
        self.central_widget = CentralWidget()
        self.setCentralWidget(self.central_widget)
