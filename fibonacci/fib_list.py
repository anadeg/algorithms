fibon = [0, 1]


def fib_table(num):
    if num == 1 or num == 2:
        return fibon[num - 1]
    for i in range(2, num):
        fibon.append(fibon[i - 2] + fibon[i - 1])
    return fibon[num - 1]


n = int(input("enter number -- "))
print(fib_table(n))