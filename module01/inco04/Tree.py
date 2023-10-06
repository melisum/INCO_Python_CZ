from inco04.Plant import Plant


class Tree(Plant):
    def __init__(self, color):
        super().__init__(color, 40, 10)