class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] # Output array
        nums.sort() # Sort (To eliminate duplicates)

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]: # we do not want to keep on same A
                continue        
            
            l, r = i + 1, len(nums) - 1
            while(l < r):
                threesum = a + nums[l] + nums[r]

                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1 # move pointer forward
                    while(nums[l] == nums[l-1] and l < r): # make sure not same number
                        l += 1
        return res

# Link: https://leetcode.com/problems/3sum/
