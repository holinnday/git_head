class Rectangle:
    w = h = 0

    def __init__(self, width, height):
        self.w = width
        self.h = height

    def area_calc(self):
        a = self.w * self.h
        print('사각형의 넓이 : %d' % a)


    def circum_calc(self):
        c = (self.w + self.h) * 2
        print('사각형의 둘레 : %d' % c)


print("사각형의 넓이와 둘레를 계산합니다.")
w =  int(input('사각형의 가로 입력 : '))
h =  int(input('사각형의 세로 입력 : '))

rec = Rectangle(w,h)
rec.area_calc()
rec.circum_calc()