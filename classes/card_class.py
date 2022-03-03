class Card:
    def __init__(self, card_type, num):
        self.type = card_type
        self.num = num

    def stringify(self):
        return str(self.type) + str(self.num)
