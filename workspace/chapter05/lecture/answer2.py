def bank_account(bal):
    balance = bal

    def getBalance():
        return balance

    def deposit(money):
        nonlocal balance
        balance += money

    def withdraw(money):
        nonlocal balance
        balance -= money

    return getBalance, deposit, withdraw

bal = int(input('최초 계좌의 잔액을 입력하세요 : '))
getBalance, deposit, withdraw = bank_account(bal)
print('현재 계좌 잔액은 ' + str(getBalance()) + '원 입니다.')

bal = int(input('입금액을 입력하세요 :'))
deposit(bal)
print(str(bal) + '원 입금후 잔액은 ' + str(getBalance()) + '원 입니다.')

bal = int(input('출금액을 입력하세요 :'))
withdraw(bal)
print(str(bal) + '원 출금후 잔액은 ' + str(getBalance()) + '원 입니다.')




