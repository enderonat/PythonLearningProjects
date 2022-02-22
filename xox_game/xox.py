tiktak = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
x = []
y = []

print(
	"\n  |7|8|9|\n  |4|5|6|\n  |1|2|3|\n  use this map of numbers to choose your position."
)

for turn in range(0,9):

	# Player x combinations
	if 1 in x and 2 in x and 3 in x:
		print("X won!!!!!")
		break

	if 4 in x and 5 in x and 6 in x:
		print("X won!!!!!")
		break

	if 7 in x and 8 in x and 9 in x:
		print("X won!!!!!")
		break

	if 7 in x and 4 in x and 1 in x:
		print("X won!!!!!")
		break

	if 8 in x and 5 in x and 2 in x:
		print("X won!!!!!")
		break

	if 9 in x and 6 in x and 3 in x:
		print("X won!!!!!")
		break

	if 7 in x and 5 in x and 3 in x:
		print("X won!!!!!")
		break

	if 1 in x and 5 in x and 9 in x:
		print("X won!!!!!")
		break

	# player y combinations
	if 1 in y and 2 in y and 3 in y:
		print("O won!!!!!")
		break

	if 4 in y and 5 in y and 6 in y:
		print("O won!!!!!")
		break

	if 7 in y and 8 in y and 9 in y:
		print("O won!!!!!")
		break

	if 7 in y and 4 in y and 1 in y:
		print("O won!!!!!")
		break

	if 8 in y and 5 in y and 2 in y:
		print("O won!!!!!")
		break

	if 9 in y and 6 in y and 3 in y:
		print("O won!!!!!")
		break

	if 7 in y and 5 in y and 3 in y:
		print("O won!!!!!")
		break

	if 1 in y and 5 in y and 9 in y:
		print("O won!!!!!")
		break

	if (turn % 2) == 0:
		number = input("player 'x' pick a place from numpad")
		x.append(int(number))

		if number == '1':
			tiktak[0] = 'x'

		elif number == '2':
			tiktak[1] = 'x'

		elif number == '3':
			tiktak[2] = 'x'

		elif number == '4':
			tiktak[3] = 'x'

		elif number == '5':
			tiktak[4] = 'x'

		elif number == '6':
			tiktak[5] = 'x'

		elif number == '7':
			tiktak[6] = 'x'

		elif number == '8':
			tiktak[7] = 'x'

		elif number == '9':
			tiktak[8] = 'x'

		else:
			print("please use a single number from numpad")
			break
	
	elif turn == 9:
		print("Draw")
		break

	else:
		number = input("player 'y' pick a place from numpad")
		y.append(int(number))

		if number == '1':
			tiktak[0] = 'o'

		elif number == '2':
			tiktak[1] = 'o'

		elif number == '3':
			tiktak[2] = 'o'

		elif number == '4':
			tiktak[3] = 'o'

		elif number == '5':
			tiktak[4] = 'o'

		elif number == '6':
			tiktak[5] = 'o'

		elif number == '7':
			tiktak[6] = 'o'

		elif number == '8':
			tiktak[7] = 'o'

		elif number == '9':
			tiktak[8] = 'o'

		else:
			print("please use a single number from numpad")
			break

	print(
		f"\n({tiktak[6]})({tiktak[7]})({tiktak[8]})"
		f"\n({tiktak[3]})({tiktak[4]})({tiktak[5]})"
		f"\n({tiktak[0]})({tiktak[1]})({tiktak[2]})"
	)


input('open the file again to play again.')