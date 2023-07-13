from player import *
from constantes import *
from auxiliar import Auxiliar
from botin import Loot

class Proyectile:
    def __init__(self, speed, x, y, direction, player_shoot=True):
        self.speed = speed
        self.direction = direction
        self.tiempo_transcurrido = 0
        self.player_shoot = player_shoot
        
        if player_shoot:
            self.sprite_left = Auxiliar.getSurfaceFromSpriteSheet("recursos/images/caracters/tropper/bullet/0.png",1,1,scale=2)[0]
            self.sprite_right = Auxiliar.getSurfaceFromSpriteSheet("recursos/images/caracters/tropper/bullet/1.png",1,1,scale=2)[0]
        else:
            self.sprite_left = Auxiliar.getSurfaceFromSpriteSheet("recursos/images/caracters/tropper/bullet/0.png",1,1,scale=2)[0]
            self.sprite_right = Auxiliar.getSurfaceFromSpriteSheet("recursos/images/caracters/tropper/bullet/1.png",1,1,scale=2)[0]
        
        self.image = self.sprite_right
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        if self.direction == DIRECTION_L:
            self.image = self.sprite_left
        screen.blit(self.image, self.rect)

    def update(self, delta_ms, enemy_list, platform_list, proyectile_list, proyectile, player, loot_list, boss):
        if self.direction == DIRECTION_L:
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        self.collide(delta_ms, enemy_list, platform_list, proyectile_list, proyectile, player, loot_list, boss)

    def collide(self, delta_ms, enemy_list, platform_list, proyectile_list, proyectile, player, loot_list, boss):
        if self.player_shoot:
            for enemy in enemy_list:
                if self.rect.colliderect(enemy.rect):
                    ENEMY_HURTED.play()
                    enemy_list.remove(enemy)
                    player.score += 100
                    loot = Loot(enemy.rect.x, enemy.rect.bottom, 15)
                    loot_list.append(loot) 
                    proyectile_list.remove(proyectile)
            try:
                if self.rect.colliderect(boss.rect):
                    proyectile_list.remove(proyectile)
                    boss.suffer_damage(player)
            except:
                pass
        else:
            if self.rect.colliderect(player.rect):
                player.discount_live()
                proyectile_list.remove(proyectile)
                
        for platform in platform_list:
            try:
                if self.rect.colliderect(platform.rect_right_side_col) or self.rect.colliderect(platform.rect_left_side_col):
                    proyectile_list.remove(proyectile)
            except:
                pass
