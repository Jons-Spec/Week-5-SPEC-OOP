class Clothes:
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def __str__(self):
        return f"{self.color} {self.__class__.__name__} (Size: {self.size})"
