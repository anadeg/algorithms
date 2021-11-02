def fib_closure():
    x1, x2 = 0, 1

    def fib_inner():
        nonlocal x1, x2
        x1, x2 = x2, x1 + x2
        return x2

    return fib_inner


n = int(input("enter number -- "))
num = 0

f = fib_closure()
for i in range(2, n + 1):
    num = f()

print(num)
