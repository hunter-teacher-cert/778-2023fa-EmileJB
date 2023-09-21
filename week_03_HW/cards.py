import random

class Playing_card:
  suits = {"Clubs":'\u2663',
          "Hearts":"\u2665",
          "Diamonds":"\u2666",
          "Spades":"\u2660",}
  def __convert_value(self, value):
    if value == "Ace" or value == "A":
      return 14
    elif value == "Jack" or value == "J":
      return 11
    elif value == "Queen" or value == "Q":
      return 12
    elif value == "King" or value == "K":
      return 13
    else:
      return value
  
  def __init__(self, suit, value):
    self.suit = suit
    self.value = value
    self.__internal_value = self.__convert_value(value)

  def __lt__(self, other):
        return self.__internal_value < other.__internal_value

  def __gt__(self, other):
        return self.__internal_value > other.__internal_value

  def __eq__(self, other):
        return self.__internal_value == other.__internal_value

  def __add__(self, other):
        return self.__internal_value + other.__internal_value

  def __str__(self):
        return f"{self.value} of {self.suits[self.suit]}"

  def print_val(self):
    print(f"This card is the {self}")

  def compare(self, other):
    if self < other:
      return "<"
    elif self > other:
      return ">"
    else:
      return "=="

  def get_suit(self):
    return self.suit

  def get_value(self):
    return self.value

  def set_suit(self,suit):
    self.suit = suit

  def set_value(self,value):
    self.value = value
    self.__internal_value = self.__convert_value(value)
    



class Hand_of_cards:
  def __init__(self):
    self.hand = []

  def addCard(self,card):
    self.hand.append(card)

  def removeRandom(self):
    if len(self.hand) == 0:
      return
    rand_card = random.randrange(len(self.hand))
    return self.hand.pop(rand_card)

  def hasMatch(self):
    max_matches = 1
    for target_card in self.hand:
      num_matches = 0
      for other_card in self.hand:
        if target_card == other_card:
          num_matches+=1
          #Used to debug matching problems
          #print(f"Target Card: {target_card}")
          #print(f"Other Card: {other_card}")
      if num_matches == 4:
          return 4
      if num_matches > max_matches:
          max_matches = num_matches
    if max_matches == 1:
      return 0
    else:
      return max_matches

  def printHand(self):
    print("Cards in hand:",end=" ")
    print(*self.hand)


def main():
  valid_values = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
  valid_suits = ["Clubs","Hearts","Diamonds","Spades"]
  deck_of_cards = []
  for value in valid_values:
    for suit in valid_suits:
      new_card = Playing_card(suit,value)
      deck_of_cards.append(new_card)
  random.shuffle(deck_of_cards)
  players = []
  for i in range(4):
    new_player = Hand_of_cards()
    players.append(new_player)
  for player in players:
    for i in range(5):
      player.addCard(deck_of_cards.pop())
    player.printHand()
    print(f"Matches: {player.hasMatch()}")
    print()

  print("\n")

  for player in players:
    print(f"Discarded {player.removeRandom()}")
    new_card = deck_of_cards.pop();
    print(f"Drew {new_card}")
    player.addCard(new_card)
    player.printHand()
    print(f"Matches: {player.hasMatch()}")
    print()

main()