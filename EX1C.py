from itertools import combinations
lst=[2,-3,6,-7]
print("Possitive nambers are")
for i in range(1,len(lst)+1):
    for combo in combinations(lst,i):
        if all(num>0 for num in combo):
            print(combo)
