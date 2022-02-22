import sys

import pygame

class Keys:

	def __init__(self):

		pygame.init()

		self.screen = pygame.display.set_mode((1200, 700))
		pygame.display.set_caption("DA KEYZZ")

	def run_game(self):

		while True:
			self._update_screen()
			self._check_events()

	def _check_events(self):

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYUP:
				print(event.key)

	def _update_screen(self):
		self.screen.fill((230, 230, 230))
		pygame.display.flip()

if __name__ == '__main__':
	ky = Keys()
	ky.run_game()
