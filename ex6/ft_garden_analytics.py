"""
Exercise 6: Garden Analytics
Demonstrates advanced OOP: nested classes, class methods, static methods,
inheritance hierarchies, and encapsulation.
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

    def grow(self) -> int:
        """Grow the plant by 1cm and return the growth amount."""
        self.height += 1
        return 1

    def __str__(self) -> str:
        """Return string representation of the plant."""
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """A flowering plant with color attribute."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initialize a FloweringPlant instance.

        Args:
            name: The name of the plant.
            height: The height in centimeters.
            age: The age in days.
            color: The color of the flowers.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> bool:
        """Return True indicating the plant can bloom."""
        return True

    def __str__(self) -> str:
        """Return string representation of the flowering plant."""
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """A prize-winning flower with competition points."""

    def __init__(self, name: str, height: int, age: int,
                 color: str, prize_points: int) -> None:
        """
        Initialize a PrizeFlower instance.

        Args:
            name: The name of the flower.
            height: The height in centimeters.
            age: The age in days.
            color: The color of the flowers.
            prize_points: Points earned in competitions.
        """
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def __str__(self) -> str:
        """Return string representation of the prize flower."""
        return (f"{self.name}: {self.height}cm, {self.color} flowers "
                f"(blooming), Prize points: {self.prize_points}")


class Garden:
    """A garden that manages a collection of plants."""

    def __init__(self, name: str) -> None:
        """
        Initialize a Garden instance.

        Args:
            name: The name of the garden owner.
        """
        self.name = name
        self.plants = []
        self.total_growth = 0
        self.added_count = 0

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden."""
        self.plants.append(plant)
        self.added_count += 1
        print(f"Added {plant.name} to {self.name}'s garden")

    def help_grow(self) -> None:
        """Make all plants in the garden grow."""
        print(f"\n{self.name} is helping all plants grow...")
        for plant in self.plants:
            growth = plant.grow()
            self.total_growth += growth
            print(f"{plant.name} grew {growth}cm")
        print()

    def report(self) -> None:
        """Print a detailed report of the garden."""
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant}")
        print(f"\nPlants added: {self.added_count}, "
              f"Total growth: {self.total_growth}cm")

        reg = sum(isinstance(p, Plant) and not isinstance(p, FloweringPlant)
                  for p in self.plants)
        flow = sum(isinstance(p, FloweringPlant)
                   and not isinstance(p, PrizeFlower) for p in self.plants)
        prize = sum(isinstance(p, PrizeFlower) for p in self.plants)
        print(f"Plant types: {reg} regular, {flow} flowering, "
              f"{prize} prize flowers")
        print(f"Height validation test: {self.validate_heights()}")

    def validate_heights(self) -> bool:
        """Validate that all plants have positive heights."""
        return all(p.height > 0 for p in self.plants)

    def garden_score(self) -> int:
        """Calculate the total score for the garden."""
        score = sum(p.height for p in self.plants)
        score += sum(getattr(p, 'prize_points', 0) for p in self.plants)
        return score


class GardenManager:
    """Manages multiple gardens with analytics capabilities."""

    class GardenStats:
        """Nested class for calculating garden statistics."""

        @staticmethod
        def total_plants(gardens: list) -> int:
            """Return the total number of plants across all gardens."""
            return sum(len(g.plants) for g in gardens)

        @staticmethod
        def average_garden_height(gardens: list) -> float:
            """Return the average total height across gardens."""
            heights = [sum(p.height for p in g.plants)
                       for g in gardens if g.plants]
            return sum(heights) / len(heights) if heights else 0

    def __init__(self) -> None:
        """Initialize a GardenManager instance."""
        self.gardens = []

    def add_garden(self, garden: Garden) -> None:
        """Add a garden to the manager."""
        self.gardens.append(garden)

    @classmethod
    def create_garden_network(cls, names: list) -> "GardenManager":
        """
        Create a network of gardens from a list of owner names.

        Args:
            names: List of garden owner names.

        Returns:
            A GardenManager instance with gardens created.
        """
        manager = cls()
        for name in names:
            manager.add_garden(Garden(name))
        return manager

    @staticmethod
    def utility_garden_tip() -> str:
        """Return a helpful gardening tip."""
        return "Water your plants in the morning for best results."

    def show_scores(self) -> None:
        """Display scores for all managed gardens."""
        scores = ", ".join(
            f"{g.name}: {g.garden_score()}" for g in self.gardens)
        print(f"Garden scores - {scores}")

    def show_total_gardens(self) -> None:
        """Display the total number of managed gardens."""
        print(f"Total gardens managed: {len(self.gardens)}")


def ft_garden_analytics() -> None:
    """Demonstrate the garden management system."""
    print("=== Garden Management System Demo ===\n")

    manager = GardenManager.create_garden_network(["Alice", "Bob"])
    alice_garden = manager.gardens[0]
    bob_garden = manager.gardens[1]

    # Alice's plants
    oak = Plant("Oak Tree", 100, 365)
    rose = FloweringPlant("Rose", 25, 30, "red")
    sunflower = PrizeFlower("Sunflower", 50, 60, "yellow", 10)
    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    # Bob's plants (added silently for scoring)
    maple = Plant("Maple", 80, 200)
    tulip = FloweringPlant("Tulip", 12, 15, "purple")
    bob_garden.plants.append(maple)
    bob_garden.plants.append(tulip)

    alice_garden.help_grow()
    alice_garden.report()
    manager.show_scores()
    manager.show_total_gardens()


if __name__ == "__main__":
    ft_garden_analytics()
