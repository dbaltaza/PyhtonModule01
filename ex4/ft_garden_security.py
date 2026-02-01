"""
Exercise 4: Garden Security
Demonstrates encapsulation using private attributes and getter/setter methods.
"""


class SecurePlant:
    """A Plant class with encapsulated attributes for data validation."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a SecurePlant instance with validation.

        Args:
            name: The name of the plant.
            height: The height of the plant in centimeters (must be >= 0).
            age: The age of the plant in days (must be >= 0).
        """
        self._name = name
        print(f"Plant created: {name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        """
        Set the plant height with validation.

        Args:
            height: New height in centimeters (must be >= 0).
        """
        if height >= 0:
            self._height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def get_height(self) -> int:
        """Return the plant height."""
        return self._height

    def set_age(self, age: int) -> None:
        """
        Set the plant age with validation.

        Args:
            age: New age in days (must be >= 0).
        """
        if age >= 0:
            self._age = age
            print(f"Age updated: {age} days [OK]\n")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_age(self) -> int:
        """Return the plant age."""
        return self._age

    def get_name(self) -> str:
        """Return the plant name."""
        return self._name

    def __str__(self) -> str:
        """Return string representation of the plant."""
        return f"{self._name} ({self._height}cm, {self._age} days)"


def ft_garden_security() -> None:
    """Demonstrate secure plant creation with validation."""
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, 30)
    plant.set_height(-5)
    print(f"\nCurrent plant: {plant}")


if __name__ == "__main__":
    ft_garden_security()
