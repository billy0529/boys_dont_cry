import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow
from PyQt5.QtGui import QFont

class MyApp(QMainWindow): # QMainWindow 클래스의 statusBar() 메소드를 사용


    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready') 
        # -- QMainWindow 클래스의 statusBar() 메소드를 최초로 호출
        ## 그 다음 호출부터는 상태바 객체를 반환
    
        self.setWindowTitle('Billy\'s Application')
        self.setGeometry(800,400,400,200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())