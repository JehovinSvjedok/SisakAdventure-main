import pygame
import random

def add_attributes(attack, health, heal_amount):
    def decorator(cls):
        cls.attack = attack
        cls.health = health
        cls.heal_amount = heal_amount
        return cls
    return decorator

class Enemy:
    def __init__(self, x, y, speed, image_path, size, health=None):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = self.load_image(image_path, size)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.health = health if health is not None else self.__class__.health

    def load_image(self, path, size):
        image = pygame.image.load(path)
        return pygame.transform.scale(image, size)

    def update(self):
        pass  # No movement for enemies

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def take_damage(self, amount):
        self.health -= amount
        return self.health <= 0  # Return whether the enemy is slain

    def heal(self, amount):
        self.health += amount  # Heal the enemy

@add_attributes(attack=5, health=50, heal_amount=10)
class BossEnemy(Enemy):
    type = "boss"

    def __init__(self, x, y, speed, image_path, size, health=None):
        super().__init__(x, y, speed, image_path, size, health)
        self.attack = self.__class__.attack  # Ensure attack attribute is set
        self.heal_amount = self.__class__.heal_amount  # Ensure heal_amount attribute is set
        self.is_boss = True  # Mark this enemy as a boss

    def update(self):
        # Special boss behavior (e.g., different movement, attack, etc.)
        pass

@add_attributes(attack=2, health=10, heal_amount=3)
class EnemyType1(Enemy):
    type = "type1"

    def update(self):
        # Implement movement or behavior for EnemyType1
        pass

@add_attributes(attack=3, health=15, heal_amount=4)
class EnemyType2(Enemy):
    type = "type2"

    def update(self):
        # Implement movement or behavior for EnemyType2
        pass

@add_attributes(attack=4, health=20, heal_amount=5)
class EnemyType3(Enemy):
    type = "type3"

    def update(self):
        # Implement movement or behavior for EnemyType3
        pass

@add_attributes(attack=5, health=25, heal_amount=6)
class EnemyType4(Enemy):
    type = "type4"

    def update(self):
        # Implement movement or behavior for EnemyType4
        pass

@add_attributes(attack=6, health=100, heal_amount=5)
class GoblinBoss(BossEnemy):
    type = "Goblin_boss"

    def update(self):
        # Implement movement or behavior for GoblinBoss
        pass

@add_attributes(attack=8, health=150, heal_amount=5)
class SkeletonDragon(BossEnemy):
    type = "skeleton_dragon"

    def update(self):
        # Implement movement or behavior for SkeletonDragon
        pass

@add_attributes(attack=10, health=200, heal_amount=5)
class King(BossEnemy):
    type = "King"

    def update(self):
        # Implement movement or behavior for King
        pass

@add_attributes(attack=15, health=250, heal_amount=10)
class DemonCerberus(BossEnemy):
    type = "demon_cerberus"

    def update(self):
        # Implement movement or behavior for DemonCerberus
        pass

class EnemyFactory:
    # Mapping normal enemy types to their respective parameters
    NORMAL_ENEMY_DATA = {
        1: ("my-pygame-game/src/assets/goblin_koplje.png", (200, 270), EnemyType1),
        2: ("my-pygame-game/src/assets/goblin.png", (200, 270), EnemyType1),
        3: ("my-pygame-game/src/assets/spider.png", (200, 270), EnemyType1),
        4: ("my-pygame-game/src/assets/skeleton_spear.png", (200, 270), EnemyType2),  # Add new enemy types for level 2
        5: ("my-pygame-game/src/assets/skeleton_bow.png", (200, 270), EnemyType2),
        6: ("my-pygame-game/src/assets/mali_skeleton.png", (200, 270), EnemyType2),  # Add new enemy types for level 3
        7: ("my-pygame-game/src/assets/knight_sword.png", (200, 270), EnemyType3),
        8: ("my-pygame-game/src/assets/knight_spear.png", (200, 270), EnemyType3),
        9: ("my-pygame-game/src/assets/knight_hammer.png", (200, 270), EnemyType3),
        10: ("my-pygame-game/src/assets/demon_soldier.png", (200, 270), EnemyType4),   # Add new enemy types for level 4
        11: ("my-pygame-game/src/assets/demon_imp.png", (200, 270), EnemyType4),
        12: ("my-pygame-game/src/assets/demon_hellhound.png", (200, 270), EnemyType4)
    }

    # Mapping boss enemy types to their respective parameters
    BOSS_ENEMY_DATA = {
        "Goblin_boss": ("my-pygame-game/src/assets/hobogoblin.png", (400, 400), GoblinBoss),
        "skeleton_dragon": ("my-pygame-game/src/assets/skeleton_dragon.png", (400, 400), SkeletonDragon),
        "King": ("my-pygame-game/src/assets/king.png", (400, 400), King),
        "demon_cerberus": ("my-pygame-game/src/assets/demon_cerberus.png", (400, 400), DemonCerberus)
    }

    @staticmethod
    def create_enemy(enemy_type, x, y, speed):
        if enemy_type in EnemyFactory.NORMAL_ENEMY_DATA:
            image_path, size, enemy_class = EnemyFactory.NORMAL_ENEMY_DATA[enemy_type]
            return enemy_class(x, y, speed, image_path, size)
        elif enemy_type in EnemyFactory.BOSS_ENEMY_DATA:
            image_path, size, enemy_class = EnemyFactory.BOSS_ENEMY_DATA[enemy_type]
            return enemy_class(x, y, speed, image_path, size)
        else:
            raise ValueError("Unknown enemy type")

