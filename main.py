from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QFormLayout
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont
from PyQt5.QtCore import Qt
import sys
import riot_data_get


# Subclass QMainWindow to customize your application's main window
class lineEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.name = ""


        Player_Id = QLineEdit()
        Player_Id.textChanged.connect(self.textchanged)
        Player_Id.editingFinished.connect(self.enterPress)

        flo = QFormLayout()
        flo.addRow("Player_Id", Player_Id)

        self.setLayout(flo)
        self.setWindowTitle("QLineEdit Example")

    def textchanged(self, text):
        self.name = text


    def enterPress(self):
        self.account_info = riot_data_get.get_accunt_info(self.name)
        # check id typo?

        print("Enter pressed")

        # self.setWindowTitle("My App")
        # button = QPushButton("Press Me!")

        # Set the central widget of the Window.
        # self.setCentralWidget(button)

if __name__ == "__main__":




        app = QApplication(sys.argv)
        win = lineEditDemo()
        win.show()
        sys.exit(app.exec_())
