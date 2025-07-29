arr = [5, 3, 1, 6, 7, 8, 10, 2, 1]
target = 8
arr_length = len(arr)

print(arr_length)

i = 0

for x in range(0, arr_length+1):
    if x == target:
        print("found")
    else:
        i+=1

print(i)
