a = [1, 2, 3]
a.append(7)
print(a)
#append adds an item at the end of the list
a.append("Bob")
print(a)
#string are immutable, lists are a 'container' and you can change what's inside it
a[1] = "Alice"
print(a)

#extend is the same as append but adds another list
a.extend(["James", "Bond"])
print(a)

#pop removes an item from position
a.pop(4)
print(a)

a.remove("Bond")
print(a)

#remove takes away by value
#pop takes away from position
