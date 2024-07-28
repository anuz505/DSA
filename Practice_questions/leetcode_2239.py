#find the closest number to zero.
def CNZ(nums):
    temp = nums[0]
    for num in nums:
        if(abs(num)<abs(temp)):
            temp = num
        elif(abs(num) == abs(temp)):
            temp = max(num,temp)
    return temp

nums = [-4,-2,1,4,8]
result = CNZ(nums)
print(result)