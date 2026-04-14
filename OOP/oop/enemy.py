import random

class Enemy:
    def __init__(self, type_of_enemy,health_points,attack_damage):
        self.__type_of_enemy = type_of_enemy   # these are attributes of class enemy.
        self.health_points = health_points
        self.attack_damage = attack_damage
    
    def get_type_of_enemy(self):
        return self.__type_of_enemy
    
    def talk(self):
        print(f"I am a {self.__type_of_enemy} be prepared to fight.")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closure to you.")

    def attack(self):
        print(f"{self.__type_of_enemy} attacks you for {self.attack_damage} damage points.")

    def special_attack(self):
        print("Enemy has no special attack.")