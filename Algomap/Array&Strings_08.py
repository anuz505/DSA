from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output:int = []
        left_product = 1
        right_product =1
        L_array = [0] * length
        R_array = [0] * length

        for i in range(length):
            j = -i-1
            L_array[i] = left_product
            R_array[j] = right_product
            left_product *= nums[i]
            right_product *= nums[j]
            output = [l*r for l,r in zip(L_array,R_array)]
        return output

    

if __name__ == "__main__":
    arr = [1,2,3,4]
    s = Solution()
    output = s.productExceptSelf(arr)
    print(output)
