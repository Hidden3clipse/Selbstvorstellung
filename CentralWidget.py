from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
import sys


class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.current_page = 0  # Seitenindex
        self.text_index = 0  # Index für die Stichpunkte
        self.texts = []  # Liste für die Stichpunkte
        self.hobby_labels = {}  # Dictionary für die Hobby-Beschreibungen
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Hauptüberschrift
        self.title = QLabel("Meine Präsentation")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet("font-size: 32px; font-weight: bold;")
        self.layout.addWidget(self.title)

        # Unterüberschrift (dynamisch änderbar)
        self.subtitle = QLabel("")
        self.subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subtitle.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.subtitle.setVisible(False)
        self.layout.addWidget(self.subtitle)

        # Container für Inhalte (Texte, Buttons)
        self.content_container = QWidget()
        self.content_layout = QVBoxLayout()
        self.content_container.setLayout(self.content_layout)
        self.layout.addWidget(self.content_container)

        # Button-Layout für Next und Weiter
        self.button_layout = QHBoxLayout()

        self.text_button = QPushButton("Weiter")
        self.text_button.clicked.connect(self.show_next_text)
        self.button_layout.addWidget(self.text_button, alignment=Qt.AlignmentFlag.AlignRight)

        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.next_page)
        self.button_layout.addWidget(self.next_button, alignment=Qt.AlignmentFlag.AlignRight)

        self.layout.addLayout(self.button_layout)
        self.setLayout(self.layout)

    def next_page(self):
        self.clear_content()
        self.current_page += 1

        if self.current_page == 1:
            self.animate_title()
            self.show_hobbies()
        elif self.current_page == 2:
            self.subtitle.setText("Duales Studium Cybersecurity")
            self.subtitle.setVisible(True)
            self.texts = ["Technische Grundlagen", "Netzwerksicherheit", "Penetration Testing", "Sicherheitsmanagement",
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
        else:
            self.close()

    def animate_title(self):
        self.title.setStyleSheet("font-size: 24px;")
        self.subtitle.setText("Hobbys")
        self.subtitle.setVisible(True)

    def show_hobbies(self):
        hobbies = {
            "Lesen": "Bücher & Wissen erweitern.",
            "Fremd- & Programmiersprachen": "Neue Sprachen und Code lernen.",
            "Videospiele": "Strategie & Spaß.",
            "Instrument spielen": "Musikalische Kreativität.",
            "Gym": "Fitness & Gesundheit.",
            "Zeit für Freunde & Familie": "Gemeinsame Erlebnisse genießen."
        }

        hobby_layout = QHBoxLayout()
        self.description_labels = {}

        for hobby, description in hobbies.items():
            button = QPushButton(hobby)
            label = QLabel("")  # Leere Beschreibung
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setStyleSheet("font-size: 16px;")

            button.clicked.connect(lambda checked, lbl=label, desc=description: lbl.setText(desc))

            hobby_layout.addWidget(button)
            self.content_layout.addWidget(label)
            self.hobby_labels[hobby] = label

        self.content_layout.addLayout(hobby_layout)

    def show_clickable_texts(self):
        self.text_index = 0

    def show_next_text(self):
        if self.text_index < len(self.texts):
            label = QLabel(self.texts[self.text_index])
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setStyleSheet("font-size: 18px;")
            self.content_layout.insertWidget(self.text_index, label)
            self.text_index += 1

    def clear_content(self):
        for label in self.hobby_labels.values():
            label.clear()
        while self.content_layout.count():
            item = self.content_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        self.hobby_labels.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CentralWidget()
    window.setWindowTitle("Meine Präsentation")
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())
