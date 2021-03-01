import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Billy\'s Application')
        self.setWindowIcon(QIcon('/Users/hansejin/Documents/Codes/boys_dont_cry/python/Basic Programming/web.png')) # 파일위치에 따라 경로를 따로 조정해야함
        self.setGeometry(800,400,400,200) # move, resize를 통합
        self.show() 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
