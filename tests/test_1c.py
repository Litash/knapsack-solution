from solution.first import questc
import pytest

def createStockList(filename):
    testData = json.load(open(filename))
    capital = testData["startingCapital"]
    stocksList = []
    for s in testData["stocks"]:
        stocksList.append(Stock(s[0], s[2], s[1]))

    return (stocksList, capital)


def prettyPortfolio(choices):
    stockDict = dict()
    for stk in choices:
        if stk in stockDict:
            stockDict[stk] += 1
        else:
            stockDict[stk] = 1
    return stockDict


def test_case1():
    (stocksList, capital) = questc.createStockList("tests/testcase_1.json")
    (profit, choices) = questc.calculateProfit(stocksList, capital)
    stockDict = prettyPortfolio(choices)

    assert profit == 52846