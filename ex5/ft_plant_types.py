"""
Exercise 5: Plant Types
Demonstrates inheritance with specialized plant classes.
"""


class Plant:
    """Base class representing a generic plant."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a Plant instance.

        Args:
            name: The name of the plant.
            height: The height of the plant in centimeters.
            age: The age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """A flowering plant with color attribute."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initialize a Flower instance.

        Args:
            name: The name of the flower.
            height: The height in centimeters.
            age: The age in days.
            color: The color of the flower.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        """Return a message indicating the flower is blooming."""
        return f"{self.name} is blooming beautifully!"

    def __str__(self) -> str:
        """Return string representation of the flower."""
        return (f"{self.name} (Flower): {self.height}cm, "
                f"{self.age} days, {self.color} color")


class Tree(Plant):
    """A tree with trunk diameter attribute."""

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: float) -> None:
        """
        Initialize a Tree instance.

        Args:
            name: The name of the tree.
            height: The height in centimeters.
            age: The age in days.
            trunk_diameter: The diameter of the trunk in centimeters.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> str:
        """Calculate and return the shade area provided by the tree."""
        import math
        area = math.pi * (self.trunk_diameter / 2) ** 2 / 100
        return f"{self.name} provides {int(area)} square meters of shade"

    def __str__(self) -> str:
        """Return string representation of the tree."""
        return (f"{self.name} (Tree): {self.height}cm, "
                f"{self.age} days, {int(self.trunk_diameter)}cm diameter")


class Vegetable(Plant):
    """A vegetable plant with harvest and nutritional information."""

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """
        Initialize a Vegetable instance.

        Args:
            name: The name of the vegetable.
            height: The height in centimeters.
            age: The age in days.
            harvest_season: The season for harvesting.
            nutritional_value: Description of nutritional benefits.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutrition(self) -> str:
        """Return nutritional information about the vegetable."""
        return f"{self.name} is {self.nutritional_value.lower()}"

    def __str__(self) -> str:
        """Return string representation of the vegetable."""
        return (f"{self.name} (Vegetable): {self.height}cm, "
                f"{self.age} days, {self.harvest_season} harvest")


def ft_plant_types() -> None:
    """Demonstrate different specialized plant types."""
    print("=== Garden Plant Types ===\n")

    rose = Flower("Rose", 25, 30, "red")
    print(rose)
    print(rose.bloom())
    print()

    oak = Tree("Oak", 500, 1825, 50)
    print(oak)
    print(oak.produce_shade())
    print()

    tomato = Vegetable("Tomato", 80, 90, "summer", "rich in vitamin C")
    print(tomato)
    print(tomato.nutrition())


if __name__ == "__main__":
    ft_plant_types()
