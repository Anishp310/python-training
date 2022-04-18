
num = int(input("enter a num"))
m= len(str(num))
sum=0
temp = num
while num!=0:
    digit = int(num % 10)
    sum = sum + digit**m
    print(sum)
    num = num//10
if temp == sum:
    print(temp,"is amstrong")
else:
    print(temp,"is not amstrong")