def maxProfit(prix):
    max_profit = 0
    for i in range(len(prix)):
        for j in range(i + 1, len(prix)):
            profit = prix[j] - prix[i]
            if profit > max_profit :
                max_profit = profit
    return max_profit

x= [7,1,5,3,6,4]
y = [7,6,4,3,1]
z = [10,1,7,5,9]

print(maxProfit(x))
print(maxProfit(y))
print(maxProfit(z))