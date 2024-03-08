from src.clothes import Clothes

class Pants(Clothes):
    def __init__(self, size, color, style):
        super().__init__(size, color)
        self.style = style

    def __str__(self):
        return super().__str__() + f", Style: {self.style}"
