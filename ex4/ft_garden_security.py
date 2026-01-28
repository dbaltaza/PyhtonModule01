
class SecurePlant:

    def __init__(self, name: str, h: int, a: int) -> None:
        self._name = name
        print(f"Plant created: {n}")
        self.set_height(h)
        self.set_age(a)

    def set_height(self, h: int) -> int:
        if h >= 0:
            self._height = h
            print(f"Height updated: {h}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {h}cm [REJECTED]")
            print("Security: Negative height rejected")

    def get_height(self) -> int:
        return self._height

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
            print(f"Age updated: {age} days [OK]\n")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_age(self) -> int:
        return self._age

    def get_name(self) -> str:
        return self._name

    def __str__(self) -> str:
        return f"{self._name} ({self._height}cm, {self._age} days)"


def ft_garden_security() -> None:

    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, 30)
    plant.set_height(-5)
    print(f"\nCurrent plant: {plant}")


if __name__ == "__main__":
    ft_garden_security()
