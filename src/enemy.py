import pygame

class Enemy:
    def __init__(self, name, power_level, speed):
        self.name = name
        self.power_level = power_level
        self.health = 100
        self.speed = speed  # Speed of movement (pixels per frame)
        self.x = 900  # Start at the right side of the screen
        self.y = random.randint(0, 400)  # Random vertical position
        self.animation_state = 'idle'  # Animation states for enemies

    def move(self):
        self.x -= self.speed  # Move the enemy leftwards

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()

    def die(self):
        self.animation_state = 'die'
        print(f"{self.name} has died!")

    def draw(self, screen):
        if self.animation_state == 'die':
            # Render death animation (for simplicity, we use a static image here)
            screen.blit(ENEMY_IMAGES[self.name], (self.x, self.y))
        else:
            # Render normal animation
            screen.blit(ENEMY_IMAGES[self.name], (self.x, self.y))
