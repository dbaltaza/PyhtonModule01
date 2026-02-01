"""
Exercise 0: Garden Introduction
Demonstrates basic class definition and object instantiation in Python.
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


def ft_garden_intro() -> None:
    """Display basic plant information to introduce the garden system."""
    plant = Plant("Rose", 25, 30)

    print("== Welcome to my Garden ==")
    print("Name:", plant.name)
    print("Height:", f"{plant.height}cm")
    print("Age:", plant.age, "days")
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
