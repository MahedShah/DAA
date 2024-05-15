def merge(left, right):
 
  merged = []
  i, j = 0, 0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1
  # Append remaining elements from whichever list has them
  merged += left[i:]
  merged += right[j:]
  return merged

def merge_sort(data):
  
  if len(data) <= 1:
    return data
 
  mid = len(data) // 2
  left = merge_sort(data[:mid])
  right = merge_sort(data[mid:])
 
  return merge(left, right)

data = [6, 5, 3, 1, 8, 7, 2, 4]
sorted_data = merge_sort(data)

print("Original data:", data)
print("Sorted data:", sorted_data)
