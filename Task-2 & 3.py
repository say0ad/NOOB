#prints from index 2 to 5
b = "0123456789"
print(b[2:5])
#prints last 5
b = "Hello, World!"
print(b[:5])
#prints 2 index and rest off all
b = "Hello, World!"
print(b[2:])

#This will return the items from position 2 to 5.
#Remember that the first item is position 0
#and note that the item in position 6 is NOT included
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:6])
#adding to the list:
thislist = ["apple", "banana", "Sojib_Mumma"]
thislist.append("Jim_mim")
print(thislist)
thislist.insert(1, "Sadia")
print(thislist)
# Now Im going to show you how to input data in another data set:
thislist = ["apple", "banana", "cherry"]
thistuple = ("Kutta", "Bilay","Fuck")
thislist.extend(thistuple)
print(thislist) 
#Let's pop:
thislist = ["Fuck","Suck","apple", "banana", "cherry"]
thislist.pop()
print(thislist)
thislist.pop()
print(thislist)
thislist.pop()
print(thislist)
thislist.pop()
print(thislist)
thislist.pop()
print(thislist)
#Now clear all data:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print("Clraring data")
print(thislist)
#Data Sorting:
thislist = ["Onu", "Meghla", "Kanni", "Payel", "Boby","Anika"]
thislist.sort()
print(thislist)
#Number Sorting:
thislistt = [100, 50, 65, 82, 23]
thislistt.sort()
print(thislistt)
#Desending: Girls
thislist.sort(reverse = True)
print(thislist)
# Tuple using
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuplez
thistuple = ("apple")
print(type(thistuple))
#Few More:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)
#Printing Type:
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#Showing replase the value:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)