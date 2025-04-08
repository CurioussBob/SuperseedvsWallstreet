class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.occupied = False
        self.plant = None

    def place_plant(self, plant):
        if not self.occupied:
            self.plant = plant
            self.occupied = True

    def remove_plant(self):
        self.plant = None
        self.occupied = False

    def draw(self, screen):
        # Draw tile
        tile_color = (200, 200, 200) if not self.occupied else (150, 150, 150)
        pygame.draw.rect(screen, tile_color, (self.x, self.y, 100, 100))
        
        if self.occupied:
            self.plant.draw(screen)

class Board:
    def __init__(self):
        self.tiles = []
        self.setup_board()

    def setup_board(self):
        for row in range(5):
            for col in range(9):
                tile = Tile(col * 100, row * 100)
                self.tiles.append(tile)

    def draw(self, screen):
        for tile in self.tiles:
            tile.draw(screen)

    def get_tile_at(self, x, y):
        for tile in self.tiles:
            if tile.x <= x <= tile.x + 100 and tile.y <= y <= tile.y + 100:
                return tile
        return None
