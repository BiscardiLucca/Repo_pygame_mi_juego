import pygame
from constantes import *
from auxiliar import Auxiliar
from bullet import Proyectile

class Player:
    def __init__(self, x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, p_scale=1, interval_time_jump=100):
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/images/caracters/tropper/walk/{0}.png", 0, 7, flip=False, scale=p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/images/caracters/tropper/walk/{0}.png", 0, 7, flip=True, scale=p_scale)
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/images/caracters/tropper/idle/{0}.png", 0, 7, flip=False, scale=p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/images/caracters/tropper/idle/{0}.png", 0, 7, flip=True, scale=p_scale)
        self.jump_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/images/caracters/tropper/jump/{0}.png", 0, 2, flip=False, scale=p_scale)
        self.jump_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/images/caracters/tropper/jump/{0}.png", 0, 2, flip=True, scale=p_scale)
        self.atk_stance_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/images/caracters/tropper/shoot/{0}.png", 0, 6, flip=False, scale=p_scale)
        self.atk_stance_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/images/caracters/tropper/shoot/{0}.png", 0, 6, flip=True, scale=p_scale)
        self.charge_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/images/caracters/tropper/shoot/{0}.png", 0, 6, flip=False, scale=p_scale)
        self.charge_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/images/caracters/tropper/shoot/{0}.png", 0, 6, flip=True, scale=p_scale)
        self.atk_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/images/caracters/tropper/shoot/{0}.png", 0, 6, flip=False, scale=p_scale)
        self.atk_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/images/caracters/tropper/shoot/{0}.png", 0, 6, flip=True, scale=p_scale)
        self.hurt_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/images/caracters/tropper/hit/{0}.png", 0, 5, flip=False, scale=p_scale)
        self.hurt_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/images/caracters/tropper/hit/{0}.png", 0, 5, flip=True, scale=p_scale)

        self.tiempo_trans = 0
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x + self.rect.width / 3, y, self.rect.width / 3, self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0
        self.interval_time_jump = interval_time_jump

        self.tiempo_objetivo = 500
        self.atk_stance_flag = False
        self.tiempo_transcurrido = 0

        self.tiempo_inicial = pygame.time.get_ticks()

        self.flag_boss_hurted = False
        self.flag_hurted = False

    def walk(self, direction):
        if self.is_jump == False and self.is_fall == False:
            if self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l):
                self.frame = 0
                self.direction = direction
                if direction == DIRECTION_R:
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                else:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l

    def shoot(self, on_off=True):
        self.is_shoot = on_off
        if on_off == True and self.is_jump == False and self.is_fall == False:
            if self.animation != self.shoot_r and self.animation != self.shoot_l:
                self.frame = 0
                self.is_shoot = True
                if self.direction == DIRECTION_R:
                    self.animation = self.shoot_r
                else:
                    self.animation = self.shoot_l

    def receive_shoot(self):
        self.lives -= 1

    def death_animation(self):
        if self.animation != self.dead_r and self.animation != self.dead_l:
            self.frame = 0
        self.is_dead = True
        if self.direction == DIRECTION_R:
            self.animation = self.dead_r
        else:
            self.animation = self.dead_l
        if self.frame == len(self.animation) - 1:
            self.is_death_animation_finished = True
            self.game_over = True

    def jump(self, platform_list, on_off=True):
        if on_off and self.is_jump == False and self.is_fall == False:
            self.y_start_jump = self.rect.y
            ADV_JUMP.play()
            if self.direction == DIRECTION_R:
                self.move_x = int(self.move_x / 1.5)
                self.move_y = -self.jump_power
                self.animation = self.jump_r
            else:
                self.move_x = int(self.move_x / 1.5)
                self.move_y = -self.jump_power
                self.animation = self.jump_l
            self.frame = 0
            self.is_jump = True
        if on_off == False:
            self.is_jump = False
            self.stay()

    def stay(self):
        if self.is_knife or self.is_shoot:
            return

        if self.animation != self.stay_r and self.animation != self.stay_l:
            if self.direction == DIRECTION_R:
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def change_x(self, delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self, delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self, delta_ms, plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if self.tiempo_transcurrido_move >= self.move_rate_ms:
            self.tiempo_transcurrido_move = 0

            if abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump:
                self.move_y = 0
            self.change_x(self.move_x)
            self.change_y(self.move_y)
            if not self.is_on_plataform(plataform_list):
                if self.move_y == 0:
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                if self.is_jump:
                    self.jump(plataform_list, False)
                self.is_fall = False
            if self.collide_platform_left_side(plataform_list) or self.rect.x >= 1400:
                self.move_x = 0
                self.change_x(-5)
            elif self.collide_platform_right_side(plataform_list) or self.rect.x <= 0:
                self.move_x = 0
                self.change_x(5)
            if self.collide_platform_bottom(plataform_list):
                self.move_y = 0

    def is_on_plataform(self, plataform_list):
        retorno = False

        if self.ground_collition_rect.bottom >= GROUND_LEVEL:
            retorno = True
        else:
            for plataforma in plataform_list:
                if self.ground_collition_rect.colliderect(plataforma.ground_collition_rect):
                    retorno = True
                    break
        return retorno

    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if self.tiempo_transcurrido_animation >= self.frame_rate_ms:
            self.tiempo_transcurrido_animation = 0
            if self.frame < len(self.animation) - 1:
                self.frame += 1
            else:
                self.frame = 0

    def update(self, delta_ms, plataform_list, enemy_list):
        self.do_movement(delta_ms, plataform_list)
        self.do_animation(delta_ms)
        self.colllide_enemy(enemy_list)
        self.boss_hurted()

    def draw(self, screen):

        if DEBUG:
            pygame.draw.rect(screen, color=(255, 0, 0), rect=self.collition_rect)
            pygame.draw.rect(screen, color=(255, 255, 0), rect=self.ground_collition_rect)

        try:
            self.imagen = self.animation[self.frame]
        except IndexError:
            print("IndexError")
        screen.blit(self.imagen, self.rect)

    def events(self, delta_ms, keys, event, proyectile_list, platform_list):
        self.tiempo_transcurrido += delta_ms

        if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.walk(DIRECTION_L)

        if not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
            self.walk(DIRECTION_R)

        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_UP]:
            self.stay()
        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_UP]:
            self.stay()

        if keys[pygame.K_UP]:
            if (self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump:
                self.jump(platform_list, True)
                self.tiempo_last_jump = self.tiempo_transcurrido

        if keys[pygame.K_SPACE] and not self.is_shoot:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.tiempo_trans >= 2000:
                self.attack()
                if self.direction == DIRECTION_R:
                    self.create_proyectile(proyectile_list, self.rect.right, self.rect.centery)
                else:
                    self.create_proyectile(proyectile_list, self.rect.left, self.rect.centery)
                self.tiempo_trans = tiempo_actual

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.is_shoot = False

    def create_proyectile(self, proyectile_list, x, y):
        proyectile = Proyectile(5, x, y, self.direction)
        proyectile_list.append(proyectile)

    def timer(self, tiempo_obj):
        if self.atk_stance_flag == False:
            self.tiempo_trans = pygame.time.get_ticks()
            self.atk_stance_flag = True
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_trans >= tiempo_obj:
            return True
        else:
            return False

    def calculate_delta_time(self, tiempo_objetivo):
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = tiempo_actual - self.tiempo_inicial
        if tiempo_transcurrido >= tiempo_objetivo:
            return True
        else:
            return False

    def attack(self):
        self.frame = 0
        ADV_ATTACK.play()
        if self.direction == DIRECTION_R:
            self.animation = self.atk_r
        else:
            self.animation = self.atk_l

    def atk_stance(self):
        self.frame = 0
        if self.direction == DIRECTION_R:
            self.animation = self.atk_stance_r
        else:
            self.animation = self.atk_stance_l

    def colllide_enemy(self, enemy_list):
        collision_detected = False
        for enemy in enemy_list:
            if self.rect.colliderect(enemy.rect):
                collision_detected = True
                break
        if collision_detected:
            if not self.colliding_enemy_flag:
                self.be_hurted()
                self.discount_live()
                self.colliding_enemy_flag = True
        else:
            self.colliding_enemy_flag = False

    def collide_platform_left_side(self, platform_list):
        retorno = False
        for platform in platform_list:
            try:
                if self.rect.colliderect(platform.rect_left_side_col):
                    retorno = True
                    break
            except:
                pass
        return retorno

    def collide_platform_right_side(self, platform_list):
        retorno = False
        for platform in platform_list:
            try:
                if self.rect.colliderect(platform.rect_right_side_col):
                    retorno = True
                    break
            except:
                pass
        return retorno

    def collide_platform_bottom(self, platform_list):
        retorno = False
        for platform in platform_list:
            try:
                if self.rect.colliderect(platform.rect_bottom_col):
                    retorno = True
                    break
            except:
                pass
        return retorno

    def be_hurted(self):
        if self.direction == DIRECTION_R:
            self.animation = self.hurt_r
        else:
            self.animation = self.hurt_l

    def boss_hurted(self):
        if self.flag_boss_hurted:
            if self.calculate_delta_time(300):
                self.move_y = 0
                self.flag_boss_hurted = False

    def discount_live(self):
        ADV_HURTED.play()
        self.flag_hurted = True
        self.lives -= 1
