
class Plant:
    def __init__(self, n: str, h: int, a: int) -> None:
        self.name = n
        self.height = h
        self.age = a


def ft_plant_factory() -> None:
    plants = (
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Catcus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    )

    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)"),
    print("\nTotal plants created:", len(plants))


if __name__ == "__main__":
    ft_plant_factory()
