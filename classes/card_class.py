class Card:
    def __init__(self, card_type, num):
        self.type = card_type
        self.num = num

    def show(self):
        print({
            "type": self.type,
            "number": self.num
        })
