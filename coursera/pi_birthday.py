filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
birthday = input("Enter your birthday, in the form of ddmmyy: ")

for line in lines:
    if birthday in pi_string:
        print('your birthday appears in million digits of pi!!')
        break
    else:
        pi_string += line

print(pi_string)
