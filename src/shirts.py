from src.clothes import Clothes

class TShirt(Clothes):
    def __init__(self, size, color, design):
        super().__init__(size, color)
        self.design = design

    def __str__(self):
        return super().__str__() + f", Design: {self.design}"
