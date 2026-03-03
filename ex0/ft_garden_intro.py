def ft_garden_intro() -> None:
    name = (input("Plant name: "))
    height = int(input("height plant: "))
    age = int(input("age plant: "))
    print("===Welcome to My Garden===")
    print(f"Plant: {name}\nHeight: {height} cm \nAge: {age} days")
    print("===End of Program===")


if __name__ == "__main__":
    ft_garden_intro()
