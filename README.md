# removeRepeatingNumList
Goal is to write a program to remove all the repeting numbers in the myList variable. The code will store the numbers in a new list. A for loop is used append the numbers in the list. The **not in** operator is used to prevent adding repeated number from the list. 

The in and not in operators

1. The in checks if a given element is currently stored somewhere inside the list - the operator returns TRUE in this case
2. The not in checks if a given element is absent in a list - the operator returns TRUE in this case

[Code:](https://github.com/Fran0616/removeRepeatingNumList/blob/master/removeRepeatingNUMList.py)
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
