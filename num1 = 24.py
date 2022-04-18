num1 = 24
if num2 = 48
pf = []
def getprimefactor(num1)
while num1 % 2 == 0:
    pf.append(2)
    num1 //= 2

    print(pf)
    print(num1)
    for i in range(3,num1,2):
        if num1%i == 0:
            pf.append(i)
            num1// = i

     print(pf)
    print(num1)

    return pf
    def computeLcm(fact1,fact2)

    num1 = 24
    num = 48

    pfnum1 = getprimefactors(num1)
    pfnum2 = getprimefactors(num2)