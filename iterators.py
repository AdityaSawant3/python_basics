my_list = [1, 2, 3]
my_iterator = iter(my_list)

# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

class MyIterator:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a < 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

my_iter1 = MyIterator()
my_iter = iter(my_iter1)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))