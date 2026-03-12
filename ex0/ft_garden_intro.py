def ft_garden_intro() -> None:
    name = (input("Plant name: "))
    height = int(input("height plant: "))
    age = int(input("age plant: "))
    print("\033[1;32m\n=== Welcome to My Garden ===\033[0m")
    print(f"Plant: {name}\nHeight: {height} cm \nAge: {age} days")
    print("\033[1;32m=== End of Program ===\033[0m")


if __name__ == "__main__":
    ft_garden_intro()
