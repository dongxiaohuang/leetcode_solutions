def merge_sort(arr):
    if not arr or len(arr) == 1:
        return arr
    mergeSort(arr, s=0, e=len(arr)-1)
    return arr

def mergeSort(arr, s, e):
    if s >= e:
        return 
    m = s + (e-s)//2
    mergeSort(arr, s, m)
    mergeSort(arr, m+1, e)
    merge(arr, s, m, e)

def merge(arr, s, m, e):
    i = s
    j = m+1

    new_arr = []
    while i <= m and j <= e:
        if arr[i] < arr[j]:
            new_arr.append(arr[i])
            i += 1
        else:
            new_arr.append(arr[j])
            j+=1
    while i <= m:
        new_arr.append(arr[i])
        i+=1
    while j <= e:
        new_arr.append(arr[j])
        j += 1
    for i in range(len(new_arr)):
        arr[s+i] = new_arr[i]

print(merge_sort([11,2,3,4,5]))