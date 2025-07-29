list_1 = [1, 2, 45.3, 45, 'ajf']

print(list_1)

my_list = [1, 2, 4]

# add element to the end.
my_list.append(3)
print(f"Added 3 at the end: {my_list}")

# Extend the list by appending all the items from the iterable.
my_list.extend([6, 7, 8])
print(f"Extended list by [6, 7, 8]:{my_list}")

# insert at specific location.
my_list.insert(2, 3)
print(f"Inserted 3 at index 2: {my_list}")

# Remove first occurance of the element from the list.
my_list.remove(3)
print(f"Removed first occurance of 3 from the list: {my_list}")

# Remove element from the specific position.
my_list.pop(2)
print(f"Removed element from index 2: {my_list}")

# Returns the first occurance index of the element specified in it.
index_ele = my_list.index(3)
print(f"List element specified for index: {index_ele}")

my_list.extend([5, 6, 2, 3, 1, 3, 6, 3])
# count the number of occurance the element in the list.
print(f"Count of 3: {my_list.count(3)}")

another_copy = my_list.copy()
print(f"Another copy is: {another_copy}")

my_list.sort()
print(f"Sorted array: {my_list}")

my_list.sort(reverse=True)
print(f"Sorted array in reverse: {my_list}")

my_list.reverse()
print(f"Sorted array using reverse: {my_list}")

my_list.clear()
print(f"empty array: {my_list}")

# List comprehension.
print("List Comprehension")
# a_list = []

# for i in range(0, 10):
#     a_list.append(i**2)

# print(a_list)

a_list = [x**2 for x in range(0, 10)]
print(a_list)

b_list = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            b_list.append((x, y))
print(b_list)

b_list = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(b_list)