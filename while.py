# num = 1
# while num <=10:
#     if num % 2 == 0:
#         print("print even",num)
#         num = num+1
#     else:
#         num = num+1

n = int(input("enter the number"))
rev = 0
w = n
r = 0
while n != 0:
    r = n%10
    rev = rev*10+r
    n = int(n/10)
    print("the rev no is"121,rev)
if n == w:
    print("not palindrome")
else:
    print(" palindrome")
