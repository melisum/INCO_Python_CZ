class Garden:
    def __init__(self, name):
        self.name = name
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def status_garden(self):
        for plant in self.plants:
            print(plant)
        print()

    def water_garden(self, water_amount):
        print(f"Watering with {water_amount}")

        need_water = sum(1 for plant in self.plants if plant.needs_water())

        for plant in self.plants:
            if plant.needs_water():
                plant.water((water_amount / need_water))

        self.status_garden()