import random
from enum import Enum, auto

class TurnState(Enum):
	DRAW_CARD = 1
	OPEN_OR_DISCARD_CARD = 2
	PUT_CARD_ON_TABLE = 3
	DISCARD_CARD = 4
	FINISH_MOVE = 5


#Klasa karta- model jedne karte
class Card:
	SYMBOLS = ['♠', '♢', '♡', '♣']
	SUIT = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
	RANK = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
	RANK_VALUE = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12,
				  'K': 13}
	SUIT_SYMBOLS = {'Hearts': '♡', 'Clubs': '♣', 'Spades': '♠', 'Diamonds': '♢'}

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
		self.cards = []	#dek nepoznatih karata
		self.table = [] #bacene karte na sto
		self.build_deck()

	# Kreira dek karata
	def build_deck(self):
			for i in range(self.packs):
				for s in Card.SUIT:
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
		self.table.clear()

	def draw_card(self):

		if self.is_empty():
			self.remake_deck()
		else:
			return self.cards.pop()

	def flip_card(self):

		card_flipped = self.cards.pop()
		return self.table.append(card_flipped)


class Game:

	def __init__(self, number_of_players):

		self.number_of_players = number_of_players
		self.count_turns = 0
		self.current_player = 0
		self.deck = Deck(2)
		self.cards_that_are_put_on_table = []
		self.table = []
		self.state_status = TurnState.DRAW_CARD

	def player_initialization(self, number_of_players):
		pass

	def deal_card(self):

            deckcard = self.deck.draw_card()
            self.hand.append(deckcard)

	def deal_hand(self):

         for i in range(14):
             self.deal_card()


	def draw_card(self):

		if not self.state_status == TurnState.DRAW_CARD:
			print("Not valid move")
		else:
			pass

		self.state_status = TurnState.OPEN_OR_DISCARD_CARD


	def pickup_card_from_unknown_pile(self):
		pickupcard = self.deck.table.pop()
		return self.hand.append(pickupcard)

	def pickup_card_from_known_pile(self):
		pickupcard = self.deck.table.pop()

		return self.hand.append(pickupcard)

	def is_valid_opening(self):

		if not self.state_status == TurnState.OPEN_OR_DISCARD_CARD:
			print("Not valid move")
		else:
			pass

		self.state_status = TurnState.PUT_CARD_ON_TABLE

	def can_you_add_to_already_existing_set(self):

		if not self.state_status == TurnState.OPEN_OR_DISCARD_CARD or not  self.state_status == TurnState.PUT_CARD_ON_TABLE:
			print("Not valid move")
		else:
			pass

		self.state_status = TurnState.DISCARD_CARD

	def adding_to_already_existing_set(self):
		pass

	def discard_card(self, card_index):

		if not self.state_status == TurnState.OPEN_OR_DISCARD_CARD or not  self.state_status == TurnState.PUT_CARD_ON_TABLE or not self.state_status == TurnState.DISCARD_CARD:
			print("Not valid move")
		else:
			discard_card  = self.hand.pop(card_index)
			self.deck.table.append(discard_card)

		self.state_status == TurnState.FINISH_MOVE

	def get_current_player(self):

		return self.current_player

	def finish_turn(self):

		if not self.state_status == TurnState.FINISH_MOVE:
			print("Not valid move")
		else:
			pass

		self.state_status == TurnState.DRAW_CARD

	def next_player(self):

		self.current_player = (self.current_player + 1) % self.number_of_players

		self.count_turns += 1 if self.current_player == 0 else 0


	def get_last_thrown_card(self):
		pass

	def is_game_over(self):

		return self.count_turns == 10

	def calculate_score(self):
		pass

