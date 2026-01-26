"""
Garden Analytics Platform - Advanced OOP Demonstration.

This module demonstrates complex data relationships, nested components,
inheritance chains, and different types of methods in Python.
"""
from typing import List, Dict, Any
from abc import ABC, abstractmethod


# Utility functions (module-level functions that don't need specific data)
def validate_plant_height(height: int) -> bool:
    """
    Utility function to validate plant height.
    
    Args:
        height: Height to validate in cm
        
    Returns:
        True if height is valid (positive), False otherwise
    """
    return height > 0


def calculate_growth_rate(initial: int, current: int, days: int) -> float:
    """
    Calculate growth rate per day.
    
    Args:
        initial: Initial height in cm
        current: Current height in cm  
        days: Number of days
        
    Returns:
        Growth rate in cm per day
    """
    if days <= 0:
        return 0.0
    return (current - initial) / days


# Base Plant class - foundation of our inheritance chain
class Plant:
    """
    Base plant class - foundation of our inheritance hierarchy.
    
    Attributes:
        name (str): Plant name
        height (int): Plant height in cm
        age (int): Plant age in days
        initial_height (int): Starting height for growth calculations
    """
    
    def __init__(self, name: str, height: int, age: int = 0) -> None:
        """Initialize a basic plant."""
        self.name = name
        self.height = height
        self.age = age
        self.initial_height = height
        
    def grow(self) -> None:
        """Make the plant grow 1cm."""
        self.height += 1
        
    def get_info(self) -> str:
        """Get basic plant information."""
        return f"{self.name}: {self.height}cm"
        
    def __str__(self) -> str:
        """String representation of the plant."""
        return self.get_info()


# Second level in inheritance chain
class FloweringPlant(Plant):
    """
    Flowering plant that extends basic Plant functionality.
    
    Adds flower-specific attributes and methods.
    """
    
    def __init__(self, name: str, height: int, flower_color: str, 
                 age: int = 0) -> None:
        """Initialize a flowering plant."""
        super().__init__(name, height, age)
        self.flower_color = flower_color
        self.is_blooming = False
        
    def bloom(self) -> None:
        """Make the flower bloom."""
        self.is_blooming = True
        
    def get_info(self) -> str:
        """Get flowering plant information."""
        bloom_status = "(blooming)" if self.is_blooming else "(not blooming)"
        return f"{self.name}: {self.height}cm, {self.flower_color} flowers {bloom_status}"


# Third level in inheritance chain - specialized prize flowers
class PrizeFlower(FloweringPlant):
    """
    Prize-winning flower - most specialized plant type.
    
    Extends FloweringPlant with competition scoring.
    """
    
    def __init__(self, name: str, height: int, flower_color: str, 
                 prize_points: int = 0, age: int = 0) -> None:
        """Initialize a prize flower."""
        super().__init__(name, height, flower_color, age)
        self.prize_points = prize_points
        
    def award_points(self, points: int) -> None:
        """Award prize points to the flower."""
        self.prize_points += points
        
    def get_info(self) -> str:
        """Get prize flower information."""
        base_info = super().get_info()
        return f"{base_info}, Prize points: {self.prize_points}"


