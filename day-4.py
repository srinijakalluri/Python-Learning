#creating and printing a list
fruits = ['apple', 'mango', 'grapes']
print(fruits)

#adding elements to a list
fruits.append('cherry')
print(fruits)
fruits.insert(1,'kiwi')
print(fruits)

#length of the list
print(len(fruits))

#replacing an element
fruits[1]= 'banana'
print(fruits)

#deleting elements from a list
fruits.pop(1)
print(fruits)
fruits.remove('cherry')
print(fruits)

fruits.append('cherry')
fruits.append('banana')
fruits.append('kiwi')
print(fruits)

#organising a list
fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

#fetching an element from a list
print(fruits[5])
print(fruits[-1])

#slicing of a list
print(fruits[2:5])

#for loop
print("fruits are :")
for x in fruits :
    print(x)

#copying a list
a = fruits[ : ]
b = fruits.copy()
print(a)
print(b)