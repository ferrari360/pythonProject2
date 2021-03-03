class Hero():
#родительский класс Parent class
    """Class to create hero for our game"""
    def __init__(self, name,  level, race):
       "" "initiate our hero"""
       self.name = name
       self.level = level
       self.race = race
       self.health = 100

    def show_hero(self):
        """print all parameters of this HERO"""
        discription = (self.name + " Level is: " + str(self.level) + " race is " + self.race + " health is "+ str(self.health)).title()
        print(discription)

    def level_up(self):
        """Upgrade level of hero"""
        self.level += 1

    def move(self):
        """Start moving hero"""
        print("Hero"+ self.name + "start moving...")

    def set_health(self, new_health):
        "edit health"
        self.health = new_health

# Child class===========================================================================
class SuperHero(Hero):
    "Class to create super hero"
    def __init__(self, name,  level, race, magiclevel):
        "initiate our hero"
        super().__init__(name,  level, race)
        self.magiclevel = magiclevel
        self.magic  = 100

    def makemagic(self):
        'use magic'
        self.magic -= 10

    def show_hero(self):
        """print all parameters of this HERO"""
        discription = (self.name + " Level is: " + str(self.level) + " race is " + self.race + " health is " + str(self.health)+" magic is " + str(self.magic)).title()
        print(discription)
