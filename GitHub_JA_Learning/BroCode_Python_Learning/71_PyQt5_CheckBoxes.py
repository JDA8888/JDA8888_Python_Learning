# Checkboxes in PyQt5

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QCheckBox)
from PyQt5.QtCore import Qt




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Cool First GUI Window code thingy yay")
        self.setGeometry(700, 300, 500, 500)
        self.checkbox = QCheckBox("Do You really want to play Battle Field 6???", self)
        self.initUI()
        
        
    def initUI(self):
        self.checkbox.setGeometry(0,0,600,200)
        self.checkbox.setStyleSheet("font-size: 26px;"
                                    "font-family: Arial;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_change)
        
    def checkbox_change(self, state):
        if state == Qt.Checked:
            print("You BET BOYYY LETS GET AT IT! ! ! ")
        else:
            print("Well its either Battle field 6 or..... nothing?")
        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()