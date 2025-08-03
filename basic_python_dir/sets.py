# Sets: Unordered collection of unique elements.
# Uses: For removing duplicates and performing mathematical operations such as Union, Insertion, and Difference.
# Difference: Sets are unordered and do not index elements.

fruits = {"Apple", "Banana", "Cherry"}

# Adding
fruits.add("Orange") # Add single element.
fruits.update(["Mango", "Jackfruit"]) # Add multiple items.

# Removing
fruits.remove("Banana") # Raise error if not exists.
popped_fruit = fruits.pop() # Removes and returns an arbitrary element
print("Popped fruit: ", popped_fruit)
fruits.discard("Banana") # No error if element doesn't exist
fruits.clear()
print("Sets: ", fruits)

# Mathemeatical Set operations.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set = set1.union(set2)
print("Union set: ", union_set)

intersction_set = set1.intersection(set2)
print(intersction_set)

difference_set = set1.difference(set2)
print("Difference: ", difference_set)

# Symmetric difference (elements in either set, but not in both)
symmetric_set = set1.symmetric_difference(set2)
print("Symmetric Difference: ", symmetric_set)


# Set Comphrension
squares = {x**2 for x in range(10)}
print(squares)

# Even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_num = {x for x  in numbers if x % 2 == 0}
print(even_num)

list_with_duplicates = [3, 1, 2, 6, 2, 5, 8, 9, 1, 2, 6, 10, 8, 9, 2]
removed_duplicates = list(set(list_with_duplicates))
print(removed_duplicates)

# Frozen sets: Immutable sets.
frozen = frozenset([2, 4, 6, 7])
frozen.add(3) # Raise error

# Use sets when order doesn’t matter, but uniqueness does
# Prefer sets over lists for membership testing with large collections
# Use frozen sets when you need an immutable set (like dictionary keys)
# Remember that sets can only contain hashable elements