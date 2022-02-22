def word_counter(filename,word):
    try:
        with open(filename, encoding='utf-8') as f:
            file = f.read()
    except FileNotFoundError:
        print('sorry i cant find that file')
    else:
        words =file.lower().split().count(word)
        print(words)

