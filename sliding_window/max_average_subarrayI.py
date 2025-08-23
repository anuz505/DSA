class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        current_sum = 0
        
        for i in range(k):
            current_sum += nums[i]

        max_avg = current_sum / k

        for i in range(k,n):
            current_sum += nums[i]        # This line was correct
            current_sum -= nums[i - k]    # This line was correct
        
            avg = current_sum / k
            max_avg = max(max_avg,avg)
        return max_avg
    
if __name__ == "__main__":
    nums = [1,12,-5,-6,50,3]
    k = 4
    sol = Solution()
    print(sol.findMaxAverage(nums, k))