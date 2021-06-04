import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QAction, QMainWindow, qApp
from PyQt5.QtGui import QFont, QIcon

class MyApp(QMainWindow):


    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('/Users/hansejin/Documents/Codes/boys_dont_cry/python/Basic Programming/exit.png'), 'Exit', self) # QAction 동작정의후 Exit로 명명
        exitAction.setShortcut('Ctrl+Q') # 종료 단축키 생성
        exitAction.setStatusTip('Exit application') # 상태바에 툴팁

        exitAction.triggered.connect(qApp.quit) 
        # -- 생성된 (triggered) 시그널이 QApplication 위젯의 quit() 메서드에 연결되고, 어플리케이션을 종료시키게 됩니다. 

        self.statusBar()  
    
        menubar = self.menuBar() # 메뉴바 생성
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File') 
        # File 앞에 &는 앰퍼샌드 단축키를 지원하게 합니다. 앞자가 F 이므로 Alt-F를 단축키로 지정합니다.
        filemenu.addAction(exitAction)

        self.setWindowTitle('Billy\'s Application')
        self.setGeometry(800,400,400,200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
