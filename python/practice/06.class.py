## class 실습

# 다음의 결과와 같이 국어, 영어, 수학 점수를 입력받아 합계를 구하는 객체지향 코드를 작성하십시오.
# 이 때 학생 클래스의 객체는 객체 생성 시 국어, 영어, 수학 점수를 저장하며, 총점을 구하는 메서드를 제공합니다.
class Scores_class:
    def __init__(self,name):
        self.name = name
    def total_score_def(self,korean,english,math):
        total_score = korean + english + math
        print("{0}님의 총 점수는 {1} 입니다.".format(self.name, total_score))
    def subj_score_def(self,korean,english,math):
        while True:
            subj = input("과목을 입력하세요. (국어,영어,수학) >>> ")
            if subj == "국어":print ("{0}님의 국어 점수는 {1}점 입니다.".format(self.name,korean));break
            elif subj == "영어":print ("{0}님의 영어 점수는 {1}점 입니다.".format(self.name,english));break
            elif subj == "수학":print ("{0}님의 수학 점수는 {1}점 입니다.".format(self.name,math));break
            else:print("=== 잘못 입력하셨습니다. 다시 입력해주세요 ===")
billy = Scores_class("세진")
billy.total_score_def(70,80,90)
billy.subj_score_def(70,80,90)
print("")


# 국적을 출력하는 printNationality 정적 메서드를 갖는 Korean 클래스를 정의하고
# 메서드를 호출하는 코드를 작성해봅시다.# 
class Korean:
    nationality = "대한민국"
    @classmethod
    def printNationality(cls):
        return cls.nationality
print(Korean.printNationality())
