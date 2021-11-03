"""
knapsack problem
fill a fixed-size bag with the most valuable items
we can divide all objects, the price is proportional to weight
"""

lst_of_lst = []
# get amount of elements and bag capacity. for example 3 and 10
n, all_weight = map(int, input().split())
for i in range(n):
    # get list [price, kg] like [[30, 5], [120, 6], [45, 5]]
    all_price__weight = list(map(float, input().split()))
    # now we get [price per kg, rg]: [6, 5], [20, 6], [9, 5]
    price_weight = [all_price__weight[0] / all_price__weight[1], all_price__weight[1]]
    lst_of_lst.append(price_weight)


def stole(lst):
    res = 0    # max price
    # sort in ascending order: [[20, 6], [9, 5], [6, 5]]
    lst.sort(reverse=True)
    global all_weight
    for obj in lst:
        # first step: 6 < 11 ---> res += 20 * 6 (res = 120)
        # all_weight -= 6 (all_weight = 4)
        if obj[1] <= all_weight:
            res += obj[0] * obj[1]
            all_weight -= obj[1]
        # second step: 5 > 4 ---> res += 9 * 4
        # (we cannot take 5kg because we have only 4kg free space),
        # (res = 120 + 36 = 156)
        # all all_weight is used
        # bag is filled
        else:
            res += all_weight * obj[0]
            break
    return f"{res:.3f}"


print(stole(lst_of_lst))
