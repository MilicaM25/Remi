import random

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

	def player_initialization(self, number_of_players):
		pass

	def deal_card(self):
		pass

	def deal_hand(self):
		pass

	def pickup_card_from_unknown_pile(self):
		pass

	def pickup_card_from_known_pile(self):
		pass

	def is_valid_opening(self):
		pass

	def discard_card(self):
		pass

	def can_you_add_to_already_existing_set(self):
		pass

	def adding_to_already_existing_set(self):
		pass

	def get_current_player(self):

		return self.current_player

	def next_player(self):

		self.current_player = (self.current_player + 1) % self.number_of_players

		self.count_turns += 1 if self.current_player == 0 else 0


	def get_last_thrown_card(self):
		pass

	def is_game_over(self):

		return self.count_turns == 10

	def calculate_score(self):
		pass


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


class Controller:

	def __init__(self):

		self.game = Game(2)
		self.bot = Bot1()

	def play(self):
		while not self.game.is_game_over():
			self.bot.make_a_move(self.game)
		print("Gotovooo")

#Globalne funkcije

def is_valid_run(sequance):
	pass

def main():

	c = Controller()

	c.play()



if __name__ == "__main__":
    main()


"""
#Klasa za modelovanje ruke igraca i njegovih mogucih akcija
class Player:

	def __init__(self, name, deck, game):

		self.name = name	#ime igraca
		self.deck = deck  	#trenutni objekat deka igre
		self.game = game  	#trenutni objekat igre

		# Karte igraca
		self.hand = []  	# Karte koje igrac poseduje
		self.made_hand = [] # Karte koje je izlozio igrac
		self.is_open = False #Da li je igrac otvoren
		self.is_it_first_move = True #Da li je igracu prvi potez


	def deal_card(self):
		deckcard = self.deck.draw_card()
		self.hand.append(deckcard)

	def deal_hand(self):

		if self.is_it_first_move:
			for i in range(14):
				self.deal_card()

	def pickup_card_from_known_pile (self):
		#Adds pick up card from table to player's hand.
		pickupcard = self.deck.table.pop()

		return self.hand.append(pickupcard)

	def pickup_card_from_unknown_pile (self):
		pickupcard = self.deck.cards.pop()

		return self.hand.append(pickupcard)

	def throw_out(self, card_index):
		#Removes card from player's hand to table.

#		if card_index < 0 or card_index > 15:
#			print('That is not a valid card index. Remeber the cards are ordered 1 - 15, the top representing 1 and the bottom 13.')

		throwout = self.hand.pop(card_index)
		self.deck.table.append(throwout)


"""