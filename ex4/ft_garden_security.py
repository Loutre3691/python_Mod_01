class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)
        print(f"Plant created: {self.name}"
              f"\nHeight update: {self.__height}cm \033[1;92m[OK]\033[0m\n"
              f"Age updated: {self.__age} days \033[1;92m[OK]\033[0m\n")
# initialiser l attribut prive a 0 au cas ou si la valeur dans objet nest
# pas valide, puis appeler set_... pour verifier

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


if __name__ == "__main__":
    print("\033[1;36m\n=== Garden Security System ===\033[0m\n")
    rose = SecurePlant("Rose", 25, 20)
    rose.set_age(12)
    rose.set_height(21)
    print(f"\033[1;92mCurrent plant:\033[0m {rose.name} ({rose.get_height()}"
          f"cm, {rose.get_age()} days)")
