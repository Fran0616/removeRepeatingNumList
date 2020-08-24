# removeRepeatingNumList
Goal is to write a program to remove all the repeting numbers in the myList variable. The code will store the numbers in a new list. A for methos is used append the numbers in lhe list. The not in operator is used to prevent adding repeated number from the list. 

[Code:]()
=

```
#Goal is to write a program to remove all the repeting numbers in the myList variable.
myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newList =[]
for i in myList: 
    if i not in newList:
        newList.append(i)
print (newList)

```

Output: 
=

```
[1, 2, 4, 6, 9]
```
