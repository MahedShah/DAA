def selectionSort(arr):
    for i in range(len(arr)):
        smallest = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i] , arr[smallest] = arr[smallest], arr[i]  
    return arr



a = [9,8,3,5,1,12,9,24]
print(selectionSort(a))
