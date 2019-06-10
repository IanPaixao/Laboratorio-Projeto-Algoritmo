while input() != "":
 days = int(input())
 daycost = int(input())
 week = []
 profit = []
 for i in range(days):
  week.append(int(input()))
  highest = max(week)
  profit.append(max(highest,daycost))
  profit.remove(daycost)
print((profit[0] + profit[len(profit)-1] + days) - (3 * daycost))

    