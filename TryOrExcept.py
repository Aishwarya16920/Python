try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print("Divided by Zero")
    print(err)
except ValueError:
    print("Invalid Input")