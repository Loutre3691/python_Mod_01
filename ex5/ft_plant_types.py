class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm"
                  f" \033[0;31m[REJECTED]\033[0m\nSecurity: Negative height"
                  f" rejected\n")
        else:
            self.__height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age} days "
                  f"\033[0;31m[REJECTED]\033[0m\nSecurity: Negative age"
                  f" rejected\n")
        else:
            self.__age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        if self.get_age() > 20:
            print(f"{self.name} is blooming beautifully!\n")
        else:
            print(f"{self.name} is not in bloom\n")

    def get_info(self) -> str:
        return (
            f"{self.name} \033[0;35m(Flower)\033[0m: {self.get_height()}cm, "
            f" {self.get_age()} days, {self.color} color"
                )


class Tree(Plant):
    def __init__(self, name: str, height: int,
                 age: int, diameter: int) -> None:
        super().__init__(name, height, age)
        self.__trunk_diameter = diameter

    def produce_shade(self) -> int:
        return round(31.2 * (self.get_height() / 100) *
                     (self.__trunk_diameter / 100))

    def get_info(self) -> str:
        square = self.produce_shade()
        return (
            f"{self.name} \033[0;32m(Tree)\033[0m: {self.get_height()}cm,  "
            f"{self.get_age()} days, {self.__trunk_diameter}cm diameter\n"
            f"{self.name} provides {square} square meters of shade\n"
        )


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = season

    def nutritional_value(self) -> str:
        if self.harvest_season == "summer":
            return f"{self.name} is rich in vitamin C\n"
        elif self.harvest_season == "winter":
            return f"{self.name} is rich in vitamin C\n"
        elif self.harvest_season == "autumn":
            return f"{self.name} is rich in vitamin A and C\n"
        else:
            return f"{self.name} is rich in vitamin B\n"

    def get_info(self) -> str:
        return (
            f"{self.name} \033[0;33m(Vegetable)\033[0m: {self.get_height()}cm,"
            f" {self.get_age()} days, {self.harvest_season} harvest"
        )


if __name__ == "__main__":
    print("\033[1;36m\n=== Garden Plant Types ===\033[0m\n")
    flowers = [
        Flower("Rose", 25, 21, "red"),
        Flower("Tulip", 15, 1, "blue")
    ]
    trees = [
        Tree("Sakura", 500, 25, 50),
        Tree("Oak", 856, 129, 154)
    ]
    vegetables = [
        Vegetable("Tomato", 45, 10, "summer"),
        Vegetable("Carot", 10, 1, "autumn")
    ]
    for flower in flowers:
        print(flower.get_info())
        flower.bloom()

    for tree in trees:
        tree.produce_shade()
        print(tree.get_info())

    for vegetable in vegetables:
        print(vegetable.get_info())
        print(vegetable.nutritional_value())
