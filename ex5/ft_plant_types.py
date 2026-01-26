
class Plant:
    """
    Basic plant class that other plant types inherit from.

    Attributes:
        name (str): The plant's name
        height (int): The plant's height in cm
        age (int): The plant's age in days
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a basic Plant.

        Args:
            name: what to call the plant
            height: how tall it is in cm
            age: how old it is in days
        """
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        """
        Show basic plant info.

        Returns:
            string with plant details
        """
        return f"{self.name}: {self.height}cm, {self.age} days"

    def grow(self) -> None:
        """Make the plant grow a bit."""
        self.height += 1
        self.age += 1


class Flower(Plant):
    """
    A flowering plant that inherits from Plant.
    """

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Make a flower plant.

        Args:
            name: flower name
            height: height in cm
            age: age in days
            color: what color the flower is
        """
        super().__init__(name, height, age)  # inherit basic plant stuff
        self.color = color

    def bloom(self) -> None:
        """Make the flower bloom."""
        print(f"{self.name} is blooming beautifully!\n")

    def __str__(self) -> str:
        """
        Show flower info.

        Returns:
            string with flower details
        """
        return f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color"


class Tree(Plant):
    """
    A tree that inherits from Plant.
    """

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """
        Make a tree plant.

        Args:
            name: tree name
            height: height in cm
            age: age in days
            trunk_diameter: how thick the trunk is in cm
        """
        super().__init__(name, height, age)  # inherit basic plant stuff
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Make the tree provide shade."""
        shade_area = self.trunk_diameter * self.height // 100
        print(f"{self.name} provides {shade_area} square meters of shade\n")

    def __str__(self) -> str:
        """
        Show tree info.

        Returns:
            string with tree details
        """
        return (f"{self.name} (Tree): {self.height}cm, {self.age} days, "
                f"{self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """
    A vegetable plant that inherits from Plant.
    """

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """
        Make a vegetable plant.

        Args:
            name: vegetable name
            height: height in cm
            age: age in days
            harvest_season: when to harvest it
            nutritional_value: what nutrients it has
        """
        super().__init__(name, height, age)  # inherit basic plant stuff
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def harvest(self) -> None:
        """Show nutritional info."""
        print(f"{self.name} is rich in {self.nutritional_value}\n")

    def __str__(self) -> str:
        """
        Show vegetable info.

        Returns:
            string with vegetable details
        """
        return (f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
                f"{self.harvest_season} harvest")


def ft_plant_types() -> None:
    """
    Test different plant types.
    """
    print("=== Garden Plant Types ===\n")

    # create 2 flowers
    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 20, 25, "yellow")

    # create 2 trees
    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 300, 1000, 30)

    # create 2 vegetables
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 15, 120, "fall", "vitamin A")

    # show flowers
    print(rose)
    rose.bloom()
    print(tulip)
    tulip.bloom()

    # show trees
    print(oak)
    oak.produce_shade()
    print(pine)
    pine.produce_shade()

    # show vegetables
    print(tomato)
    tomato.harvest()
    print(carrot)
    carrot.harvest()


if __name__ == "__main__":
    ft_plant_types()
   