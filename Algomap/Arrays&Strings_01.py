from typing import List

class Solution:
    def findClosestNumber(self,nums):
        num = float('inf')
        for i in nums:
            a = abs(num)
            if abs(i) < a:
                num = i
            elif abs(i) == a:
                if i > num:
                    num = i
        return num
    
if __name__ == '__main__':
    s = Solution()
    print(s.findClosestNumber([1,-1,3,4,-2]))