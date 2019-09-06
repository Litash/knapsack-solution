from solution.first import questc
import json

if __name__ == '__main__':
    (stocksList, capital) = questc.createStockList("tests/testcase_2.json")
    (profit, choice) = questc.calculateProfit(stocksList, capital)

    stockDict = dict()
    for stk in choice:
        if stk in stockDict:
            stockDict[stk] += 1
        else:
            stockDict[stk] = 1

    ans = {}
    ans["profit"] = profit
    ans["portfolio"] = stockDict
    with open("tests/result/result.json", 'w') as fp:
        jsonAns = json.dump(ans, fp)
        print("Done.")