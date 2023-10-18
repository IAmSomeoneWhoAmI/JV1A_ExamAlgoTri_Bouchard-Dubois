#Ex 1

myTable = [1,2,3,5,4]
change1 = 0
change2 = 0

print(myTable)

change1 = int(input("quel valeur voulez vous echanger ?\n"))
change2 = int(input("Avec ?\n"))

stock = myTable[change1]
myTable [change1] = myTable[change2]
myTable[change2] = stock

print(myTable)