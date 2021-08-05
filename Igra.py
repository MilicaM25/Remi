import random
from enum import Enum

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
	RANK = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
	RANK_VALUE = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12,
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
					for r in Card.RANK_VALUE:
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
		self.flip_card()

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
		self.deck.shuffle()
		self.cards_that_are_put_on_table = []
		self.table = []
		self.state_status = TurnState.DRAW_CARD
		self.hands = [
			[] for _ in range(self.number_of_players)
		]
		self.open_players = [
			False for _ in range(self.number_of_players)
		]
		self.number_of_sets = 3 #dobijamo od igraca koliko ima setova
		self.made_hand = [
			[] for _ in range(self.number_of_sets)
		]
		self.hand_count = 0

	def deal_hand(self):

		i = 0
		while i < self.number_of_players:
			for k in range(14):
				deckcard = self.deck.draw_card()
				self.hands[i].append(deckcard)
			i += 1


	def can_you_draw_card(self):

		if not self.state_status == TurnState.DRAW_CARD:
			return False
		elif len(self.hands[self.current_player]) > 15 or len(self.hands[self.current_player]) <= 0:
			return False
		else:
			return True

	def can_you_draw_from_known_pile(self):

		if self.count_turns == 0:
			return True
		elif self.open_players[self.current_player] == True:
			return True
		else:
			pass
			# slucaj kada igrac nije otvoren, a zeli da uzme kartu sa sredine da bi se otvorio
			# mora da se proveri da li igrac moze tako nesto da uradi


	def pickup_card_from_unknown_pile(self):

		if not self.can_you_draw_card():
			print("Can not take card")
			exit(1)

		pickupcard = self.deck.draw_card()
		self.state_status = TurnState.OPEN_OR_DISCARD_CARD
		return self.hands[self.current_player].append(pickupcard)

	def pickup_card_from_known_pile(self):

		if not self.can_you_draw_card():
			print("Can not take card")
			exit(1)

		if not self.can_you_draw_from_known_pile():
			print("Can not take card from discard pile")
			exit(1)

		pickupcard = self.table.pop()
		self.state_status = TurnState.OPEN_OR_DISCARD_CARD
		return self.hands[self.current_player].append(pickupcard)

	def is_valid_opening(self):

		for sets in self.made_hand:
			for item in sets:
				self.hand_count += self.made_hand[sets][item].value

		if not self.state_status == TurnState.OPEN_OR_DISCARD_CARD:
			return False
		elif self.hand_count <= 51:
			return False
		else:
			pass

	def open (self):

		#nesto

		if not self.is_valid_opening():
			print("Can not open")
			exit(1)

		self.state_status = TurnState.PUT_CARD_ON_TABLE

	def can_you_add_to_already_existing_set(self):

		if not self.state_status == TurnState.OPEN_OR_DISCARD_CARD or not  self.state_status == TurnState.PUT_CARD_ON_TABLE:
			return False
		else:
			pass


	def adding_to_already_existing_set(self):

		if not self.can_you_add_to_already_existing_set():
			print("Can not add card to another set")
			exit(1)

		self.state_status = TurnState.DISCARD_CARD

	def is_valid_to_discard_card(self):
		return self.state_status == TurnState.OPEN_OR_DISCARD_CARD or self.state_status == TurnState.PUT_CARD_ON_TABLE or self.state_status == TurnState.DISCARD_CARD

	def discard_card(self, card_index):

		if not self.is_valid_to_discard_card():
			print("You can not discard card")
			exit(1)

		discard_card  = self.hands[self.current_player].pop(card_index)
		self.deck.table.append(discard_card)

		self.state_status = TurnState.FINISH_MOVE

	def get_current_player(self):
		return self.current_player

	def is_valid_finish_turn(self):
		return self.state_status == TurnState.FINISH_MOVE

	def finish_turn(self):

		if not self.is_valid_finish_turn():
			print("Can not finish turn")
			exit(1)

		self.current_player = (self.current_player + 1) % self.number_of_players

		self.count_turns += 1 if self.current_player == 0 else 0

		self.state_status = TurnState.DRAW_CARD

	def get_last_thrown_card(self):
		pass

	def is_hand_empty(self, hand):
		return len(hand) == 0

	def is_game_over(self):

		i = 0

		while i < self.number_of_players:
			if self.is_hand_empty(self.hands[i]):
				return True
			i += 1

		return False

	def calculate_score(self):
		pass

