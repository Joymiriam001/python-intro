class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def displayinfo(self):
        return f"I am {self.name}, {self.age}, from {self.city}"

class Player(Person):
    def __init__(self, name, age, city, level):
        super().__init__(name, age, city)
        self.level = level

# Create an instance of the Player class
player_instance = Player("Denver", 24, "New York", 11)

# Print player information
print(f"playername: {player_instance.name}, playerage: {player_instance.age}, playercity: {player_instance.city}, playerlevel: {player_instance.level}")
