for value in range(100):
    if value % 5 == 0 and value % 3 == 0:
        print("FizzBuzz")
        continue
    elif value % 3 == 0:
        print("Fizz")
        continue
    elif value % 5 == 0:
        print("Buzz")
    else:
        print(value)
