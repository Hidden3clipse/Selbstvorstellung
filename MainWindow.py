from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QPixmap, QPalette, QBrush
from CentralWidget import CentralWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Selbstpräsentation")
        self.setGeometry(100, 100, 800, 400)  # Größe des Fensters

        # Hintergrundbild setzen
        self.setAutoFillBackground(True)
        palette = self.palette()
        pixmap = QPixmap("pos.jpg")  # Pfad zu deinem Hintergrundbild
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))  # QPixmap in QBrush umwandeln
        self.setPalette(palette)

        self.central_widget = CentralWidget()
        self.setCentralWidget(self.central_widget)