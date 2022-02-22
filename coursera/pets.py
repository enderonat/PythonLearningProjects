def pets(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)


pets('cats.txt')
pets('dogs.txt')
