def find_max(*args):
    max_value = args[0]
    for i in range(1, len(args)):
        if args[i] > max_value:
            max_value = args[i]
    return max_value


print(find_max(5, 3, 8, 10, 3))
print(find_max(15, 3, 8, 10, 3))
print(find_max(5, 16, 8, 10, 3))
print(find_max(5, 3, 18, 10, 3))
print(find_max(5, 3, 8, 10, 25))
