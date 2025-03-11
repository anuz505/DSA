def merge_sort(arr:list):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2

    left_half =merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half,right_half)

def merge(left:list,right:list) -> list:
    i = j = 0
    sorted_arr = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

Arr = [12, 4, 6, 2]
Arr = merge_sort(Arr)
print(Arr)