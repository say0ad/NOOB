# today we will start from: Set
thisset = {"apple", "banana", "cherry"}
print(thisset)
# Now we will print Orderd set, without duplicate value:
thisset = {"apple", "Samsung", "xioami", "alu","alu"}
print(thisset)
#Printing various typof value in set:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 17, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)
# A set with strings, integers and boolean values:
set1 = {"abc", 34, True, 40, "male"}
print(set1)
# Printing The type:
myset = {"apple", "banana", "cherry"}
print(type(myset))
# The set constructor:
thisset = set(("apple", "banana", "cherry"))
print("The set will print randomly.")
print(thisset) # Note: the set list is unordered, so the result will display the items in a random order.
#Access Set item:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
#checking if banana is in set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
#Adding new item:
thisset = {"apple", "banana", "cherry"}
print("Adding 'Orange' to the list.")
thisset.add("orange")
print(thisset)
#Updating new data to the set:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
#Removing Spacific data:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#Remove random item from list:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #the set after removal
#Join set1 and set2 into a new set:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
#Joining The Two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)
#Useing | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)
#Using & to join 2 set:
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)
#if Statement:
a = 33
b = 200

if b > a:
  print("b is greater than a")
#else kyeword:
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#Multiple statemant in one line:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
# Test if a is greater then b, AND if c is greater then a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
#The OR kyeword is a logicla operatior, and is used to combind conditional statement:
a = 200
b = 33
c = 500
if a > b or a > c:
   print("At least one of the conditions is True")
#while loop we can exicute a set of long as a conditonal is true:
i = 1
while i < 6:
  print(i)
  i += 1
print("New Loop")
#i will stop in the value of 3.
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1
# Print a messahe once the conditon is false:
print("New Loop")
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
#Loop through the letters "banana":
print("New Banana Loop")
for x in "banana":
  print(x) 

#Exit when the loop is 'Banana'
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break
# Dont print Banana:
print("New Loop:\nDont print Banana:")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 
# Nested loop. Print each adjective for even fruit:
print("\nNew Topic:")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
