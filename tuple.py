tup = (1,2,3,4,5)
print(type(tup))
print(len(tup))
l1 = list(tup)
print(type(l1)) 
l1.append(6)

tup = tuple(l1)
print(type(tup))
print(tup)

d1 = {}
print(type(d1))
d1 = {
    "id": 10,
    "name": "dipak thapa",
    "roll": 20
}
print(d1["name"])

d1["name"] = "Ramesh"
print(d1)

for elem in d1.name():
    print(elem)

