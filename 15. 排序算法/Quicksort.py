def quick_sort(arr):
    if not arr or len(arr) == 1:
        return arr
    quickSort(arr, s=0, e=len(arr)-1)
    return arr

def quickSort(arr, s, e):
    if s >= e:
        return
    else:
        m = partition(arr, s, e)
        quickSort(arr, s, m-1)
        quickSort(arr, m+1, e)

def partition(arr, s, e):
    if s >= e:
        return s
    pivot = arr[e]
    i = s
    for j in range(s, e):
        if arr[j] <= pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[e], arr[i] = arr[i], arr[e]
    return i
m = partition([4,1,2,3,4,-16], 0, 5)

print(quick_sort([4,1,2,3,4,-16]))