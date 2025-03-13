# leetcode 771 Jewels and stones
from collections import defaultdict
def numJewelsInStone(jewels:str,stones:str):
    jewel_map = defaultdict(int)
    result = 0
    
    for s in stones:
        jewel_map[s] += 1
    
    for j in jewels:
        result += jewel_map[j]
    
    return result

#brute force o(n)
def newJwewelsInStone(jewels,stones):
    count = 0
    for s in stones:
        if s in jewels:
            count +=1
    return count

#set optimal o(1)
def newJwewlsInStones(jewels:str,stones:str):
    count = 0
    jewels_set = set(jewels)
    for s in stones:
        if s in jewels_set:
            count += 1
    return count
if __name__ == "__main__":
    jewels = "aA"
    stones = "aAAbbbb"
    result = newJwewlsInStones(jewels, stones)
    print(result)  # Output: 3

