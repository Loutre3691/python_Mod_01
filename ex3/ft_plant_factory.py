class Plant:
    def __init__(self, name: str, start_height: int, start_age: int) -> None:
        self.name = name
        self.height = start_height
        self.age = start_age

    def ft_plant_factory(self) -> None:
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    plants = [
        Plant("Rose", 2, 3),
        Plant("Tomato", 10, 2),
        Plant("Banzai", 120, 20),
        Plant("Iris", 20, 1),
        Plant("Sunflower", 80, 6)
    ]

    print("\033[1;32m=== Plant Factory Output ===\033[0m")
    for plant in plants:
        plant.ft_plant_factory()
    print(f"\nTotal plants created: {len(plants)}")
