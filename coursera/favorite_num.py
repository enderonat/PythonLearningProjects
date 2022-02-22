import json

def store_number():
    fav_num = input('write your favorite number: ')

    filename = 'number.json'
    with open(filename, 'w') as f:
        json.dump(fav_num, f)
        print('we will remember this number')

def call_number():
    filename = 'number.json'
    with open(filename) as f:
        fav_num = json.load(f)
        print(f'your favorite number is {fav_num}')
