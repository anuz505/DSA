class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ans = []
        i = 0

        while i<len(nums):
            start = nums[i]
            while i<len(nums)-1 and nums[i]+1 == nums[i+1]:
                i += 1
            if start != nums[i]:
                ans.append(str(start) + "->" + str(nums[i]))
            else:
                ans.append(str(start))
            i += 1
        
        return ans
    
if __name__ == '__main__':
    s = Solution()
    print(s.summaryRanges([0,1,2,4,5,7])) # ["0->2","4->5","7"]
    print(s.summaryRanges([0,2,3,4,6,8,9])) # ["0","2->4","6","8->9"]
    print(s.summaryRanges([])) # []
    print(s.summaryRanges([-1])) # ["-1"]
    print(s.summaryRanges([0])) # ["0"]