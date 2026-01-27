
class Plant:
    def __init__(self, n: str, h: int, a: int) -> None:
        self.name = n
        self.height = h
        self.age = a


def grow(h: int, d: int) -> int:
    return h + d


def age(a: int, d: int) -> int:
    return a + d


def ft_plant_growth() -> None:
    plants = Plant("Rose", 25, 30)
    days = 1
    print(f"=== Day {days} ===")
    print(f"{plants.name}:", f"{plants.height}cm,", f"{plants.age} days old")

    while days < 6:
        days += 1
    print(f"=== Day {days + 1} ===")
    print(
        f"{plants.name}: {grow(plants.height, days)}cm, "
        f"{age(plants.age, days)} days old"
    )
    print("Growth this week: " f"+{days}cm")


if __name__ == "__main__":
    ft_plant_growth()
