import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        self.setToolTipDuration(5000)

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButon</b> widget')
        btn.setToolTipDuration(5000) # 툴팁 표시 5초
        btn.move(50,50)
        btn.resize(btn.sizeHint())
    
        self.setWindowTitle('Billy\'s Application')
        self.setGeometry(800,400,400,200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())