# Garden class to manage individual gardens
class Garden:
    """
    Individual garden that contains plants and tracks statistics.
    
    Each garden belongs to an owner and maintains its plant collection.
    """
    
    def __init__(self, owner_name: str) -> None:
        """Initialize a garden with an owner."""
        self.owner_name = owner_name
        self.plants: List[Plant] = []
        self.total_growth = 0
        
    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden."""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")
        
    def grow_all_plants(self) -> None:
        """Make all plants in the garden grow."""
        print(f"{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            initial_height = plant.height
            plant.grow()
            growth = plant.height - initial_height
            self.total_growth += growth
            print(f"{plant.name} grew {growth}cm")
            
    def get_plant_count_by_type(self) -> Dict[str, int]:
        """Get count of plants by type."""
        counts = {"regular": 0, "flowering": 0, "prize flowers": 0}
        
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                counts["prize flowers"] += 1
            elif isinstance(plant, FloweringPlant):
                counts["flowering"] += 1
            else:
                counts["regular"] += 1
                
        return counts
        
    def calculate_garden_score(self) -> int:
        """Calculate total garden score based on plant heights and prizes."""
        total_score = 0
        for plant in self.plants:
            total_score += plant.height
            if isinstance(plant, PrizeFlower):
                total_score += plant.prize_points
        return total_score
        
    def generate_report(self) -> None:
        """Generate detailed garden report."""
        print(f"\n=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        
        for plant in self.plants:
            print(f"- {plant.get_info()}")
            
        type_counts = self.get_plant_count_by_type()
        print(f"Plants added: {len(self.plants)}, Total growth: {self.total_growth}cm")
        print(f"Plant types: {type_counts['regular']} regular, "
              f"{type_counts['flowering']} flowering, "
              f"{type_counts['prize flowers']} prize flowers")


class GardenManager:
    """
    Advanced Garden Management System.
    
    Manages multiple gardens and provides comprehensive analytics.
    Demonstrates nested classes, class methods, and static methods.
    """
    
    # Class variable to track total number of managers created
    total_managers_created = 0
    
    # Nested helper class for statistics calculations
    class GardenStats:
        """
        Nested statistics helper for calculating garden analytics.
        
        This helper is nested inside GardenManager because it's specifically
        designed to work with garden data and doesn't need to exist independently.
        """
        
        @staticmethod
        def calculate_average_height(plants: List[Plant]) -> float:
            """Calculate average plant height."""
            if not plants:
                return 0.0
            return sum(plant.height for plant in plants) / len(plants)
            
        @staticmethod
        def find_tallest_plant(plants: List[Plant]) -> Plant:
            """Find the tallest plant in a collection."""
            if not plants:
                return None
            return max(plants, key=lambda p: p.height)
            
        @staticmethod
        def count_blooming_flowers(plants: List[Plant]) -> int:
            """Count how many flowering plants are currently blooming."""
            count = 0
            for plant in plants:
                if isinstance(plant, FloweringPlant) and plant.is_blooming:
                    count += 1
            return count
            
        @staticmethod
        def calculate_total_prize_points(plants: List[Plant]) -> int:
            """Calculate total prize points across all plants."""
            total = 0
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    total += plant.prize_points
            return total
    
    def __init__(self, manager_name: str) -> None:
        """
        Initialize garden manager.
        
        Args:
            manager_name: Name of the person managing the gardens
        """
        self.manager_name = manager_name
        self.gardens: Dict[str, Garden] = {}
        
        # Increment class variable when instance is created
        GardenManager.total_managers_created += 1
        
    def add_garden(self, garden: Garden) -> None:
        """Add a garden to management."""
        self.gardens[garden.owner_name] = garden
        
    def get_garden(self, owner_name: str) -> Garden:
        """Get a garden by owner name."""
        return self.gardens.get(owner_name)
        
    def add_plant_to_garden(self, owner_name: str, plant: Plant) -> bool:
        """
        Add a plant to a specific garden.
        
        Returns:
            True if successful, False if garden doesn't exist
        """
        garden = self.get_garden(owner_name)
        if garden:
            garden.add_plant(plant)
            return True
        return False
        
    def calculate_all_garden_scores(self) -> Dict[str, int]:
        """Calculate scores for all managed gardens."""
        scores = {}
        for owner_name, garden in self.gardens.items():
            scores[owner_name] = garden.calculate_garden_score()
        return scores
        
    def get_comprehensive_analytics(self) -> Dict[str, Any]:
        """
        Get comprehensive analytics using nested GardenStats helper.
        
        Returns:
            Dictionary with various statistics
        """
        all_plants = []
        for garden in self.gardens.values():
            all_plants.extend(garden.plants)
            
        return {
            'total_plants': len(all_plants),
            'average_height': self.GardenStats.calculate_average_height(all_plants),
            'tallest_plant': self.GardenStats.find_tallest_plant(all_plants),
            'blooming_flowers': self.GardenStats.count_blooming_flowers(all_plants),
            'total_prize_points': self.GardenStats.calculate_total_prize_points(all_plants),
            'total_gardens': len(self.gardens)
        }
        
    @classmethod
    def create_garden_network(cls, manager_names: List[str]) -> List['GardenManager']:
        """
        Class method to create a network of garden managers.
        
        This method works on the GardenManager class itself, not on instances.
        It's useful for setting up multiple managers at once.
        
        Args:
            manager_names: List of names for new managers
            
        Returns:
            List of GardenManager instances
        """
        managers = []
        for name in manager_names:
            manager = cls(name)
            managers.append(manager)
            print(f"Created garden manager: {name}")
        return managers
        
    @staticmethod
    def validate_plant_compatibility(plant1: Plant, plant2: Plant) -> bool:
        """
        Static method - utility function that belongs to the class conceptually
        but doesn't need class or instance data.
        
        Check if two plants are compatible for the same garden.
        This is a utility that relates to plants but doesn't need specific
        garden or manager instance data.
        """
        # Simple compatibility check - same type plants are compatible
        return type(plant1) == type(plant2)
        
    @classmethod
    def get_total_managers(cls) -> int:
        """Class method to get total number of managers created."""
        return cls.total_managers_created
        
    def run_analytics_demo(self) -> None:
        """Run a comprehensive demonstration of the analytics system."""
        print("=== Garden Management System Demo ===")
        
        # Create gardens and add them to management
        alice_garden = Garden("Alice")
        bob_garden = Garden("Bob")
        
        self.add_garden(alice_garden)
        self.add_garden(bob_garden)
        
        # Create different types of plants
        oak_tree = Plant("Oak Tree", 100, 365)
        rose = FloweringPlant("Rose", 25, "red", 30)
        sunflower = PrizeFlower("Sunflower", 50, "yellow", 10, 45)
        
        # Add plants to Alice's garden
        alice_garden.add_plant(oak_tree)
        alice_garden.add_plant(rose)
        alice_garden.add_plant(sunflower)
        
        # Make flowers bloom
        rose.bloom()
        sunflower.bloom()
        
        # Add a plant to Bob's garden
        bob_garden.add_plant(Plant("Maple Tree", 80, 200))
        bob_garden.add_plant(FloweringPlant("Daisy", 12, "white", 15))
        
        # Grow all plants
        alice_garden.grow_all_plants()
        
        # Generate reports
        alice_garden.generate_report()
        
        # Test height validation utility
        print(f"Height validation test: {validate_plant_height(oak_tree.height)}")
        
        # Show garden scores
        scores = self.calculate_all_garden_scores()
        score_parts = [f"{name}: {score}" for name, score in scores.items()]
        print(f"Garden scores - {', '.join(score_parts)}")
        
        # Show total managers
        print(f"Total gardens managed: {len(self.gardens)}")


def ft_garden_analytics() -> None:
    """
    Main function to demonstrate the garden analytics platform.
    
    This function showcases all the advanced OOP concepts:
    - Inheritance chains (Plant → FloweringPlant → PrizeFlower)
    - Nested classes (GardenStats inside GardenManager)
    - Different method types (instance, class, static)
    - Complex data relationships and analytics
    """
    # Create a garden manager
    manager = GardenManager("Master Gardener")
    
    # Run the comprehensive demo
    manager.run_analytics_demo()
    
    print(f"\nTotal managers created: {GardenManager.get_total_managers()}")


if __name__ == "__main__":
    ft_garden_analytics()
