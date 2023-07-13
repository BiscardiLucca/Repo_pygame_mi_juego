import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_progressbar import ProgressBar
from player import Player
from enemigo import Enemy
from plataform import Plataform
from background import Background
from gui_label import Label
from auxiliar import Auxiliar
from trampa import Trampa

class FormGameLevel2(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,lvl1):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.player_1 = self.generate_player()
        self.music_path = r"recursos/sounds/music/soundtrack_level_2.mp3"
        self.music_menu = r"recursos/sounds/music/soundtrack_menu.mp3"
        self.tiempo_inicial = pygame.time.get_ticks()
        self.music = True
        self.cronometro = 120
        self.lvl_anterior = lvl1
        self.score_total = 0
        self.pausado = False
        self.font = pygame.font.SysFont("Bauhaus 93",50)

        
        # --- GUI WIDGET ---        
        self.button_menu = Button(master=self,x=1275,y=700,w=200,h=100,color_background=None,color_border=None,image_background="recursos/images/buttoms/boton_1.png",on_click=self.on_click_boton1,on_click_param="form_menu_principal",text="MENU",font="Bauhaus 93",font_size=30,font_color=C_WHITE)
         
        self.text_score = Label(master=self,x=1200,y=30,w=200,h=50,color_background=None,color_border=None,image_background=None,
                                  text=f'SCORE: {str(self.player_1.score)}',font="Bauhaus 93",font_size=30,font_color=C_WHITE)
        
        self.text_time = Label(master=self,x=1200,y=80,w=200,h=50,color_background=None,color_border=None,image_background=None,
                                  text=f'TIME: {str(self.cronometro)}',font="Bauhaus 93",font_size=30,font_color=C_WHITE)
        
        self.pb_lives = ProgressBar(master=self,x=1000,y=50,w=150,h=30,color_background=None,color_border=None,image_background="recursos/images/gui/set_gui_01/Data_Border/Bars/Bar_Background01.png",image_progress="recursos/images/gui/set_gui_01/Data_Border/Bars/Bar_Segment05.png",value = self.player_1.lives, value_max=5)
       
        self.widget_list = [self.button_menu,self.text_score,self.text_time,self.pb_lives]

        # --- GAME ELEMNTS --- 
        self.static_background = Background(x=0,y=0,width=w,height=h,path="recursos/images/locations/cindralling/cindralling.png")

        self.boss = None

        self.enemies_list = []
        self.generate_enemies()
        
        self.platform_list = []
        self.generate_platform()

        self.trampa_list = []
        self.generate_trampas()

        self.proyectile_list = []
        self.proyectile_enemy_list = []
        self.loot_list = []
        

    def generate_player(self):
        player = Player(x=750, y=600, speed_walk=15, speed_run=15, gravity=15, jump_power=20, frame_rate_ms=100, move_rate_ms=45, jump_height=160, p_scale=1.7, interval_time_jump=300)
        return player

    def generate_enemies(self):
        self.enemies_list.append(Enemy(x=130, y= 620, speed_walk=5, speed_run=8, gravity=8, jump_power=30, frame_rate_ms=80, move_rate_ms=80, jump_height=140, p_scale=1.7, interval_time_jump=300, enemy_type=2, x_length=100))
        self.enemies_list.append(Enemy(x=1310, y= 620, speed_walk=5, speed_run=8, gravity=8, jump_power=30, frame_rate_ms=80, move_rate_ms=80, jump_height=140, p_scale=1.7, interval_time_jump=300, enemy_type=2, x_length=100))
        self.enemies_list.append(Enemy(x=40, y= 250, speed_walk=5, speed_run=8, gravity=8, jump_power=30, frame_rate_ms=80, move_rate_ms=80, jump_height=140, p_scale=1.2, interval_time_jump=300, enemy_type=1, x_length=15))
        self.enemies_list.append(Enemy(x=1420, y= 240, speed_walk=5, speed_run=8, gravity=8, jump_power=30, frame_rate_ms=80, move_rate_ms=80, jump_height=140, p_scale=1.2, interval_time_jump=300, enemy_type=0, x_length=15))
    
    def generate_platform(self):
        self.platform_list.append(Plataform(x=20, y=320, height=50, width=100, image="recursos/images/tiles/level_2.png", column=0))
        self.platform_list.append(Plataform(x=580, y=400, height=50, width=300, image="recursos/images/tiles/level_2.png", column=0))
        self.platform_list.append(Plataform(x=250, y=540, height=50, width=250, image="recursos/images/tiles/level_2.png", column=0))
        self.platform_list.append(Plataform(x=250, y=360, height=50, width=250, image="recursos/images/tiles/level_2.png", column=0))
        self.platform_list.append(Plataform(x=1050, y=380, height=50, width=250, image="recursos/images/tiles/level_2.png", column=0))
        self.platform_list.append(Plataform(x=1400, y=300, height=50, width=100, image="recursos/images/tiles/level_2.png", column=0))


    def generate_trampas(self):
        self.trampa_list.append(Trampa(x=340,y=345))
        self.trampa_list.append(Trampa(x=1060,y=690))
        self.trampa_list.append(Trampa(x=1150,y=370))


    def update(self,lista_eventos,keys,delta_ms,event,evento_1000ms):
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.pausado = not self.pausado
        
        if self.pausado:
        
            pausa_texto = self.font.render("JUEGO EN PAUSA", True, (255, 255, 255))
            self.surface.blit(pausa_texto, (self.w/2 - pausa_texto.get_width()/2, self.h/2 - pausa_texto.get_height()/2))
        
        else:
        
            if self.music:
                Auxiliar.generar_musica(self.music_path,0.1)
                self.music = False
            
            for aux_widget in self.widget_list:
                aux_widget.update(lista_eventos)

            for proyectile_element in self.proyectile_list:
                proyectile_element.update(delta_ms,self.enemies_list,self.platform_list,self.proyectile_list,proyectile_element,self.player_1,self.loot_list,self.boss)
                
            for proyectile_enemy_element in self.proyectile_enemy_list:
                proyectile_enemy_element.update(delta_ms,self.enemies_list,self.platform_list,self.proyectile_enemy_list,proyectile_enemy_element,self.player_1,self.loot_list,self.boss)

            for enemy_element in self.enemies_list:
                enemy_element.update(delta_ms,self.platform_list,self.player_1,self.proyectile_enemy_list)
                
            for loot_element in self.loot_list:
                loot_element.update(self.player_1, self.loot_list, loot_element,self.platform_list)
                
            for trampa_element in self.trampa_list:
                trampa_element.update(self.player_1, self.trampa_list, trampa_element)
                
            self.descontar_tiempo(lista_eventos,evento_1000ms)

            self.score_total = self.player_1.score
            
            self.text_score._text = f'PUNTOS: {str(self.player_1.score)}'
            self.text_time._text = f'TIEMPO: {str(self.cronometro)}'
            self.player_1.events(delta_ms,keys,event,self.proyectile_list,self.platform_list)
            self.player_1.update(delta_ms,self.platform_list,self.enemies_list)

            self.pb_lives.value = self.player_1.lives 

            if self.player_1.score > 1350:
                self.score_total = self.player_1.score
                print(self.score_total)
                self.reiniciar_nivel()
                self.set_active("form_game_L3")
                    
            if self.player_1.lives < 1 or self.cronometro < 1:
                self.score_total = 0
                self.reiniciar_nivel()
                self.reproducir_musica(self.music_menu)
                self.set_active("form_game_lose")
                
            
    def on_click_boton1(self, parametro):
        self.reiniciar_nivel()
        self.reproducir_musica(self.music_menu)
        self.music = True
        self.set_active("form_menu_principal") 
           
    def descontar_tiempo(self,lista_eventos,evento_1000ms):
        for event in lista_eventos:
            if event.type == evento_1000ms:
                self.cronometro -= 1  
            
    def reiniciar_nivel(self):

        self.cronometro = 120
        self.music = True
        self.player_1 = self.generate_player()
        self.boss = None
        self.platform_list = []
        self.enemies_list = []
        self.proyectile_list = []
        self.proyectile_enemy_list = []   
        self.loot_list = []
        self.trampa_list = []
        self.generate_trampas()
        self.generate_enemies()
        self.generate_platform()

    def reproducir_musica(self,music_path):
        if self.music:
            Auxiliar.generar_musica(music_path,0.1)
            self.music = False
                
    def calculate_delta_time(self,tiempo_objetivo):
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = tiempo_actual - self.tiempo_inicial
        if tiempo_transcurrido >= tiempo_objetivo:
            return True
        else:
            return False

        
    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)


        for aux_widget in self.widget_list:    
            aux_widget.draw()

        for plataforma in self.platform_list:
            plataforma.draw(self.surface)

        for enemy_element in self.enemies_list:
            enemy_element.draw(self.surface)
        
        self.player_1.draw(self.surface)

        for proyectile_element in self.proyectile_list:
            proyectile_element.draw(self.surface)
            
        for proyectile_element in self.proyectile_enemy_list:
            proyectile_element.draw(self.surface)
            
        for loot_element in self.loot_list:
            loot_element.draw(self.surface)
            
        for trampa_element in self.trampa_list:
            trampa_element.draw(self.surface)