class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0] # Initial subarray
        curSum = 0 # Initial sum

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum) # update maximum sum
        return maxSub

# Link: https://leetcode.com/problems/maximum-subarray/