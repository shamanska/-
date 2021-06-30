

class Hero:

    def __init__(self, rank, health, power):
        self.__rank = rank
        self.__health = health
        self.__power = power

    def fight(self, other_hero):
        other_hero.health = other_hero.health - self.__power

    def heal(self, other_hero):
        if self.__health < 50:
            self.__health = self.__health + 2
        if other_hero.health < 50:
            other_hero.health = other_hero.health + 5

    def get_rank(self):
        return self.__rank

    def set_rank(self, value):
        self.__rank = int(value)
        if value > 3:
            self.__rank = 3
        if value < 1:
            self.__rank = 1

    rank = property(get_rank, set_rank)

    def get_health(self):
        return self.__health

    def set_health(self, value):
        self.__health = value
        if value < 0:
            value = 0
        if value > 100:
            value = 100

    health = property(get_health, set_health)

    def get_power(self):
        return self.__power

    def set_power(self, value):
        self.__power = value
        if value < 0:
            value = 0
        if value > 100:
            value = 100

    power = property(get_power, set_power)

hero_1 = Hero(rank=1, health=78, power=10)
hero_2 = Hero(rank=3, health=56, power=13)

hero_1.fight(hero_2)
hero_2.heal(hero_2)
hero_2.fight(hero_1)
hero_1.heal(hero_1)

print(hero_2.health)
print(hero_1.health)