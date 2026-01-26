
from typing import List


class Plant:
    """
    A simple plant class representing a garden plant.

    Attributes:
        name (str): The plant's name
        height (int): The plant's height in cm
        age (int): The plant's age in days
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a Plant.

        Args:
            name (str): The plant's name
            height (int): The plant's height in cm
            age (int): The plant's age in days
        """
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        """
        Return string representation of the plant.

        Returns:
            str: Formatted string with plant information
        """
        return f"{self.name}: {self.height}cm, {self.age} days old"


def ft_garden_data() -> None:
    """
    Create and display multiple plants in a garden registry.

    Demonstrates basic class usage and object creation
    by managing data for several plants.
    """
    print("=== Garden Plant Registry ===")
    plants: List[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Tulip", 40, 20)
    ]

    for plant in plants:
        print(plant)


if __name__ == "__main__":
    ft_garden_data()
