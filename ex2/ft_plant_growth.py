
class Plant:
    """
    A plant class that can grow and age over time.

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

    def grow(self) -> None:
        """
        Increase the plant's height by 1cm.

        Simulates one day of growth.
        """
        self.height += 1

    def age_up(self) -> None:
        """
        Increase the plant's age by 1 day.

        Simulates the passage of one day.
        """
        self.age += 1

    def get_info(self) -> str:
        """
        Get current plant status information.

        Returns:
            str: Current plant status
        """
        return self.__str__()


def ft_plant_growth() -> None:
    """
    Simulate plant growth over a week period.

    Creates a plant and demonstrates growth and aging
    over 6 days, showing the difference between day 1 and day 7.
    """
    # Create a plant
    rose = Plant("Rose", 25, 30)

    # Store initial height for growth calculation
    initial_height = rose.height

    # Show day 1
    print("=== Day 1 ===")
    print(rose)

    # Simulate 6 days of growth (to get to day 7)
    for day in range(6):
        rose.grow()
        rose.age_up()

    # Show day 7
    print("=== Day 7 ===")
    print(rose)

    # Calculate and show growth
    growth = rose.height - initial_height
    print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
