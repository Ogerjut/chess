import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self) :
        super().__init__()
        self.sprite_sheet = pygame.image.load('pieces_sprite.png').convert_alpha()
        self.sprite_sheet = pygame.transform.scale(self.sprite_sheet, (384, 128))
        
    def get_image(self, x, y): 
        image= pygame.Surface([64, 64], pygame.SRCALPHA)
        image.blit(self.sprite_sheet, (0,0),(x,y, 64, 64)) 
        return image
        
class Piece(Sprite) : 
    def __init__(self, x, y, tile, color):
        super().__init__()
        self.image = self.get_image(x,y)
        self.rect = self.image.get_rect()
        self.tile = tile
        self.color = color

        # donner le sprite en arg et non héritage

    def move(self): 
        pass
        
class King(Piece):
    def __init__(self, x, y, tile, color ):
        super().__init__(x, y, tile, color)
        self.chess = False
        self.mat = False
        
class Queen(Piece):
    def __init__(self, x, y, tile, color ):
        super().__init__(x, y, tile, color)
        
class Knight(Piece):
    def __init__(self, x, y, tile, color ):
        super().__init__(x, y, tile, color)
        
class Rook(Piece):
    def __init__(self, x, y, tile, color ):
        super().__init__(x, y, tile, color)
        
class Bishop(Piece):
    def __init__(self, x, y, tile , color):
        super().__init__(x, y, tile, color)
        
class Pawn(Piece):
    def __init__(self, x, y, tile, color ):
        super().__init__(x, y, tile, color)
        self.first_move = True
        