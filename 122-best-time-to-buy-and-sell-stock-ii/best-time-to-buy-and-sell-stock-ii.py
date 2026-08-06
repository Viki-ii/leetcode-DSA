class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        BUY = 0
        SELL = 1
        dp = []

        for i in range(n):
            dp.append([-1] * 2)

        def f(idx, transactionType):
            if idx == n:
                return 0

            if dp[idx][transactionType] != -1:
                return dp[idx][transactionType]

            #skip this day
            ans1 = f(idx + 1, transactionType)

            if transactionType == BUY:
                ans2 = -prices[idx] + f(idx +1,SELL)
            else: 
                ans2 = prices[idx] + f(idx + 1, BUY)

            dp[idx][transactionType] = max(ans1, ans2)

            return dp[idx][transactionType]
        return f(0, BUY)

