
class SecurePlant:
    """
    Plant class that keeps data safe.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """Make a new plant with some checks.

        Args:
            name: what to call the plant
            height: how tall it is in cm
            age: how old it is in days
        """
        self._name = name
        print(f"Plant created: {name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        """Change the plant height but check if it makes sense first.

        Args:
            height: new height in cm (can't be negative)
        """
        if height >= 0:
            self._height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def get_height(self) -> int:
        """Just return the height.

        Returns:
            the plant's height in cm
        """
        return self._height

    def set_age(self, age: int) -> None:
        """Change age but make sure it's not negative.

        Args:
            age: new age in days (has to be 0 or more)
        """
        if age >= 0:
            self._age = age
            print(f"Age updated: {age} days [OK]\n")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_age(self) -> int:
        """Get the age.

        Returns:
            how old the plant is in days
        """
        return self._age

    def get_name(self) -> str:
        """Get the name.

        Returns:
            the plant's name
        """
        return self._name

    def __str__(self) -> str:
        """Show plant info when printed.

        Returns:
            string with plant name, height and age
        """
        return f"{self._name} ({self._height}cm, {self._age} days)"


def ft_garden_security() -> None:
    """
    Test the secure plant thing.
    """
    print("=== Garden Security System ===")

    # make a plant
    plant = SecurePlant("Rose", 25, 30)

    # try to set negative height - should not work
    plant.set_height(-5)

    print(f"\nCurrent plant: {plant}")


if __name__ == "__main__":
    ft_garden_security()
