"""
get number as sum of different components
for example 8 = 1 + 2 + 5, 13 = 1 + 2 + 3 + 7
"""

number = int(input())
# for example n = 8
def different_components(n):
    num = n
    res = []
    # try to add 1 + 2 + 3 + 4 + ... while it's less then num
    for i in range(1, n + 1):
        num -= i
        if num >= (i + 1):
            res.append(i)
            # first step:
            # num -= 1 (num = 8 - 1= 7)
            # 7 > 2(i + 1) ---> res = [1]

            # second step:
            # num -= i (num = 7 - 2 = 5)
            # 5 > 3(i + 1) ---> res = [1, 2]
        else:
            res.append(num + i)
            break
            # third step:
            # num -= 1 (num = 5 - 3 = 2)
            # 2 < 4(i + 1) ---> we put 5 (num before iteration) in list
            # because 2 is already in res
            # otherwise we will get [1, 2, 3, 2]
            # res = [1, 2, 5]
    return res


print(len(different_components(number)))
print(*(different_components(number)))
