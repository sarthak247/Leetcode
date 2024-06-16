class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} #value:index
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [i, hashmap[diff]]
            else:
                hashmap[num] = i
        
# Link: https://leetcode.com/problems/two-sum/