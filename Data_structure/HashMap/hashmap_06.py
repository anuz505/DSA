## majority element
class Solution:
    def majorityElement(self,nums):
        hashmap = {}
        n = len(nums)
        for i in range(n):
            hashmap[nums[i]] = hashmap.get(nums[i],0) + 1 

        for num, count in hashmap.items():
            if count > n // 2:
                return num
    
if __name__ == "__main__":
    S = Solution()
    nums= [3,2,3]
    res = S.majorityElement(nums=nums)
    print(res)