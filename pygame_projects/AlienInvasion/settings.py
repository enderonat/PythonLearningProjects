class Settings:
	"""class that stores all settings"""

	def __init__(self):
		"""Initialize the games settings"""
		# screen settings
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_color = (230, 230, 230)

		# ship settings
		self.ship_speed = 1
		self.ship_limit = 3

		# bullet settings
		self.bullet_speed = 1.5
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (230, 60, 230)
		self.bullets_allowed = 3

		# alien settings
		self.alien_speed = 0.5
		self.fleet_drop_speed = 50
		# fleet direction 1 represents right -1 is left
		self.fleet_direction = 1
