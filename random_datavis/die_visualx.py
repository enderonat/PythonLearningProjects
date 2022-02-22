import matplotlib.pyplot as plt

from die import Die


# Create a D6.
die = Die()

# Make some rolls and store results in a list.
results = []
for roll_num in range(100000):
	result = die.roll()
	results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)
input_values = []

y = 1

for x in range(die.num_sides):
	input_values.append(y)
	y += 1
	if y > die.num_sides:
		break

print(frequencies)

# Visualize the results.
fig, ax = plt.subplots()
ax.scatter(input_values, frequencies, s=20)

plt.show()