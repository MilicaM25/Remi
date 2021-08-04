import random
from Igra import Game

class Bot1:

	def __init__(self):

	#	self.last_card = last_card
	#	self.hand = hand
	#	self.cards_on_table = cards_on_table
		self.can_you_open = False

	def make_a_move(self, game):

		print(game.get_current_player(), game.count_turns)
		self.finished_turn(game)

	def make_sets(self, hand):
		pass

	def choose_card_to_pick_up(self, cards_on_table, last_card):
		pass

	def pick_up_card(self):
		pass

	def can_you_open(self, hand):
		pass

	def open(self, can_you_open):
		pass

	def discard_card(self, hand):
		pass

	def finished_turn(self, game):
		game.next_player()
