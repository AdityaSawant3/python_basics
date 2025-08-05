def bubble_sort(arr):

    arr_len = len(arr)

    for i in range(arr_len):
        for j in range(arr_len-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

array = [7, 2, 4, 9, 1, 5, 2, 0, 1, 7, 8, 2]

sorted_arr = bubble_sort(array)
print(sorted_arr)