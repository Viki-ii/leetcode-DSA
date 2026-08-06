class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        BUY = 0
        SELL = 1
        dp = []

        for i in range(n):
            dp.append([-1] * 5)

        def f(idx, transactionDone):
            if idx == n or transactionDone == 4 :
                return 0

            if dp[idx][transactionDone] != -1:
                return dp[idx][transactionDone]

            #skip this day
            ans1 = f(idx + 1, transactionDone)

            if transactionDone % 2 == 0:
                ans2 = -prices[idx] + f(idx +1,transactionDone + 1)
            else: 
                ans2 = prices[idx] + f(idx + 1, transactionDone + 1)

            dp[idx][transactionDone] = max(ans1, ans2)

            return dp[idx][transactionDone]
        return f(0, BUY)

