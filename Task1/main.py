history = {'+': [], '-': [], '*': [], '/': []}

print('Calculator started, enter "q" instead of operation to quit')

while True:
    try:
        num1 = int(input('> '))
        num2 = int(input('> '))
    except ValueError:
        print('Invalid number, enter numbers and operation again')
        continue

    operation = input('> ')

    match operation:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            result = num1 / num2
        case 'q':
            break
        case _:
            print('Invalid operation, enter numbers and operation again')
            continue

    operation_str = f'{num1}{operation}{num2}={result}'
    history[operation].append(operation_str)

    print()
    print(operation_str)
    for key, value in history.items():
        print(f'{key} {value}')
