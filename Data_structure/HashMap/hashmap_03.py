from collections import defaultdict


def duplicate_count(nums: list):
    count_map = defaultdict(int)
    for n in nums:
        count_map[n] += 1
    for value in count_map.values():
        if value >= 2:
            return True
        else:
            return False


def set_duplicate_count(nums: list):
    hashset = set(nums)
    for n in nums:
        if n in hashset:
            return True
        else:
            hashset.add(n)
    return False


if __name__ == "__main__":
    numbers = [2, 14, 18, 22, 22]
    result = duplicate_count(numbers)
    print(result)
