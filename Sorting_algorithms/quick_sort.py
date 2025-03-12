def quick_sort(arr:list):
    if len(arr) <=1:
        return arr
    n = len(arr)
    piviot = arr[-1]

    L = [x for x in arr[:-1] if x <= piviot]
    R = [x for x in arr[:-1] if x > piviot]

    L = quick_sort(L)
    R = quick_sort(R)

    return L + [piviot] + R

Arr = [12, 4, 6, 2]
Arr = quick_sort(Arr)
print(Arr)