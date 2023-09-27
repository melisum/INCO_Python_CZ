from inco04.Flower import Flower
from inco04.Garden import Garden
from inco04.Tree import Tree
from inco04.Plant import Plant


# The Garden Application
# The task is to create a garden application, so in your main method you should create a garden with flowers and trees. The program should demonstrate an example garden with two flowers (yellow and blue) and two trees (purple and orange). After creating these plants you should show the user how the garden looks like. After that the program should water the garden twice, first with the amount of 40 then with 70. After every watering the user should see the state of the garden as you can see in the output below:
#
# The yellow Flower needs water
# The blue Flower needs water
# The purple Tree needs water
# The orange Tree needs water
#
# Watering with 40
# The yellow Flower doesn't need water
# The blue Flower doesn't need water
# The purple Tree needs water
# The orange Tree needs water
#
# Watering with 70
# The yellow Flower doesn't need water
# The blue Flower doesn't need water
# The purple Tree doesn't need water
# The orange Tree doesn't need water
# Information on the elements
# The Garden
# is able to hold unlimited amount of flowers and trees
# when watering it should only water those plants that need water with equally divided amount amongst them
# eg. watering with 40 and 4 of them need water then each gets watered with 10
# The Flower
# needs water if its current water amount is less than 5
# when watered the flower can only absorb 75% of the water
# eg. watering with 10 the flower's amount of water should only increase by 7.5
# The Tree
# needs water if its current water amount is less than 10
# when watered the tree can only absorb the 40% of the water
# eg. watering with 10 the tree's amount of water should only increase by 4
class Main:
    @staticmethod
    def main():
        secret_garden = Garden("My garden")

        secret_garden.add_plant(Flower("yellow"))
        secret_garden.add_plant(Flower("blue"))
        secret_garden.add_plant(Tree("purple"))
        secret_garden.add_plant(Tree("orange"))

        secret_garden.status_garden()

        secret_garden.water_garden(40)

        secret_garden.water_garden(70)



if __name__ == "__main__":
    Main.main()
