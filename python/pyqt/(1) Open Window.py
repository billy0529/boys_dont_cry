import sys
from PyQt5.QtWidgets import QApplication, QWidget
# -- import modules

class MyApp(QWidget):

    def __init__(self): # self는 MyApp 객체를 의미합니다.
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Billy\'s Application')
        self.move(800,400) # 창 위치
        self.resize(400,200) # 창 크기 가로.세로
        self.show() # 창 보이기


if __name__ == '__main__':
    # '__name__'은 현재 모듈의 이름이 저장되는 내장 변수입니다.
    ## 만약 'moduleA.py'라는 코드를 import해서 예제 코드를 수행하면 __name__ 은 'moduleA'가 됩니다.
    ### 그렇지 않고 코드를 직접 실행한다면 __name__ 은 __main__ 이 됩니다. 
    #### 따라서 이 한 줄의 코드를 통해 프로그램이 직접 실행되는지 혹은 모듈을 통해 실행되는지를 확인합니다. 
    app = QApplication(sys.argv) # PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 합니다.
    ex = MyApp()
    sys.exit(app.exec_())
