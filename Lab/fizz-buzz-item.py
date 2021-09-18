# for value in range(100):
#     if value % 5 == 0 and value % 3 == 0:
#         print("FizzBuzz")
#         continue
#     elif value % 3 == 0:
#         print("Fizz")
#         continue
#     elif value % 5 == 0:
#         print("Buzz")
#     else:
#         print(value)

input_number = int(input("Enter the value you want to process:"))

for number in range(1, input_number + 1):
    if number % 3 == 0 and  number %5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

    

