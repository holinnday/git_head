# (1)  재귀함수 정의 : 1-n 누적합 (1+2+3+4+5=15)
def Adder (n) :
    if n == 1 :
        return 1
    else :
        result  =  n + Adder(n-1)

        print (n, end =  ' ')
        return result

    print ('n=1', Adder(1))  n=1 : 1
    print ('\nn=5:1'Adder(5))  n=5 : 15