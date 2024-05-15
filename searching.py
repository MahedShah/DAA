def linear_search(arr, target):
    
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    my_list = [3, 6, 8, 1, 5, 9, 2]
    target_element = 5
    index = linear_search(my_list, target_element)
    if index != -1:
        print(f"Element {target_element} found at index {index}.")
    else:
        print(f"Element {target_element} not found in the list.")
