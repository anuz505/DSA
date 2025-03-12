def count_sort(arr:list)->list[int]:
    max_val = max(arr)
    n = len(arr)
    count = [0] * (max_val +1)

    for x in arr:
        count[x]+=1
    i = 0
    for c in range(max_val+1):
        while count[c]>0:
            arr[i] = c
            i += 1
            count[c] -= 1
    return arr

Arr = [12, 4, 6, 2]
Arr = count_sort(Arr)
print(Arr)