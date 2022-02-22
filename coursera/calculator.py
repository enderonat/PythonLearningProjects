x = 0
while x == 0:

    number1 = (input('first number: '))
    number2 = (input('second number: '))

    if number1 == 'q':
        break

    try:
        print(int(number1) + int(number2))
        print("type 'q' to quit")
    except ValueError:
        print('you need to use a number')
        print("type 'q' to quit")
