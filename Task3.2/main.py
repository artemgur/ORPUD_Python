def print_in_out_decorator(func):
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper


@print_in_out_decorator
def test_function(*args, **kwargs):
    kwargs['args'] = args
    return kwargs


max_decorated = print_in_out_decorator(max)
print_decorated = print_in_out_decorator(print)


max_decorated(5, 3, 8, 10, 3)
test_function(4, 5, test=True)
print_decorated(':-)')
