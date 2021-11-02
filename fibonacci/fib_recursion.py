def fib_recursion(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_recursion(n - 1) + fib_recursion(n - 2)


num = int(input("enter number -- "))
print(fib_recursion(num))
