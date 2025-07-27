def custom_map(func, iterable):
    return [func(x) for x in iterable]

def custom_filter(func, iterable):
    return [func(x) for x in iterable if func(x)]

def custom_reduce(func, iterable):
    res = iterable[0]

    for x in iterable[1:]:
        res = func(res, x)
    return res

#________________________________________________________

# Example usage:
custom_map(lambda x:x*2, [1, 2, 3, 4])  # Output: [2, 4, 6, 8]
custom_filter(lambda x: x > 2, [1, 2, 3, 4])  # Output: [3, 4]
custom_reduce(lambda x,y:x + y, [1, 2, 3, 4])  # Output: 10