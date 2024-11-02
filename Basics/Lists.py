friends = ["Aranya", "Rakesh", "Arpan", "Ritobhash"]
numbers = [7,4,16,18,15,15]
#friends.extend(numbers)
friends.append("Saturo")
friends.insert(2,"Solo")
friends.remove("Arpan")
friends2= friends.copy()
#friends.clear()
friends.pop()
#numbers.sort()
numbers.reverse()

print(friends)
print(friends2)
print(friends.index("Aranya"))
print(numbers)
#print(friends.count(15))
