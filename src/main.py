import pygame
import random
from board import Board
from plant import Plant
from enemy import Enemy
from resources import ResourceManager
from game_states import MENU, GAMEPLAY, GAME_OVER, current_state

# Initialize pygame
pygame.init()

# Define screen size and setup
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create the game objects
board = Board()
resource_manager = ResourceManager()

# Main Game Loop
def game_loop():
    global current_state
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                tile = board.get_tile_at(mouse_x, mouse_y)
                if tile and not tile.occupied:
                    place_plant(tile)

        # Update game logic
        if current_state == MENU:
            display_menu()
        elif current_state == GAMEPLAY:
            update_gameplay()
        elif current_state == GAME_OVER:
            display_game_over()

        # Drawing everything
        screen.fill((255, 255, 255))  # Clear screen to white

        if current_state == GAMEPLAY:
            # Draw the board and the plants
            board.draw(screen)
            resource_manager.draw(screen)

        pygame.display.flip()
        pygame.time.Clock().tick(60)

# Place a plant on the selected tile
def place_plant(tile):
    # Assume we place a low power plant here as an example
    if resource_manager.deduct_seed(10):  # Cost of a plant (example: 10 Seed tokens)
        new_plant = Plant("Plant1", "low", 10)  # Using "Plant1" as the plant name
        tile.place_plant(new_plant)

# Update the gameplay elements (plants, enemies, etc.)
def update_gameplay():
    # Update plants and enemies
    for tile in board.tiles:
        if tile.occupied:
            plant = tile.plant
            plant.update()

    # Spawn and move enemies
    spawn_enemy()
    for enemy in enemies:
        enemy.move()
        enemy.draw(screen)
        if enemy.x <= 0:  # Enemy reached the Seed Bank
            resource_manager.shield_bar -= 5  # Example of shield damage
            if resource_manager.shield_bar <= 0:
                game_over()

    # Example collision detection between projectiles and enemies
    for enemy in enemies:
        if enemy.health <= 0:
            enemies.remove(enemy)
            resource_manager.increase_shield(2)  # Reward shield points for killing an enemy

# Spawn an enemy
enemies = []
def spawn_enemy():
    # Randomly decide the type of enemy to spawn
    enemy_type = random.choice(["Enemy1", "Enemy2", "Enemy3"])
    new_enemy = Enemy(enemy_type, "low", random.randint(1, 3))  # Random speed for enemies
    enemies.append(new_enemy)

# Display the Menu screen
def display_menu():
    font = pygame.font.SysFont('Arial', 30)
    text = font.render("Seed vs Wall Street - Press Space to Start", True, (0, 0, 0))
    screen.blit(text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        global current_state
        current_state = GAMEPLAY

# Display Game Over screen
def display_game_over():
    font = pygame.font.SysFont('Arial', 30)
    text = font.render("Game Over - Press Space to Retry", True, (0, 0, 0))
    screen.blit(text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        global current_state
        current_state = MENU

# Start the game loop
if __name__ == "__main__":
    current_state = MENU  # Start at the menu
    game_loop()
