# Best Case: In the best case, the key might be present at the first index. So the best case complexity is O(1)
# Worst Case: In the worst case, the key might be present at the last index i.e., opposite to the end from which the search has started in the list. So the worst-case complexity is O(N) where N is the size of the list.
# Average Case: O(N)
def search (arr,N,x):
    for i in range(0 , N):
        if arr[i] == x:
            return i
    return -1

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    N = len(arr)
    x = 3

    result = search(arr,N,x)
    if result == -1:
        print("The value is not present in the array")
    else:
        print(f"The value is in index {result}")

