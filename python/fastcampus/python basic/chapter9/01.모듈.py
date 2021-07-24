# 모듈
## 파이썬으로 작성한 모든 어플리케이션은 전부 모듈
# 내장 모듈 - 자동으로 설치된 기본 모듈
import sys
import math 
print(math.pi) 
print(math.ceil(5.6))    #반올림

from math import pi     # 결과는 위와 동일. 모듈명을 생략한다.
from math import ceil as c  # ceil에 대해 alias 설정
print(pi) 
print(c(5.6))

# 외부 모듈 - 다른사람이 만든 파이썬 파일을 pip로 가져옴
import pyautogui as pg
pg.moveTo(500, 500, duration=2)


