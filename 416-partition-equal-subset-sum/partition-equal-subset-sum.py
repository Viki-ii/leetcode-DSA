
def f(arr, target, idx, curSum, dp):
    if curSum > target:
        return False
    if idx >= len(arr):
        return curSum == target
    if dp[idx][curSum] != -1:
        return dp[idx][curSum]

    ans1 = f(arr, target, idx + 1, curSum + arr[idx],dp)
    ans2 = f(arr,target, idx + 1, curSum, dp)
    dp[idx][curSum] = ans1 or ans2

    return dp[idx][curSum]

class Solution:
    def isSubsetSum(self, arr, target):
        n = len(arr)
        dp = []
        for i in range(n):
            dp.append([-1] * (target +1))
        return f(arr, target, 0 , 0 ,dp)
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = 0
        for i in range(len(nums)):
            totalSum += nums[i]
        if totalSum % 2 == 1:
            return False
        return self.isSubsetSum(nums, totalSum // 2)
        