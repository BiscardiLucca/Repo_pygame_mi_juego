from player import *
from constantes import *
from auxiliar import Auxiliar
from enemigo import Enemy


class Boss():
    def __init__(self, x, y, frame_rate_ms, move_rate_ms):
        self.walk = Auxiliar.getSurfaceFromSeparateFiles("recursos/images/enemies/grievous/walk/{0}.png", 0, 7, flip=True, scale=2)
        self.stay = Auxiliar.getSurfaceFromSeparateFiles("recursos/images/enemies/grievous/idle/{0}.png", 0, 2, flip=True, scale=2)
        self.attack = Auxiliar.getSurfaceFromSeparateFiles("recursos/images/enemies/grievous/attack/{0}.png", 0, 10, flip=True, scale=2)
        self.dmg = Auxiliar.getSurfaceFromSeparateFiles("recursos/images/enemies/grievous/hit/{0}.png", 0, 2, flip=True, scale=2)
        self.spawn = Auxiliar.getSurfaceFromSeparateFiles("recursos/images/enemies/grievous/spawn/{0}.png", 0, 8, flip=True, scale=2)
        self.death = Auxiliar.getSurfaceFromSeparateFiles("recursos/images/enemies/grievous/dead/{0}.png", 0, 18, flip=True, scale=2)
        self.frame = 0
        self.lives = 5
        self.score = 0

        self.health_bar_rect = pygame.Rect(20, 500, 100, 10)

        self.is_walking = False
        self.flag_spawn = True
        self.flag_still_alive = True
        self.flag_death = False

        self.animation = self.spawn
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.tiempo_inicial = pygame.time.get_ticks()

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms

    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if self.tiempo_transcurrido_animation >= self.frame_rate_ms:
            self.tiempo_transcurrido_animation = 0
            if self.is_walking:  
                self.animation = self.walk  
            elif self.frame < len(self.animation) - 1:
                self.frame += 1
            else:
                self.frame = 0

    def update(self, delta_ms, player, enemies_list):
        self.do_animation(delta_ms)
        self.animate_spawn()
        self.do_attack(player, enemies_list)
        self.stop_suffering_dmg()
        self.animate_death()

    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen, color=(255, 255, 0), rect=self.rect)
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255, 0, 0), (self.health_bar_rect.x, self.health_bar_rect.y, 100, 10))
        pygame.draw.rect(screen, (0, 255, 0), (self.health_bar_rect.x, self.health_bar_rect.y, self.lives * 20, 10))

    def receive_shoot(self):
        BOSS_HURTED.play()
        self.lives -= 1
        if self.lives < 1:
            self.animate_death()

    def do_attack(self, player, enemies_list):
        if self.calculate_delta_time(7000) and self.animation == self.stay:
            self.animation = self.attack
            self.tiempo_inicial = pygame.time.get_ticks()
        if self.animation == self.attack and self.frame == len(self.animation) - 1:
            if player.rect.y > 575:
                player.tiempo_inicial = pygame.time.get_ticks()
                player.discount_live()
                player.move_y = -20
                player.flag_boss_hurted = True
            BOSS_ATTACK.play()
            self.frame = 0
            self.animate_stay()

    def calculate_delta_time(self, tiempo_objetivo):
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = tiempo_actual - self.tiempo_inicial
        if tiempo_transcurrido >= tiempo_objetivo:
            return True
        else:
            return False

    def animate_spawn(self):
        if self.flag_spawn:
            self.animation = self.spawn
        if self.animation == self.spawn and self.frame == len(self.animation) - 1:
            self.frame = 0
            self.animate_stay()
            self.flag_spawn = False

    def animate_stay(self):
        self.animation = self.stay

    def suffer_damage(self, player):
        self.frame = 0
        self.animation = self.dmg
        self.lives -= 1
        player.score += 200

    def stop_suffering_dmg(self):
        if self.animation == self.dmg and self.frame == len(self.animation) - 1:
            self.frame = 0
            self.animate_stay()

    def animate_death(self):
        if self.flag_still_alive:
            if self.lives < 1:
                BOSS_DIED.play()
                self.animation = self.death
                self.flag_still_alive = False
        if self.animation == self.death and self.frame == len(self.animation) - 1 and not self.flag_still_alive:
            self.frame = 0
            self.animation = self.death
            self.flag_death = True
