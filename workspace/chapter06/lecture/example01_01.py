class Rectangle:
    w = h = 0

    def __init__(self, width, height):
        self.w = width
        self.h = height

    def area_calc(self):
         return self.w * self.h

    def circum_calc(self):
        return (self.w + self.h) * 2



print("사각형의 넓이와 둘레를 계산합니다.")
w =  int(input('사각형의 가로 입력 : '))
h =  int(input('사각형의 세로 입력 : '))

rec = Rectangle(w,h)

area = rec.area_calc()
print('사각형의 넓이 : %d' % area)
circum = rec.circum_calc()
print('사각형의 둘레 : %d' % circum)
