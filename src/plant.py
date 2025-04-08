import pygame

class Plant:
    def __init__(self, name, power_level, cost):
        self.name = name
        self.power_level = power_level
        self.cost = cost
        self.health = 100
        self.attack_timer = 0  # Timer for attacks to avoid rapid firing
        self.x = 0
        self.y = 0
        self.animation_state = 'idle'  # State for animations (e.g., idle, attack)
        
    def attack(self, enemy):
        if self.attack_timer == 0:  # Only attack if the timer is zero
            self.attack_timer = 60  # Reset attack timer (attack every 60 frames)
            # Logic to fire a token (Ethereum or Seed Token)
            print(f"{self.name} attacks {enemy.name}!")

    def update(self):
        if self.attack_timer > 0:
            self.attack_timer -= 1
    
    def draw(self, screen):
        # Drawing different animations based on the state
        if self.animation_state == 'attack':
            # Example of rendering an attack animation
            if self.power_level == 'low':
                screen.blit(PLANT_IMAGES[self.name]['attack'][0], (self.x, self.y))
            elif self.power_level == 'medium':
                screen.blit(PLANT_IMAGES[self.name]['attack'][1], (self.x, self.y))
            elif self.power_level == 'high':
                screen.blit(PLANT_IMAGES[self.name]['attack'][1], (self.x, self.y))
        else:
            # Render idle animation if not attacking
            screen.blit(PLANT_IMAGES[self.name]['attack'][0], (self.x, self.y))
            
    def move(self, x, y):
        self.x = x
        self.y = y
