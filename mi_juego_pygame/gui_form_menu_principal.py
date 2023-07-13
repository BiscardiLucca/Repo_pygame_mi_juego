import pygame
import sys
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from auxiliar import Auxiliar
from background import Background

class FormMenuPrincipal(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.music_path = r"recursos/sounds/music/soundtrack_menu.mp3"
        self.music = True
        Auxiliar.generar_musica(self.music_path,0.1)

        self.static_background = Background(x=0,y=0,width=w,height=h,path="recursos/images/menu/menu_principal.png")

        self.boton_jugar = Button(master=self,x=1100,y=200,w=200,h=100,color_background=None,color_border=None,image_background="recursos/images/buttoms/boton_1.png",on_click=self.on_click_boton3,on_click_param="form_game_L1",text="Jugar",font="Bauhaus 93",font_size=30,font_color=C_WHITE)
        self.boton_niveles = Button(master=self,x=1100,y=300,w=200,h=100,color_background=None,color_border=None,image_background="recursos/images/buttoms/boton_1.png",on_click=self.on_click_boton3,on_click_param="form_menu_niveles",text="Niveles",font="Bauhaus 93",font_size=30,font_color=C_WHITE)
        self.boton_instrucciones = Button(master=self,x=1100,y=400,w=200,h=100,color_background=None,color_border=None,image_background="recursos/images/buttoms/boton_1.png",on_click=self.on_click_boton3,on_click_param="form_menu_instructions",text="Instrucciones",font="Bauhaus 93",font_size=20,font_color=C_WHITE) 
        self.boton_scoreboard = Button(master=self,x=1100,y=500,w=200,h=100,color_background=None,color_border=None,image_background="recursos/images/buttoms/boton_1.png",on_click=self.on_click_boton3,on_click_param="form_menu_scoreboard",text="SCOREBOARD",font="Bauhaus 93",font_size=18,font_color=C_WHITE)
       
        self.boton_salir = Button(master=self,x=1275,y=700,w=200,h=100,color_background=None,color_border=None,image_background="recursos/images/buttoms/boton_1.png",on_click=self.on_click_boton2,on_click_param="form_game_L3",text="Salir",font="Bauhaus 93",font_size=30,font_color=C_WHITE)
                                
        self.lista_widget = [self.boton_jugar,self.boton_niveles,self.boton_instrucciones,self.boton_salir,self.boton_scoreboard]

    def on_click_boton1(self, parametro):
        self.pb1.value += 1
 
    def on_click_boton2(self, parametro):
        pygame.quit()
        sys.exit()
    
    def on_click_boton3(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos,keys,delta_ms,event):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)
        
    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)
        for aux_widget in self.lista_widget:    
            aux_widget.draw()