"""
get change with smaller amount of coins
for example 34 = 25 * 1 + 10 * 0 + 5 * 1 + 1 * 4 (6 coins)
"""

# get 17 for example
change = int(input("enter amount of cents --- "))
coins = [25, 10, 5, 1]
res = [0, 0, 0, 0]

for i in range(len(coins)):
    if change // coins[i] == 0:
        continue
        # first step:
        # 17 // 25 = 0 ---> we don't get 25-cents coins
    else:
        res[i] = change // coins[i]
        change -= res[i] * coins[i]
    # second step:
    # 25 // 15 = 1 ---> we have one 10-cents coin
    # change -= 1 * 10 (change = 7)

    # third step:
    # 7 // 5 = 1 ---> we have one 5-cents coin
    # change -= 1 * 5 (change = 2)

    # fourth step:
    # 2 // 1 = 2 ---> we have two 1-cent coins
    # change -= 2 * 1 (change = 0)

all_coins = 0
for amount, coin in zip(res, coins):
    print(f"you get {amount} of {coin} cents")
    all_coins += amount

print(f"amount of coins --- {all_coins}")




