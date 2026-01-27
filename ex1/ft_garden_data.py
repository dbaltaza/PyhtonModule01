
class Plant:
    def __init__(self, n: str, h: int, a: int) -> None:
        self.name = n
        self.height = h
        self.age = a


def ft_garden_data() -> None:
    plants = (
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    )

    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(f"{plant.name}:", f"{plant.height}cm,", f"{plant.age} days old")


if __name__ == "__main__":
    ft_garden_data()
