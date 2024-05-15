def partition(arr,si,ei):
    index = si
    for i in range(si,ei):
        if (arr[i] < arr[ei]):
            arr[index], arr[i] = arr[i], arr[index]
            index += 1
    arr[index], arr[ei] = arr[ei], arr[index]
    return index

def quickSort(arr,si,ei):
    if si < ei:
        pivot = partition(arr,si,ei)

        quickSort(arr,si,pivot-1)
        quickSort(arr,pivot+1,ei)



a = [16,2,,7,86,5,11,72,56,65,23]
b = [4,1,6,8,9,3]
quickSort(a,0,len(a)-1)
print(a)
