class Dp(object):
    """dp[i] is going to store maximum value with knapsack capacity i"""
    dp = []
    choice = []
    def __init__(self, size):
        self.size = size
        self.dp = [0 for i in range(size)]
        self.choice = [[] for i in range(size)]
