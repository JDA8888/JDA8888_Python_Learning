# PyQt5 Images

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Cool First GUI Window code thingy yay")
        self.setGeometry(700, 300, 500, 500)
        
        label = QLabel(self)
        label.setGeometry(0, 0, 300, 300)
        
        pixmap = QPixmap("BroCode_Python_Learning/profile_pic.jpg")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        
        label.setGeometry(0,
                          0,
                          label.width(),
                          label.height())
       
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()