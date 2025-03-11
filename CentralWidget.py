from PyQt6.QtCore import Qt, pyqtSlot
from PyQt6.QtWidgets import QWidget, QGridLayout, QSlider, QPushButton
from pkg_resources import safe_listdir


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        slider = QSlider(Qt.Orientation.Horizontal)
        slider.sliderReleased.connect(self.on_slider_released)
        #slider.sliderMoved.connect(self.on_slider_moved)

        slider_v = QSlider(Qt.Orientation.Vertical)
        push_button_1 = QPushButton("Hallo Welt")
        push_button_2 = QPushButton("Hier nicht drücken")

        grid_layout = QGridLayout()

        grid_layout.addWidget(push_button_1, 0, 0)
        grid_layout.addWidget(push_button_2, 0, 1)
        grid_layout.addWidget(slider_v, 0, 2, 2, 1)
        grid_layout.addWidget(slider, 1, 0, 1, 2)

        self.setLayout(grid_layout)

    @pyqtSlot(int)
    def on_slider_moved(self, value):
        print("slider moved to " + str(value))

    @pyqtSlot()
    def on_slider_released(self):
        print("slider released")

        value = self.sender().value()
        print("value = " + str(value))

