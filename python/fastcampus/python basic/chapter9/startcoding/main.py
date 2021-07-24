# 1. import 패키지.모듈
import unit.character
unit.character.test()

# 2. from 페키지 import 모듈
from unit import item as i
i.test()

# 3. from 패키지 import * 전부다 가져옴
# * 의 경우 __init__을 수정해야함. 파일 참고
from unit import *
monster.test()

# 4. import 패키지
import unit
unit.monster.test()
