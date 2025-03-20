from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QPalette, QBrush
import sys


class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.current_page = 0
        self.text_index = 0
        self.texts = []
        self.hobby_labels = {}
        self.icon_labels = {}  # Dictionary für Icons
        self.initUI()

    def initUI(self):
        # Hintergrundbild setzen
        self.setAutoFillBackground(True)
        palette = self.palette()
        pixmap = QPixmap("hintergrund.jpg")  # Pfad zu deinem Hintergrundbild
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))  # QPixmap in QBrush umwandeln
        self.setPalette(palette)

        # Hauptlayout
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Hauptüberschrift
        self.title = QLabel("Fabian Rödel")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet("font-size: 32px; font-weight: bold; color: black;")  # Textfarbe auf Schwarz setzen
        self.main_layout.addWidget(self.title)

        # Unterüberschrift
        self.subtitle = QLabel("")
        self.subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subtitle.setStyleSheet("font-size: 24px; font-weight: bold; color: black;")  # Textfarbe auf Schwarz setzen
        self.subtitle.setVisible(False)
        self.main_layout.addWidget(self.subtitle)

        # Container für Inhalte (Texte, Buttons)
        self.content_container = QWidget()
        self.content_layout = QVBoxLayout()
        self.content_container.setLayout(self.content_layout)
        self.main_layout.addWidget(self.content_container)

        # Button-Layout für Next und X (permanent unten)
        self.button_layout = QHBoxLayout()

        self.text_button = QPushButton("X")
        self.text_button.clicked.connect(self.show_next_text)
        self.button_layout.addWidget(self.text_button, alignment=Qt.AlignmentFlag.AlignLeft)

        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.next_page)
        self.button_layout.addWidget(self.next_button, alignment=Qt.AlignmentFlag.AlignRight)

        # Button-Layout zum Hauptlayout hinzufügen
        self.main_layout.addLayout(self.button_layout)

        # Hauptlayout setzen
        self.setLayout(self.main_layout)

    def next_page(self):
        self.clear_content()
        self.current_page += 1

        if self.current_page == 1:
            self.animate_title()
            self.show_hobbies()
        elif self.current_page == 2:
            self.subtitle.setText("Duales Studium - Cybersecurity")
            self.subtitle.setVisible(True)
            self.texts = ["Technische Grundlagen", "Netzwerksicherheit", "Sicherheitsmanagement",
                          "Digitale Forensik"]
            self.text_index = 0
            self.show_clickable_texts()
        elif self.current_page == 3:
            self.subtitle.setText("Schaeffler mein Arbeitgeber")
            self.subtitle.setVisible(True)
            self.texts = ["Innovative Technologien", "Globale Karrierechancen", "Nachhaltige Mobilität",
                          "Teamarbeit & Kultur", "Persönliche Weiterentwicklung"]
            self.text_index = 0
            self.show_clickable_texts()
        elif self.current_page == 4:
            self.subtitle.setText("Stärken und Schwächen")
            self.subtitle.setVisible(True)
            self.texts = ["Stärke: Teamfähigkeit", "Stärke: Lernbereitschaft", "Schwäche: Perfektionismus",
                          "Schwäche: Ungeduld"]
            self.text_index = 0
            self.show_clickable_texts()
        else:
            self.close()

    def animate_title(self):
        self.title.setStyleSheet("font-size: 24px; color: black;")  # Textfarbe auf Schwarz setzen
        self.subtitle.setText("Interessen")
        self.subtitle.setVisible(True)

    def show_hobbies(self):
        hobbies = {
            "Lesen": ("Fantasy, Krimis und Thriller", "book-open-cover.png"),  # Icon für Lesen
            "Fremd- & Programmiersprachen": ("Japanisch, Python, Java", "cyborg.png"),  # Icon für Sprachen
            "Gym": ("Selbstdisziplin und Fitness", "dumbbell-heart.png"),  # Icon für Gym
            "Zeit mit Freunden & Familie": ("Essen gehen, Fußball, Kino", "users-alt.png")  # Icon für Familie
        }

        hobby_layout = QHBoxLayout()
        self.description_labels = {}

        for hobby, (description, icon_path) in hobbies.items():
            button = QPushButton(hobby)
            label = QLabel("")  # Leere Beschreibung
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setStyleSheet("font-size: 16px; color: black;")  # Textfarbe auf Schwarz setzen

            # Icon erstellen, aber zunächst unsichtbar
            icon = QPixmap(icon_path)
            icon_label = QLabel()
            icon_label.setPixmap(icon.scaled(24, 24, Qt.AspectRatioMode.KeepAspectRatio))  # Icon auf 24x24 skalieren
            icon_label.setStyleSheet("margin-right: 5px;")  # Abstand zwischen Icon und Text
            icon_label.setVisible(False)  # Icon zunächst unsichtbar

            # Layout für Icon und Text
            hbox = QHBoxLayout()
            hbox.addWidget(icon_label)
            hbox.addWidget(label)
            hbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

            # Container für Icon und Text
            container = QWidget()
            container.setLayout(hbox)

            # Klick-Funktion für den Button
            button.clicked.connect(lambda checked, lbl=label, icon_lbl=icon_label, desc=description: (
                lbl.setText(desc),
                icon_lbl.setVisible(True)  # Icon sichtbar machen
            ))

            hobby_layout.addWidget(button)
            self.content_layout.addWidget(container)
            self.hobby_labels[hobby] = label
            self.icon_labels[hobby] = icon_label  # Icon speichern

        self.content_layout.addLayout(hobby_layout)

    def show_clickable_texts(self):
        self.text_index = 0

    def show_next_text(self):
        if self.text_index < len(self.texts):
            label = QLabel(self.texts[self.text_index])
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setStyleSheet("font-size: 18px; color: black;")  # Textfarbe auf Schwarz setzen
            self.content_layout.insertWidget(self.text_index, label)
            self.text_index += 1

    def clear_content(self):
        for label in self.hobby_labels.values():
            label.clear()
        for icon_label in self.icon_labels.values():
            icon_label.setVisible(False)  # Icons wieder unsichtbar machen
        while self.content_layout.count():
            item = self.content_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        self.hobby_labels.clear()
        self.icon_labels.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CentralWidget()
    window.setWindowTitle("Meine Präsentation")
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())