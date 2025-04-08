class ResourceManager:
    def __init__(self):
        self.seed_tokens = 0
        self.shield_bar = 0

    def add_seed(self, amount):
        self.seed_tokens += amount

    def deduct_seed(self, amount):
        if self.seed_tokens >= amount:
            self.seed_tokens -= amount
            return True
        return False

    def increase_shield(self, amount):
        self.shield_bar += amount
        if self.shield_bar > 100:
            self.shield_bar = 100  # Max shield is 100

    def draw(self, screen):
        # Draw seed tokens and shield bar
        font = pygame.font.SysFont('Arial', 24)
        seed_text = font.render(f"Seeds: {self.seed_tokens}", True, (0, 0, 0))
        screen.blit(seed_text, (10, 10))

        pygame.draw.rect(screen, (0, 255, 0), (10, 40, self.shield_bar, 20))  # Draw shield bar
