def twosum(nums, target):
    hasmap = {}
    for i in range(len(nums)):
        hasmap[nums[i]] = i
    for i in range(len(nums)):
        temp = target - nums[i]
        if temp in hasmap and hasmap[temp] != i:
            return [i, hasmap[temp]]
    return []

# two pointers method (requires sorted array)
def twosum_pointers(nums,target):
    n = len(nums)
    l = 0
    r = n-1 

    while l < r:
        sum = nums[l] + nums[r]
        if sum == target:
            return [l+1, r+1]
        elif sum > target:
            r-=1  # Move right pointer left to decrease sum
        else:
            l+=1  # Move left pointer right to increase sum
    
    
        



if __name__ =="__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(twosum(nums, target) )
    print(twosum_pointers(nums,target))