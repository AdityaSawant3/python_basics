def sort(arr):
    arr_len = len(arr)

    for i in range(0, arr_len):
        min = i
        for j in range(i+1, arr_len):
            if arr[min] > arr[j]:
                min = j
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp
    return arr


arr = [5, 1, 2, 8, 9, 2, 1]
sorted_arr = sort(arr)

print(sorted_arr)