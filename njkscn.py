from operator import truediv


a=[1,2,2,3,4,5]
b=[1,2,3]
c=[1,2,6]
sub=True
for i in b:
    if i in a:
        sub=True
    else:
        sub=False
print(sub)
for i in c:
    if i in a:
        sub=True
    else:
        sub=false