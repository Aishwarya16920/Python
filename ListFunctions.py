friends = ["Kevin", "Karen", "Jim", "Jim", "Jim", "Jim", "Oscar", "Toby"]
lucky_numbers = [4, 8, 15, 16, 42, 23]
friends2 = friends.copy()

print(friends2)

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends.extend(lucky_numbers)
print(friends)

friends.append("Creed")
print(friends)

friends.insert(1, "Kelly")
print(friends)

friends.remove("Jim")
print(friends)

friends.pop()
print(friends)

print(friends.index("Kevin"))

print(friends.count("Jim"))

friends.clear()
print(friends)
