import plotly.express as px
from plotly import offline

from random_walk import RandomWalk


while True:
	# Make a random walk.
	rw = RandomWalk()
	rw.fill_walk()

	fig = px.scatter(x=rw.x_values, y=rw.y_values)
	fig.show()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break
