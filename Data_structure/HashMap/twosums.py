def twosum(nums, target):
    hasmap = {}
    for i in range(len(nums)):
        hasmap[nums[i]] = i
    for i in range(len(nums)):
        temp = target - nums[i]
        if temp in hasmap and hasmap[temp] != nums[i]:
            return [i, hasmap[temp]]
    return []
if __name__ =="__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(twosum(nums, target) )