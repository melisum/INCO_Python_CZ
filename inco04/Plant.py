class Plant:
    def __init__(self, color, water_absorption, water_need_level):
        self.color = color
        self.water_level = 0
        self.water_absorption = water_absorption
        self.water_need_level = water_need_level

    def needs_water(self):
        return self.water_level < self.water_need_level

    def water(self, water_amount):
        self.water_level += water_amount * (self.water_absorption / 100)

    def __str__(self):
        if self.needs_water():
            end_string = "needs water"
        else:
            end_string= "doesn't need water"
        return f"The {self.color} {type(self).__name__} {end_string}"



