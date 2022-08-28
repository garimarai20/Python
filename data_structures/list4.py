# APPEND FUNCTION
fruits=[]
fruits.append("apple")
fruits.append("banana")
fruits.append("cherry")
fruits.append("guava")
fruits 

fruits.insert(1,"orange")
print(fruits)

dry_fruits=['almonds','cashew','walnut']
fruits.extend(dry_fruits)
print(fruits)

# POSITIVE ALPHABETICAL SORT
fruits.sort()
print(fruits)

# REVERSE ALPHABETICAL SORT
fruits.sort(reverse=True)
print(fruits)

# remove function
fruits.remove("cherry")
print(fruits)

# COPY FUNCTION 
val=fruits.copy()
val.append('litchi')
print(val)
print(fruits)

# POP FUNCTION
fruits=['apple', 'banana', 'guava', 'almonds', 'cashew', 'walnut']
# BY LIST.POP() METHOD
v= fruits.pop()
print(v)

# BY list.pop(idx) METHOD
v=fruits.pop(2)
print(v)

#CLEAR FUNCTION
fruits.clear()
print(fruits)