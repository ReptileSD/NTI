import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSpinBox, QPushButton, QMainWindow, QLabel, QLineEdit, QLCDNumber
from PyQt5.QtCore import pyqtSignal


class MainWindow(QWidget):
    resized = pyqtSignal()

    def __init__(self):
        self.settings = [0, 0, 0, 0, 0]
        super().__init__()
        self.initUI()

    def resizeEvent(self, event):
        self.resized.emit()
        return super().resizeEvent(event)

    def initUI(self):
        self.setGeometry(100, 100, 1500, 800)
        self.setWindowTitle('Настройки микроклимата (By \"It\'s a secret\")')
        self.resized.connect(self.update_size)

        self.temp_spin = QSpinBox(self)
        self.temp_spin.resize(100, self.temp_spin.height())
        self.temp_spin.setSingleStep(50)
        self.temp_spin.setMaximum(1500)
        self.temp_spin.setMinimum(0)
        self.temp_spin.hide()

        self.hum_spin = QSpinBox(self)
        self.hum_spin.resize(100, self.hum_spin.height())
        self.hum_spin.setSingleStep(100)
        self.hum_spin.setMinimum(0)
        self.hum_spin.setMaximum(10000)
        self.hum_spin.hide()

        self.co2_spin = QSpinBox(self)
        self.co2_spin.resize(100, self.co2_spin.height())
        self.co2_spin.setSingleStep(1)
        self.co2_spin.setMinimum(0)
        self.co2_spin.setMaximum(10000)
        self.co2_spin.hide()

        self.bright_spin = QSpinBox(self)
        self.bright_spin.resize(100, self.bright_spin.height())
        self.bright_spin.setSingleStep(500)
        self.bright_spin.setMinimum(0)
        self.bright_spin.setMaximum(1000000)
        self.bright_spin.hide()

        self.pressure_spin = QSpinBox(self)
        self.pressure_spin.resize(100, self.pressure_spin.height())
        self.pressure_spin.setSingleStep(1000)
        self.pressure_spin.setMinimum(0)
        self.pressure_spin.setMaximum(1000000)
        self.pressure_spin.hide()

        self.curLabel = QLabel(self)
        self.curLabel.setText('Состояние:')

        self.setLabel = QLabel(self)
        self.setLabel.setText('Настройки:')

        self.temp_label = QLabel(self)
        self.temp_label.setText('Температура')

        self.hum_label = QLabel(self)
        self.hum_label.setText('Влажность')

        self.co2_label = QLabel(self)
        self.co2_label.setText('Концетрация Co2')

        self.bright_label = QLabel(self)
        self.bright_label.setText('Освещенность')

        self.pressure_label = QLabel(self)
        self.pressure_label.setText('Давление')

        self.temp_LCD_cur = QLCDNumber(self)
        self.temp_LCD_cur.setNumDigits(10)

        self.hum_LCD_cur = QLCDNumber(self)
        self.hum_LCD_cur.setNumDigits(10)

        self.co2_LCD_cur = QLCDNumber(self)
        self.co2_LCD_cur.setNumDigits(10)

        self.bright_LCD_cur = QLCDNumber(self)
        self.bright_LCD_cur.setNumDigits(10)

        self.pressure_LCD_cur = QLCDNumber(self)
        self.pressure_LCD_cur.setNumDigits(10)

        self.temp_LCD_set = QLCDNumber(self)
        self.temp_LCD_set.setNumDigits(10)

        self.hum_LCD_set = QLCDNumber(self)
        self.hum_LCD_set.setNumDigits(10)

        self.co2_LCD_set = QLCDNumber(self)
        self.co2_LCD_set.setNumDigits(10)

        self.bright_LCD_set = QLCDNumber(self)
        self.bright_LCD_set.setNumDigits(10)

        self.pressure_LCD_set = QLCDNumber(self)
        self.pressure_LCD_set.setNumDigits(10)

        self.settings_btn = QPushButton(self)
        self.settings_btn.setText('Изменить настройки')
        self.settings_btn.resize(self.settings_btn.sizeHint())
        self.settings_btn.clicked.connect(self.open_settings)

        self.change_settings_btn = QPushButton(self)
        self.change_settings_btn.setText('Применить настройки')
        self.change_settings_btn.resize(self.change_settings_btn.sizeHint())
        self.change_settings_btn.clicked.connect(self.change_settings)
        self.change_settings_btn.hide()

        self.update_info('36.6', '50.35', '0.000', '100000', '98066.5')

    def change_settings(self):
        self.settings_btn.show()
        self.curLabel.show()
        self.setLabel.show()
        self.temp_LCD_cur.show()
        self.temp_LCD_set.show()
        self.hum_LCD_cur.show()
        self.hum_LCD_set.show()
        self.co2_LCD_cur.show()
        self.co2_LCD_set.show()
        self.bright_LCD_cur.show()
        self.bright_LCD_set.show()
        self.pressure_LCD_cur.show()
        self.pressure_LCD_set.show()
        self.change_settings_btn.hide()
        self.temp_spin.hide()
        self.hum_spin.hide()
        self.co2_spin.hide()
        self.bright_spin.hide()
        self.pressure_spin.hide()
        self.update_settings()

    def open_settings(self):
        self.settings_btn.hide()
        self.curLabel.hide()
        self.setLabel.hide()
        self.temp_LCD_cur.hide()
        self.temp_LCD_set.hide()
        self.hum_LCD_cur.hide()
        self.hum_LCD_set.hide()
        self.co2_LCD_cur.hide()
        self.co2_LCD_set.hide()
        self.bright_LCD_cur.hide()
        self.bright_LCD_set.hide()
        self.pressure_LCD_cur.hide()
        self.pressure_LCD_set.hide()
        self.change_settings_btn.show()
        self.temp_spin.show()
        self.hum_spin.show()
        self.co2_spin.show()
        self.bright_spin.show()
        self.pressure_spin.show()


    def update_size(self):
        self.settings_btn.move(self.width() * 0.15, self.height() * 0.95)
        self.change_settings_btn.move(self.width() * 0.455, self.height() * 0.93)

        self.temp_spin.move(self.width() * 0.55, self.height() * 0.13)
        self.hum_spin.move(self.width() * 0.55, self.height() * 0.31)
        self.co2_spin.move(self.width() * 0.55, self.height() * 0.49)
        self.bright_spin.move(self.width() * 0.55, self.height() * 0.68)
        self.pressure_spin.move(self.width() * 0.55, self.height() * 0.85)

        self.temp_label.move(self.width() * 0.475, self.height() * 0.13)
        self.hum_label.move(self.width() * 0.48, self.height() * 0.31)
        self.co2_label.move(self.width() * 0.47, self.height() * 0.49)
        self.bright_label.move(self.width() * 0.47, self.height() * 0.68)
        self.pressure_label.move(self.width() * 0.48, self.height() * 0.85)

        self.curLabel.move(self.width() * 0.78, self.height() * 0.04)
        self.temp_LCD_cur.resize(self.width() * 0.3, self.height() * 0.13)
        self.temp_LCD_cur.move(self.width() * 0.65, self.height() * 0.08)

        self.hum_LCD_cur.resize(self.width() * 0.3, self.height() * 0.13)
        self.hum_LCD_cur.move(self.width() * 0.65, self.height() * 0.26)

        self.co2_LCD_cur.resize(self.width() * 0.3, self.height() * 0.13)
        self.co2_LCD_cur.move(self.width() * 0.65, self.height() * 0.44)

        self.bright_LCD_cur.resize(self.width() * 0.3, self.height() * 0.13)
        self.bright_LCD_cur.move(self.width() * 0.65, self.height() * 0.63)

        self.pressure_LCD_cur.resize(self.width() * 0.3, self.height() * 0.13)
        self.pressure_LCD_cur.move(self.width() * 0.65, self.height() * 0.8)

        self.setLabel.move(self.width() * 0.18, self.height() * 0.04)
        self.temp_LCD_set.resize(self.width() * 0.3, self.height() * 0.13)
        self.temp_LCD_set.move(self.width() * 0.05, self.height() * 0.08)

        self.hum_LCD_set.resize(self.width() * 0.3, self.height() * 0.13)
        self.hum_LCD_set.move(self.width() * 0.05, self.height() * 0.26)

        self.co2_LCD_set.resize(self.width() * 0.3, self.height() * 0.13)
        self.co2_LCD_set.move(self.width() * 0.05, self.height() * 0.44)

        self.bright_LCD_set.resize(self.width() * 0.3, self.height() * 0.13)
        self.bright_LCD_set.move(self.width() * 0.05, self.height() * 0.63)

        self.pressure_LCD_set.resize(self.width() * 0.3, self.height() * 0.13)
        self.pressure_LCD_set.move(self.width() * 0.05, self.height() * 0.8)

    def update_info(self, t, h, co, br, pr):  # Состояние
        self.temp_LCD_cur.display(f'{t} C\'')
        self.hum_LCD_cur.display(f'{h} \'o')
        self.co2_LCD_cur.display(f'{co} \'o')
        self.bright_LCD_cur.display(f'{br} lu')
        self.pressure_LCD_cur.display(f'{pr} Pa')

    def update_settings(self):  # Настройки
        self.settings = [self.temp_spin.value(),
                         self.hum_spin.value(),
                         self.co2_spin.value(),
                         self.bright_spin.value(),
                         self.pressure_spin.value()]

        self.temp_LCD_set.display(f'{self.settings[0] / 10} C\'')
        self.hum_LCD_set.display(f'{self.settings[1] / 100} \'o')
        self.co2_LCD_set.display(f'{self.settings[2] / 1000} \'o')
        self.bright_LCD_set.display(f'{self.settings[3]} lu')
        self.pressure_LCD_set.display(f'{self.settings[4] / 10} Pa')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
