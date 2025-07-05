from typing import List
class Solution:
    def searchInsert(self,nums:List[int], target):
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            m = (l + r ) // 2

            if nums[m] < target:
                l = m + 1

            if nums[m] > target:
                r = m - 1
            
            else: 
                return m
        
        if nums[m] < target:
            return m + 1
        
        else:
            return m