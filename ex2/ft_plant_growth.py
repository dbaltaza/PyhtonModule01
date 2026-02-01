"""
Exercise 2: Plant Growth
Demonstrates functions for modifying object attributes over time.
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


def grow(height: int, days: int) -> int:
    """
    Calculate new height after growth.

    Args:
        height: Current height in centimeters.
        days: Number of days of growth.

    Returns:
        New height after growth.
    """
    return height + days


def age(current_age: int, days: int) -> int:
    """
    Calculate new age after time passes.

    Args:
        current_age: Current age in days.
        days: Number of days passed.

    Returns:
        New age in days.
    """
    return current_age + days


def ft_plant_growth() -> None:
    """Simulate plant growth over a week."""
    plant = Plant("Rose", 25, 30)
    days = 1

    print(f"=== Day {days} ===")
    print(f"{plant.name}:", f"{plant.height}cm,", f"{plant.age} days old")

    while days < 6:
        days += 1

    print(f"=== Day {days + 1} ===")
    print(
        f"{plant.name}: {grow(plant.height, days)}cm, "
        f"{age(plant.age, days)} days old"
    )
    print(f"Growth this week: +{days}cm")


if __name__ == "__main__":
    ft_plant_growth()
