import pygame
from constantes import *
from auxiliar import Auxiliar


class Trampa:
    def __init__(self,x,y) -> None:
        self.sprite = Auxiliar.getSurfaceFromSpriteSheet(r"recursos\images\trap\trampa.png",1,1,scale=1)[0]
        self.image = self.sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def draw(self,screen):
        if(DEBUG): 
            pygame.draw.rect(screen,C_RED, self.rect)     
            #pygame.draw.rect(screen,GREEN, self.rect_ground_col)
        screen.blit(self.image,self.rect)

    def collide(self,player, Trampa_list, Trampa):
        if self.rect.colliderect(player.rect):
            player.discount_live()
            Trampa_list.remove(Trampa)  
            

    def update(self, player, Trampa_list, Trampa):
        self.collide(player, Trampa_list, Trampa)
    

