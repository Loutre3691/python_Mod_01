class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.__height = 0
        self.set_height(height)

    def get_height(self) -> int:
        return self.__height

    def set_height(self, height) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm"
                  f" \033[0;31m[REJECTED]\033[0m\nSecurity: Negative height"
                  f" rejected\n")
        else:
            self.__height = height

    def validate_height(self):
        return self.__height >= 0


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        super().__init__(name, height, color)
        self.prize_points = prize

    def total_prize(self) -> int:
        return self.prize_points


class Garden:
    def __init__(self, name: str) -> None:
        self.name = name
        self.plants = [
        ]
# Initializes a Garden with a name and an empty list of plants

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
# Adds a Plant object to the garden's plant list

    def grew_plant(self, grew: int) -> None:
        print(f"\n{self.name} is helping all plants grow...")
        for plant in self.plants:
            print(f"{plant.name} grew {grew}cm")
# Simulates growth for all plants in the garden and prints how much each grew

    def total_plant_added(self) -> int:
        total = 0
        for plant in self.plants:
            total += 1
        return total
# Returns the total number of plants added to this garden


class GardenManager:
    def __init__(self) -> None:
        self.gardens = [
        ]

    def add_garden(self, name: str) -> None:
        garden = Garden(name)
        self.gardens.append(garden)
# Creates a new Garden with the given name and adds it to the manager's
# garden list

    def add_garden_plant(self, name: str, plant: Plant) -> None:
        garden = self.get_garden(name)
        garden.add_plant(plant)
        print(f"Added {plant.name} to {garden.name}'s garden")
# Finds the specified garden and adds the given Plant object to it

    def get_garden(self, name: str) -> Garden:
        for g in self.gardens:
            if g.name == name:
                return g
        print("not garden valid")
# Retrieves a Garden object by name from the manager's list,
# prints a message if not found

    def info_garden(self, garden: Garden) -> None:

        print(f"\033[1;36m=== {garden.name}' Garden Report ===\033[0m\n"
              f"Plants in garden:")
        for plant in garden.plants:
            if isinstance(plant, PrizeFlower):
                print(f"- {plant.name}: {plant.get_height()}cm, {plant.color} "
                      f"flower (blooming), Prize points: {plant.prize_points}")
            elif isinstance(plant, FloweringPlant):
                print(f"- {plant.name}: {plant.get_height()}cm, {plant.color} "
                      f"flower (blooming)")
            else:
                print(f"- {plant.name}: {plant.get_height()}cm")
# Prints a detailed report of all plants in the given garden, including
# type, height, and prize points if applicable

    def grow_plants(self, grew: int) -> None:
        total_len_plant = 0
        total_growing = 0
        for garden in self.gardens:
            total_len_plant += garden.total_plant_added()
            for plant in garden.plants:
                total_growing += grew
        print(f"Plants added: {total_len_plant}, Total growth: {total_growing}"
              f"cm")
# Calculates and prints total number of plants and their cumulative growth
# across all gardens

    def types_plants(self) -> None:
        regular = 0
        flowering = 0
        prize = 0
        for garden in self.gardens:
            for plant in garden.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
        print(f"Plant types: {regular} regular, {flowering} flowering, "
              f" {prize} Prize flowers")
# Counts the number of each plant type (regular, flowering, PrizeFlower)
# across all gardens

    class GardenStats:

        @staticmethod
        def validation_height(plant: Plant) -> None:
            print("Height validation test:", plant.validate_height())
# validation height with booleen

        @staticmethod
        def garden_score(manager: "GardenManager") -> None:
            print("Garden scores - ", end="")

            for garden in manager.gardens:
                total = sum(
                    plant.total_prize()
                    for plant in garden.plants
                    if isinstance(plant, PrizeFlower)
                )
                print(f"{garden.name}: {total} ", end="")
# genetation expression (for), automatik calculation of the prize
# with sum()

        @staticmethod
        def total_gardens_managed(manager: "GardenManager") -> None:
            total = 0
            for garden in manager.gardens:
                total += 1
            print(f"Total gardens managed: {total}")
# Total gardens calculate

    @classmethod
    def create_garden_network(cls):
        garden_manager = cls()
        garden_manager.add_garden("Alice")
        garden_manager.add_garden("Bob")
        return garden_manager
# Creates a GardenManager with two default gardens: Alice and Bob


if __name__ == "__main__":
    print("\033[1;36m=== Garden Management System Demo ===\033[0m\n")
    manager = GardenManager.create_garden_network()

    beech = Plant("Beech", 380)
    manager.add_garden_plant("Alice", beech)

    rose = FloweringPlant("Rose", 26, "red")
    manager.add_garden_plant("Alice", rose)

    tulip = PrizeFlower("Tulip", 20, "white", 92)
    manager.add_garden_plant("Bob", tulip)

    grew = 1
    for garden in manager.gardens:
        garden.grew_plant(grew)
    print("")

    for garden in manager.gardens:
        manager.info_garden(garden)
        print("")

    manager.grow_plants(grew)
    manager.types_plants()
    print("")

    stats = GardenManager.GardenStats()
    stats.validation_height(beech)
    stats.garden_score(manager)
    print("")
    stats.total_gardens_managed(manager)

# Demo of the Garden Management System:
# - Creates a garden network with Alice's and Bob's gardens
# - Adds different types of plants to each garden
# - Simulates plant growth
# - Prints detailed garden reports, overall growth, plant counts, and garden
# scores
# Note: Some GardenStats features are placeholders for future implementation
