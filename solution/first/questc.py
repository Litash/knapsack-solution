import json
from solution.utils import stock
from solution.utils import dpstruct


def calculateProfit(stocksList, capital):
    dp = unboundedKnapsack(stocksList, capital)
    return (dp.dp[capital], dp.choice[capital])


def unboundedKnapsack(stocksList, capital):
    """
    Find maximum achievable value with a knapsack of weight W
    and multiple instances allowed.
    Returns the maximum value with knapsack of W capacity
    """
    d = dpstruct.Dp(capital + 1)
    # Fill dp[] using above recursive formula
    for i in range(capital +1):
        for j in range(len(stocksList)):
            if (stocksList[j].price <= i):
                # dp[i] = max(dp[i], dp[i-stockList[j].price] + stocksList[j].earn)
                if d.dp[i] < d.dp[i - stocksList[j].price] + stocksList[j].earn:
                    d.dp[i] = d.dp[i - stocksList[j].price] + stocksList[j].earn
                d.choice[i] = d.choice[i - stocksList[j].price][:]
                d.choice[i].append(stocksList[j].stockName)
                d.choice[i].sort()
    return d


def createStockList(filename):
    testData = json.load(open(filename))
    capital = testData["startingCapital"]
    stocksList = []
    for s in testData["stocks"]:
        stocksList.append(stock.Stock(s[0], s[2], s[1]))

    return (stocksList, capital)