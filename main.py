import random

SYMBOLS = ['♠', '♢', '♡', '♣']
SUIT = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
RANK = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
RANK_VALUE = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}
SUIT_SYMBOLS = {'Hearts': '♡', 'Clubs': '♣', 'Spades': '♠', 'Diamonds': '♢'}


#Klasa karta- model jedne karte
class Card:

	def __init__(self, rank, suit):

		self.rank = rank
		self.suit = suit

	def __str__(self):

		return (self.rank + self.suit)


#Klasa dek- formira dek karata
class Deck:

	global SUIT
	def __init__(self, packs):

		self.packs = packs
		self.cards = []
		self.table = []
		self.build_deck()

	# Kreira dek karata
	def build_deck(self):
			for i in range(self.packs):
				for s in SUIT:
					for r in range(1, 13):
						self.cards.append(Card(r, s))
	#			for i in range(2):
	#				self.cards.append(Card('Joker', i))

	def shuffle(self):

		random.shuffle(self.cards)

	def is_empty(self):

		return len(self.cards) == 0

	def remake_deck(self):

		self.table.reverse()
		self.cards = self.table

	def draw_card(self):

		if self.is_empty():
			self.remake_deck()
		else:
			return self.cards.pop()

	def flip_card(self):

		card_flipped = self.cards.pop()
		return self.table.append(card_flipped)

