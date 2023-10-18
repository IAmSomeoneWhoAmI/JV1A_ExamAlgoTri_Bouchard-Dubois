#Ex 2

myTable = [5,4,3,1,2]
taille = len(myTable)
stock = [0]

for i in range (taille):
    if myTable [0]> myTable[i]:
        taille[i] += 1
    else :
        stock = taille

stock = myTable[4]
myTable[4] = taille

print(myTable)



