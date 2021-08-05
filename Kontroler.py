from Bot1 import Bot1
from Igra import Game


class Controller:

	def __init__(self):

		self.game = Game(2)
		self.bot = Bot1()

	def play(self):
		while not self.game.is_game_over():
			self.bot.make_a_move(self.game)

		self.game.calculate_score()

		print("Gotovooo")