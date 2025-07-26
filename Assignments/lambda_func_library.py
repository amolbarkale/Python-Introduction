square = lambda x: x**2
print('square:', square(3))

from functools import reduce
arr = [1,2,3,4,5]
sum_of_elements = reduce(lambda x, y: x + y, arr)
print('sum of elements:', sum_of_elements)

reverse = lambda string: string[::-1]
print("Reverse of 'hello':", reverse('hello'))

uppercase = lambda string: string.upper()
print("Uppercase 'hello':", uppercase('hello'))

sum_of_lsit = lambda lst: sum(lst)
print("Sum of list [1, 2, 3]:", sum_of_lsit([1, 2, 3]))