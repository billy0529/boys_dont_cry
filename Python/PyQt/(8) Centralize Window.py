import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget

class MyApp(QWidget):


    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Billy\'s Application')
        self.resize(500,300)
        self.center() ## center 메소드로 창이 가운데로 오도록
        self.show()

    def center(self):
        qr = self.frameGeometry() ## 창의 크기와 위치 정보를 가져옵니다.
        cp = QDesktopWidget().availableGeometry().center() # 모니터의 화면 가운데 위치를 파악합니다.
        qr.moveCenter(cp) # 중심으로 이동
        self.move(qr.topLeft()) 
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

