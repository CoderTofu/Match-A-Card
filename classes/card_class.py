class Card:
    def __init__(self, type, num):
        self.type = type
        self.num = num

    def show(self):
        print({
            "type": self.type,
            "number": self.num
        })