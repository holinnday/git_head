class Employee:
    name = None
    pay = 0

    def __init__(self, name):
        self.name = name

    def pay_calc(self):
        pass

class Permanent(Employee):
    def __init__(self, name):
        super().__init__(name)


    def pay_calc(self, base, bonus):
        self.pay = base + bonus


class Temporary(Employee):
    def __init__(self, name):
        super().__init__(name)
    print("고용 형태 : 임시직")
    print("이름 : %s" % self.name)

    def pay_calc(self, tpay, time):
        self.pay = tpay + time
        print('급여 : ', format(self.pay, '3,d'), '원')

status = int(input("고용형태 선택(정규직<P>, 임시직<T>): "))

if status == 'P':
    name = input("이름 : ")
    base = int(input("기본급 : "))
    bonus = int(input("상여금 : "))
    emp1 = Permanent(name)
    emp1.pay_calc(base, bonus)
    print("고용 형태 : 정규직")
    print("이름 : %s" % self.name)
    print('급여 : ', format(self.pay, '3,d'), '원')
    

