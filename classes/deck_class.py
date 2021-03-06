from classes.card_class import Card


class Deck:

    def __init__(self):
        self.deck = []

    def generate(self):
        card_types = ["♥", "🔹", "♠", "♣"]

        for card_type in card_types:
            for numbers in range(1, 13):  # 4 different types and 12 numbers for each type
                self.deck.append(Card(card_type, numbers))

        return self.deck
