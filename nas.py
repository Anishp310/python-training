num1 = 10
num2 = int(input("enter a nummber"))
quot = 0
try:
    quot = num1/num2
except Exception:
    print("error divisible by 0")
else:
    print("inside this block")
finally:
    print("inside finally block")
print("your result is")
print(quot)
list ko subset nikalne
 