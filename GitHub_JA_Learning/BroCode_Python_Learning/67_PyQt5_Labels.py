# PyQt5 QLabels

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Cool First GUI Window code thingy yay")
        self.setGeometry(700, 300, 500, 500)
        
        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #292929;"
                            "background-color: #6fdcf7;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        
        # label.setAlignment(Qt.AlignTop)  # Vertically to the top 
        #label.setAlignment(Qt.AlignBottom) # Vertically bottom
        # label.setAlignment(Qt.AlignVCenter) # Vertically Center
        
        # label.setAlignment(Qt.AlignRight) # Horizontally right
        # label.setAlignment(Qt.AlignHCenter) # Horizontally Center
        # label.setAlignment(Qt.AlignLeft) # Horizontally left 
        
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # Center and Top
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # Center and Bottom
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # Center and Center
        
        label.setAlignment(Qt.AlignCenter) # Sets both to center. (H and V)
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()