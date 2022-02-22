import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
	# Make a random walk.
	rw = RandomWalk()
	rw.fill_walk()

	# Plot points in the fill_walk.
	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(15, 9))
	point_numbers = range(rw.num_points)
	ax.plot(rw.x_values, rw.y_values, linewidth=1)

	# The first and last points.
	ax.scatter(0, 0, c='green', edgecolors='none', s=80)
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=80)
	plt.show()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break
