L = [1, 2, 3, 4]

List = [[]]
for i in range (len(L)):         #  fixed length
    for j in range(len(List)):  #  longer
        sub_List = List[j] + [L[i]]
        if sub_List not in L:
            List.append(sub_List)

print('List =', List)