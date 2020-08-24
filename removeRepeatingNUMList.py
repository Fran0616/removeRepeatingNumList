#Goal is to write a program to remove all the repeting numbers in the myList variable.
myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newList =[]
for i in myList: 
    if i not in newList:
        newList.append(i)
print (newList)
