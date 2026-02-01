"""
Exercise 1: Garden Data
Demonstrates working with collections of objects using tuples.
"""


class Plant:
    """A simple Plant class representing a garden plant."""

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


def ft_garden_data() -> None:
    """Display a registry of multiple plants stored in a tuple."""
    plants = (
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    )

    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(f"{plant.name}:", f"{plant.height}cm,", f"{plant.age} days old")


if __name__ == "__main__":
    ft_garden_data()
