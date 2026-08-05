def f(nums, idx, dp):
    if idx >= len(nums):
        return 0
    if dp[idx] != -1:
        return dp[idx]
    
    ans1 = nums[idx] + f(nums, idx+2, dp)

    ans2 = f(nums, idx + 1, dp)

    dp[idx] = max(ans1, ans2)
    return dp[idx]
class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = [-1] * len(nums)
        return f(nums, 0 , dp)
        