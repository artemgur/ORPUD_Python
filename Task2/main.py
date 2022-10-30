import os


while True:
    command = input('> ')
    if command == 'pwd':
        print(os.getcwd())
    elif command.startswith('cd'):
        os.chdir(command.removeprefix('cd '))
    elif command.startswith('touch'):
        file_path = command.removeprefix('touch ')
        open(file_path, 'w').close()
    elif command.startswith('cat'):
        file_path = command.removeprefix('cat ')
        with open(file_path, 'r') as file:
            print(file.read())
    elif command == 'ls':  # Уточнение. Работает, как ls в Linux, выводит список файлов и папок
        print(os.listdir(os.getcwd()))
    elif command.startswith('rm'):
        file_path = command.removeprefix('rm ')
        os.remove(file_path)
    elif command == 'exit':
        break
    else:
        print('Invalid command, try again')