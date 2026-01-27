
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


def ft_garden_intro() -> None:
    plant = Plant("Rose", 25, 30)

    print("== Welcome to my Garden ==")
    print("Name:", plant.name)
    print("Height:", f"{plant.height}cm")
    print("Age:", plant.age, "days")
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
