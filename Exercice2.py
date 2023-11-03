def maxProfit(prix):
    max_profit = 0
    for i in range(len(prix)):
        for j in range(i + 1, len(prix)):
            profit = prix[j] - prix[i]
            if profit > max_profit :
                max_profit = profit
    return max_profit

