
from typing import List, Tuple


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
        return f"{self.name}: ({self.height}cm, {self.age} days)"


def ft_plant_factory() -> None:
    """
    Create and display multiple plants from structured data.

    Demonstrates efficient plant creation using data separation
    and factory pattern principles.
    """
    print("=== Plant Factory Output ===")

    # Plant data separated from creation logic
    plant_data: List[Tuple[str, int, int]] = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]

    # Create plants from data
    plants: List[Plant] = []
    for name, height, age in plant_data:
        plants.append(Plant(name, height, age))

    # Display created plants
    for plant in plants:
        print("Created:", plant)

    print(f"\nTotal plants created: {len(plants)}")


if __name__ == "__main__":
    ft_plant_factory()
