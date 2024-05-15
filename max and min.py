def find_max_min(arr):
    if not arr:
        return None, None

    max_element = arr[0]
    min_element = arr[0]

    for num in arr:
        if num > max_element:
            max_element = num
        elif num < min_element:
            min_element = num

    return max_element, min_element

# Example usage:
numbers = [5, 3, 9, 2, 7, 1]
max_num, min_num = find_max_min(numbers)
print("Maximum number:", max_num)
print("Minimum number:", min_num)
