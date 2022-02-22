filename = 'guestbook.txt'


with open(filename, 'a') as file_object:
    while file_object:
        print('type close to quit')
        name = input('write your name to get in the list:')
        if name == 'close':
            break
        file_object.write(f'\n{name}')
