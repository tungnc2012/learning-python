##Caculate the sum of the Fibonaccy number

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibo(n-2) + fibo(n-1)

number_to_caculate = int(input("Enter Fibonacci number you want to caculate:"))
print(fibo(number_to_caculate))