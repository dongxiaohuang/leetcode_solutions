def insert_sott(arr):
    if not arr or len(arr)==1:
        return arr
    
    for i in range(1, len(arr)):
        min_idx = i
        min_val = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > min_val:
            arr[j+1] = arr[j]
            min_idx = j
            j -= 1
        arr[min_idx] = min_val
    return arr

print(insert_sott([3,2,1,2,3,4]))