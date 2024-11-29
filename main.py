from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, \
    QPushButton, QLineEdit, QMessageBox, QComboBox
import sys
import traceback



def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    print("Uncaught exception:", exc_type, exc_value)
    traceback.print_tb(exc_traceback)

sys.excepthook = handle_exception


class AverageSpeedCalculater(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Average Speed Calculator')
        grid = QGridLayout()

        # Create widgets
        distance_label = QLabel('distance:')
        self.distance_line_edit = QLineEdit()
        self.measure_box = QComboBox()
        time_label = QLabel('Time (hours):')
        self.time_line_edit = QLineEdit()
        self.calculate_button = QPushButton('Calculate')
        self.out_put = QLabel('')

        self.measure_box.addItems(['Metric (km)', 'Imperial (miles)'])

        # Condition based on combo box value
        selected_option = self.measure_box.currentText()

        # Add widget
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(self.measure_box, 1, 2)
        grid.addWidget(self.calculate_button, 2, 1 )
        grid.addWidget(self.out_put, 3, 0, 1, 2)

        self.setLayout(grid)

        self.calculate_button.clicked.connect(self.calculate_speed)

    def calculate_speed(self):
        distance = self.distance_line_edit.text()
        time_needed = self.time_line_edit.text()
        # If distance an time field are empty QmessageBox display
        if not distance or not time_needed:
            QMessageBox.warning(self, "Input Error",
                                "Distance field cannot be empty!")
            return
        try:
            distance = float(distance)
            time_needed = float(time_needed)
            measure_unit = self.measure_box.currentText()[8:].strip('()')
            speed = distance / time_needed
            print(distance)
            print(type(distance))
            if measure_unit == 'km':
                self.out_put.setText(f'The speed is {round(speed, 2)} '
                                     f'{measure_unit} per hour.')

            else:
                measure_unit = self.measure_box.currentText()[10:].strip('()')
                self.out_put.setText(f'The speed is {round(speed * 0.621371, 2 )} '
                                     f'{measure_unit} per hour.')
        except ValueError:
            QMessageBox.critical(self, "Input Error",
                                 "Please enter a valid decimal number for distance!")

        else:
            self.out_put.setText('Please fill distance and time')

        print(time_needed)
        print(type(time_needed))


        print(self.measure_box.currentText()[7:].strip('()'))



app = QApplication(sys.argv)
if __name__ == '__main__':
    try:
        average_speed_calculater = AverageSpeedCalculater()
        average_speed_calculater.show()
        sys.exit(app.exec())
    except Exception as e:
        print("An error occurred:", e)