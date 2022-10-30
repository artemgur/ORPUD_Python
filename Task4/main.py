numbers = input('> ').split(' ')

try:
    parsed_comprehension = [int(x) for x in numbers]
except ValueError:
    print(-1)
    exit()

even_comprehension = [x for x in parsed_comprehension if x % 2 == 0]
odd_comprehension = [x for x in parsed_comprehension if x % 2 == 1]
negative_comprehension = [x for x in parsed_comprehension if x < 0]

print(even_comprehension)
print(odd_comprehension)
print(negative_comprehension)


try:
    parsed_map = list(map(lambda x: int(x), numbers))
except ValueError:
    print(-1)
    exit()

even_map = list(filter(lambda x: x % 2 == 0, parsed_map))
odd_map = list(filter(lambda x: x % 2 == 1, parsed_map))
negative_map = list(filter(lambda x: x < 0, parsed_map))

print(even_map)
print(odd_map)
print(negative_map)
