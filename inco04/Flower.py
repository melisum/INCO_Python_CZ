from inco04.Plant import Plant


class Flower(Plant):
    def __init__(self, color):
        super().__init__(color, 75, 5)