import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QAction, QMainWindow, qApp
from PyQt5.QtGui import QFont, QIcon

class MyApp(QMainWindow):


    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('/Users/hansejin/Documents/Codes/boys_dont_cry/python/Basic Programming/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q') 
        exitAction.setStatusTip('Exit application') 
        exitAction.triggered.connect(qApp.quit) 

        self.statusBar()  
    
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.setWindowTitle('Billy\'s Application')
        self.setGeometry(800,400,400,200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    