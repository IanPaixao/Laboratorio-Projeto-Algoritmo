"""
Greedy algorithm to solve coin collector
"""
n = int(input())
for i in range (n):
    Sum = 0
    input()
    coins = [int(coin) for coin in input().split()]
    ans = 0
    for coin in coins:
        if(coins.index(coin) == (len(coins)-1)) or Sum + coin < coins[coins.index(coin)+1]:
         Sum += coin
         ans+=-1
    print(ans*-1)

