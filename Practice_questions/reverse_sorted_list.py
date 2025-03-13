def reverse_sorted_array(arr:list[int]):
    new_temp_list = []
    arr = sorted(arr)

    n = len(arr)

    for i in range(n-1,-1,-1):
        new_temp_list.append(arr[i])
    return new_temp_list

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    rev_arr = reverse_sorted_array(arr)
    print(rev_arr)
    