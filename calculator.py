import cmath

print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

n=int(input("choose the option"))

if(n == 1):
    a=int(input("enter first integer"))
    b=int(input("enter second integer"))
    c=( a + b )
    print("sum is",c)
elif(n == 2):
    a=int(input("enter first integer"))
    b=int(input("enter second integer"))
    c= (a - b)
    print("difference is",c)
elif(n == 3):
    a=int(input("enter first integer"))
    b=int(input("enter second integer"))
    c= (a * b)
    print("multiplication is",c)
elif(n == 4):
    a=int(input("enter first integer"))
    b=int(input("enter second integer"))
    c= float(a / b)
    print("division is",c)
else:
    print("invalid choice")



