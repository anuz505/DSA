def binary_search(Arr,low,high,x):

    if(low<=high):
        mid = low + (high - low) // 2

        if(Arr[mid] == x):
            return mid
        
        elif(x < Arr[mid]):
            return binary_search(Arr,low,mid - 1,x)
        
        else:
            return binary_search(Arr,mid + 1, high , x)
            
    return -1

if __name__ == "__main__":
    Arr = [1,2,3,4,5,6,7,8,9,10]
    x = 3

    result =  binary_search(Arr,0,len(Arr)-1 , x)
    
    if(result != -1):
        print(f"The element {Arr[result]} is in index {result}")
    else:
        print("The array does not contain the element")
        
        