file = open("Random.txt", "r")
# print(employee_file.readable())
# print(employee_file.read())
# print(employee_file.readline())
# print(employee_file.readline())
# print(employee_file.readlines())
# print(employee_file.readlines()[1])
for text in file.readlines():
    print(text)
file.close()