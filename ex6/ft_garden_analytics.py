"""
Exercise 6: Garden Analytics
Shows OOP concepts like inheritance, nested classes and static methods.
"""


class Plant:
    """A basic plant."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Create a plant with a name, height (cm) and age (days)."""
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> int:
        """Grow the plant by 1cm."""
        self.height += 1
        return 1

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """A plant that has flowers."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Create a flowering plant with a flower color."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> bool:
        """Check if the plant can bloom."""
        return True

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """A flower that won competition points."""

    def __init__(self, name: str, height: int, age: int,
                 color: str, prize_points: int) -> None:
        """Create a prize flower with competition points."""
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def __str__(self) -> str:
        return (f"{self.name}: {self.height}cm, {self.color} flowers "
                f"(blooming), Prize points: {self.prize_points}")


class Garden:
    """A garden that holds plants."""

    def __init__(self, name: str) -> None:
        """Create a garden with an owner name."""
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
        """Make all plants grow."""
        print(f"\n{self.name} is helping all plants grow...")
        for plant in self.plants:
            growth = plant.grow()
            self.total_growth += growth
            print(f"{plant.name} grew {growth}cm")
        print()

    def report(self) -> None:
        """Print a report of the garden."""
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant}")
        print(f"\nPlants added: {self.added_count}, "
              f"Total growth: {self.total_growth}cm")

        # Count different plant types
        regular_count = 0
        flowering_count = 0
        prize_count = 0

        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                prize_count += 1
            elif isinstance(plant, FloweringPlant):
                flowering_count += 1
            else:
                regular_count += 1

        print(f"Plant types: {regular_count} regular, "
              f"{flowering_count} flowering, {prize_count} prize flowers\n")
        print(f"All plants healthy: {self.validate_heights()}")

    def validate_heights(self) -> bool:
        """Check that all plants have positive heights."""
        return all(p.height > 0 for p in self.plants)

    def garden_score(self) -> int:
        """Calculate the total score for the garden."""
        score = 0

        # Add height of each plant
        for plant in self.plants:
            score += plant.height

        # Add prize points if plant has them
        for plant in self.plants:
            if hasattr(plant, 'prize_points'):
                score += plant.prize_points

        return score


class GardenManager:
    """Manages multiple gardens."""

    class GardenStats:
        """Helper class for garden stats."""

        @staticmethod
        def total_plants(gardens: list) -> int:
            """Count all plants across gardens."""
            total = 0
            for garden in gardens:
                total += len(garden.plants)
            return total

        @staticmethod
        def average_garden_height(gardens: list) -> float:
            """Get average total height per garden."""
            if not gardens:
                return 0

            total_height = 0
            count = 0

            for garden in gardens:
                if garden.plants:
                    garden_height = 0
                    for plant in garden.plants:
                        garden_height += plant.height
                    total_height += garden_height
                    count += 1

            if count == 0:
                return 0
            return total_height / count

    def __init__(self) -> None:
        """Create an empty garden manager."""
        self.gardens = []

    def add_garden(self, garden: Garden) -> None:
        """Add a garden."""
        self.gardens.append(garden)

    def create_garden_network(self, names: list) -> "GardenManager":
        """Create gardens for a list of owner names."""
        for name in names:
            self.add_garden(Garden(name))
        return self

    @staticmethod
    def utility_garden_tip() -> str:
        """Return a gardening tip."""
        return "Water your plants in the morning for best results."

    def show_scores(self) -> None:
        """Show scores for all gardens."""
        score_list = []
        for garden in self.gardens:
            score = garden.garden_score()
            score_list.append(f"{garden.name}: {score}")

        scores_text = ", ".join(score_list)
        print(f"Garden scores - {scores_text}")

    def show_total_gardens(self) -> None:
        """Show how many gardens we manage."""
        print(f"Total gardens managed: {len(self.gardens)}")


def ft_garden_analytics() -> None:
    """Demo the garden system."""
    print("=== Garden Management System Demo ===\n")

    manager = GardenManager()
    manager.create_garden_network(["Alice", "Bob"])
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
