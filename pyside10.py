import PyQt6.QtWidgets as qtw
import PyQt6.QtGui as qtg
from PyQt6.QtCore import Qt
# pip install pyqt-tools
import sys



def press_it():
        with open("filename.xlsx", 'wb') as f:
                f.write('File', f)


class MainWindow(qtw.QWidget):
        def __init__(self):
                super().__init__()
                # Add a title
                self.setWindowTitle("My First App")
                # Set layout
                self.setLayout(qtw.QVBoxLayout())

                # Set size of window
                self.resize(600, 600)

                # Create a QVBoxLayout instance
                layout = qtw.QVBoxLayout()

                # Add widgets to the layout
                layout.addStretch()

                # Set the layout on the application's window
                self.setLayout(layout)
                # Create a Label images
                my_label_img = qtw.QLabel("")
                self.layout().addWidget(my_label_img)
                my_label_img.setPixmap(qtg.QPixmap('images/bee.png'))

                # Create a Label
                my_label = qtw.QLabel("I am File Generator program")
                self.layout().addWidget(my_label)
                font = my_label.font()
                my_label.setFont(font)
                my_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
                # my_label.setAlignment(Qt.AlignmentFlag.AlignTop)
                # my_label.setAlignment(Qt.AlignmentFlag.AlignBottom)
                # Change fon-size of label
                my_label.setFont(qtg.QFont("Georgia", 30))

                # Create the  spinbox box
                my_spinbox = qtw.QSpinBox()
                self.layout().addWidget(my_spinbox)

                my_spinbox.setMinimum(1)
                my_spinbox.setMaximum(10)
                my_spinbox.setPrefix(" file ")

                # Create a button
                my_button = qtw.QPushButton("Click me to GENERATE  ",
                                            clicked=lambda: press_it())
                self.layout().addWidget(my_button)
                my_button.setFont(qtg.QFont("Georgia",16 ))

                # Create new window
                # self.layout().addWidget()
                # Show the app
                self.show()


def run():
        app = qtw.QApplication([])
        mv = MainWindow()
        mv.show()
        app.exec()


if __name__ == '__main__':
        run()
