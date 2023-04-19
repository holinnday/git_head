# (2) SUPER 클래스

class Parent:
    # 생성자 : 객체 + 초기화
    def __init__(self, name, job):
        self.name = name
        self.job = job

    #멤버 함수(method)
    def display(self):
        print('name : {}, job : {}' .format(self.name, self.job))
# 부모 클래스 객체 생성
P = Parent('홍길동', '회사원')
P.display()

# 자식클래스 
class Children(Parent): #parent 클래스 상속
    gender = None #자식 클래스 멤버 변수 추가

    # 자식 클래스 생성자
    def __init__(self, name, job, gender):
        # 부모 클래스 생성자 호출
        super().__init__(name, job) #name, job 초기화
        self.gender = gender # 자식 멤버변수 초기화

    # 멤버 함수 매서드
    def display(self):
        print('name : {}, job : {}, gender : {}' .format(self.name, self.job, self.gender))

    #자식 클래스 객체 생성
 chil = Children("이순신", "해군 장군", "남자")
 chil.display()
