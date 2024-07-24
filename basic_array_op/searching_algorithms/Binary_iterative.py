def binary_search(Arr,low,high,x):
    while low<=high:
        mid = low + (high - low) //2

        #now we check if the value of mid is equal to x
        if(Arr[mid] == x):
            return mid
        
        # if x is greater than mid value 
        elif(x >Arr[mid]):
            low = mid + 1
        
        # if x is lower than mid value
        else:
            high = mid - 1

    return -1
    
if __name__ == "__main__":
    Arr = [1,2,3,4,5,6,7,8,9,10]
    x = 3

    result =  binary_search(Arr,0,len(Arr)-1 , x)
    
    if(result != -1):
        print(f"The element {Arr[result]} is in index{result}")
    else:
        print("The array does not contain the element")
