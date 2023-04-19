# (1) 함수정의
def calc_func(a, b) :
    x = a #전영 변수
    y = b #전영 변수

    def plus() :
        p = x + y
        return p

    def minus():
        m = x - y
        return m
    return plus, minus

# (2) 함수 호출
p, m = calc_func(10, 20)
print('plus =', p())
print('minus =', m())

# (3) 클래스 정의
class calc_calss :
    x = y = 0

    def __init__(self, a, b):
    self.x = a
    self.y = b

    def plus(self):
        p = self.x + self.y
        return p


    def minus(self):
        m = self.x - self.y
        return m

# (4) 객체 생성
obj = clac_calss(10, 20)

# (5) 멤버 호출
print('plus = ' , obj.plus())
print('minus = ' , obj.minus())


class Car:
    cc = 0
    door = 0
    carType = None

    def __init__(self, cc, door, carType):
        self.cc = cc
        self.door = door
        self.carType = carType

    def display(self):
        print("자동차는 %d cc이고, 문짝은 %d개, 타입은 %s" %(self.cc, self.door, self.carType))


car1 = Car(2000, 4, "승용차")
car2 = Car(3000, 5, "SUV")

car1.display()
car2.display()

#6.2.3

class multiply :
    x = y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mul(self):
        return self.x * self.y

obj = multiply(10, 20)
print('곱셈=', obj.mul())

# (2) 메서드 이용 멤버변수 초기화
class multiply2:
    x = y = 0

    def __init__(self):
        pass

    def data(self, x, y):
        self.x= x
        self.y= y

    def mul(self):
        return self.x * self.y

obj = multiply2()
obj.data(10, 20)
print('곱셈 =', obj.mul())


# 6.2.4

class multiply3:

    def data(self,x , y):
        self.x= x
        self.y= y

    def mul(self):
        result = self.x * self.y
        self.display(result) #괄호가 있기 때문에 메서드 임

    def display(self, result):
        print("곱셈 = %d" %(result))

obj = multiply3() # 기본 생성자
obj.data(10, 20)
obj.mul()


# 6.2.5

class DatePro :
    content = "날짜 처리 클래스"

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def display(self):
        print("%d-%d-%d" %(self.year, self.month, self.day))

    #클래스 메서드(class method)  객체 생성을 안하고 바로 쓸 수 있음
    @classmethod
    def date_string(cls, dataStr) : # '19951025'
        year = dataStr[:4]
        month = dataStr[4:6]
        day = dataStr[6:]

        print(f"{year}년 {month}월 {day}일")

date = DatePro(1995, 10, 25)
print(date.content)
print(date.year)
date.display()

# 클래스 멤버
print(DatePro.content)
#print (DatePro.year)
DatePro.date_string('19951025')

# 6.3.1

class Account:
    __balance = 0
    __accName = None
    __accNo = None

    def __init__(self, bal, name, no):
        self.__balance = bal
        self.__accName = name
        self.__accNo = no
# 계좌 정보 확인( Getter)
    def getBalance(self):
        return self.__balance, self.__accName, self.__accNo

    def deposit(self, money):
        if money < 0:
            print('금액 확인')
            return
         self.__balance += money

     def withdraw(self, money):
        if self.__balance < money:
            print('잔액 부족')
            return
         self.__balance =- money

acc = Account(1000, '홍길동', '125-152-4125-41')

# acc.__balance #은닉 정보로 객체가 접근 불가함
bal = acc.getBalance()
print('계좌정보 : ', bal)

acc.deposit(10000)
bal = acc.getBalance()
print('계좌정보 : ', bal)

#6.3.2

#부모 클래스
class Super:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#매서드
    def display(self):
        print('name : %s, age : %d' %(self.name, self.age))

sup = Super('부모', 55) #객체 생성
sup.display() #부모멤버 호출

# 자식 클래스
class Sub(super) : #클래스 상속
    gender = None # 자식멤버

    #생성자
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    #메서드 확장(재정의)
    def display(self):
        print('name : %s, age : %d, gender: %s' %  (self.name, self.age, self.gender))

sub = Sub('자식', 25 , '여자')
sub.display() # 자식 멤버호출



