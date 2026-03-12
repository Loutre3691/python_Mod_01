class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = age

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.plant_age += 1

    def get_info(self) -> None:
        return f"{self.name}: {self.height} cm, {self.plant_age} days old"

    def ft_plant_growth(self) -> None:

        start_height = self.height

        print("\033[1;35m=== Day 1 ===\033[0m")
        print(self.get_info())

        for day in range(6):
            self.grow()
            self.age()

        print(f"\033[1;35m=== Day {day+2} ===\033[0m")
        print(self.get_info())

        growth = self.height - start_height
        print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    rose.ft_plant_growth()
