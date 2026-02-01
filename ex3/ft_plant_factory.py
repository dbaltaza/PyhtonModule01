"""
Exercise 3: Plant Factory
Demonstrates creating multiple objects and tracking collection size.
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


def ft_plant_factory() -> None:
    """Create multiple plants and display factory output."""
    plants = (
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    )

    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
    print("\nTotal plants created:", len(plants))


if __name__ == "__main__":
    ft_plant_factory()
