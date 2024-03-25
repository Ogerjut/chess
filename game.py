import pygame
from sprite import *

class Game(): 
    def __init__(self) :
        self.screen = pygame.display.set_mode((640,640))
        pygame.display.set_caption("Chess")  
        self.list_tiles = []
        self.board()
        self.list_pieces = []
        self.register_pieces()
        self.active_piece = None
        self.all_sprites = pygame.sprite.Group(self.list_pieces)
    
    def board(self):
        
        size = (8,8)
        px_tile = 64
        offset = 64
        for j in range (0,size[0]) : 
            for i in range(0, size[1]):
                self.tile_rect = pygame.rect.Rect(offset+ px_tile*i, offset+px_tile*j, px_tile, px_tile)
                if (i+j)%2 == 1 :
                    pygame.draw.rect(self.screen, "Brown", self.tile_rect, 0)
                else : pygame.draw.rect(self.screen, "White", self.tile_rect,0)
                pygame.draw.rect(self.screen, "Gold", self.tile_rect, 1)
                self.list_tiles.append(self.tile_rect)

        # for num, tiles in enumerate(self.list_tiles):
        #     print(f'Case : {num}, rect : {tiles} ')
        
    def register_pieces(self):
        self.dic_pieces = {}
        self.dic_pieces["kingw"] = King(0 ,0, 60, "white")
        self.dic_pieces["queenw"] = Queen(64 ,0, 59, "white")
        self.dic_pieces["bishopww"] = Bishop(128 ,0, 61, "white")
        self.dic_pieces["knightww"] = Knight(192 ,0, 57, "white")
        self.dic_pieces["bishopw"] = Bishop(128 ,0, 58, "white")
        self.dic_pieces["knightw"] = Knight(192 ,0, 62, "white")
        self.dic_pieces["rookww"] = Rook(256 ,0, 63, "white")
        self.dic_pieces["rookw"] = Rook(256 ,0, 56, "white")
        for i in range(0,8):
            self.dic_pieces[f"pawnw_{i}"] = Pawn(320,0, i+48, "white")
        self.dic_pieces["kingb"] = King(0 ,64, 4, "black")
        self.dic_pieces["queenb"] = Queen(64 ,64, 3, "black")
        self.dic_pieces["bishopbb"] = Bishop(128 ,64, 5, "black")
        self.dic_pieces["knightbb"] = Knight(192 ,64, 1, "black")
        self.dic_pieces["bishopb"] = Bishop(128 ,64, 2, "black")
        self.dic_pieces["knightb"] = Knight(192 ,64, 6, "black")
        self.dic_pieces["rookwb"] = Rook(256 ,64, 7, "black")
        self.dic_pieces["rookbw"] = Rook(256 ,64, 0, "black")
        for i in range(0,8):
            self.dic_pieces[f"pawnb_{i}"] = Pawn(320,64, i+8, "black")

        for piece in self.dic_pieces : 
            self.list_pieces.append(self.dic_pieces[piece])
            
        for num, tile in enumerate(self.list_tiles):
            for piece in self.list_pieces :
                if num == piece.tile :
                    piece.rect = tile
        
    def update(self):
        self.screen.fill("Black")
        self.board()
        self.all_sprites.draw(self.screen)
        self.all_sprites.update()   
        
    def run(self): 
        run = True
        clock = pygame.time.Clock()
        while run :
            
            self.update()
    
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for num, piece in enumerate(self.list_pieces):
                            if piece.rect.collidepoint(event.pos):
                                self.active_piece = num
             
                if event.type == pygame.MOUSEMOTION:
                    if self.active_piece != None:
                        self.list_pieces[self.active_piece].rect.move_ip(event.rel)
                                                                
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 :
                        for num, tile in enumerate(self.list_tiles):
                            if tile.collidepoint(event.pos):
                                destination_case = num
                                for piece in self.list_pieces : 
                                    if piece.tile == destination_case :
                                        piece.rect = tile
                                        self.active_piece = None
                                   
            
            clock.tick(60)
        pygame.quit()