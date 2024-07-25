def bubblesort(Arr):
    n = len(Arr)

    for i in range (n):
        swapped = False

        for j in range (0,n - i - 1):
            if (Arr[j] > Arr [ j + 1]):
                Arr[j], Arr[j+1] = Arr[j + 1], Arr[j]
                swapped  = True
            
        if(swapped == False):
            break

if __name__ == "__main__":
    Arr = [12,4,6,2]

    bubblesort(Arr)

    for i in range(len(Arr)):
        print("%d" % Arr[i], end=" ")
