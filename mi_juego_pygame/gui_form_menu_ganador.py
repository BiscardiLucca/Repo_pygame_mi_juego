import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from auxiliar import Auxiliar
from gui_label import Label
from sql import Sql
from background import Background

class FormMenuWin(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,lvl3):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.music_path = r"music/title_theme.wav"
        self.lvl_anterior = lvl3
        self.score = 0
        self.static_background = Background(x=0,y=0,width=w,height=h,path="recursos/images/menu/ganaste.png")

        self.score_label =  Label(master=self,x=480,y=550,w=400,text=f"SCORE: {self.score}",color_border=None,font="Verdana",font_size=40,font_color=C_WHITE)
        self.nombre_jugador = TextBox(master=self,x=525,y=350,w=400,color_background=C_WHITE,color_border=None,image_background=None,text="jugador",font_size=40,font_color=C_BLACK,)
        self.boton_guardar = Button(master=self,x=600,y=400,w=200,h=100,color_background=None,color_border=None,image_background="recursos/images/buttoms/boton_1.png",on_click=self.on_click_boton_guardar,on_click_param=None,text="GUARDAR",font="Verdana",font_size=25,font_color=C_WHITE)
        self.button_menu = Button(master=self,x=1275,y=650,w=200,h=100,color_background=None,color_border=None,image_background="recursos/images/buttoms/boton_1.png",on_click=self.on_click_boton3,on_click_param="form_menu_principal",text="MENU",font="Verdana",font_size=30,font_color=C_WHITE)
     
        self.lista_widget = [self.score_label,self.nombre_jugador,self.boton_guardar,self.button_menu]

    def on_click_boton_guardar(self, parametro):
        Sql.crear_tabla()
        Sql.actualizar_tabla(self.nombre_jugador._text,self.score)
        Sql.devolver_puntaje()
        self.set_active("form_menu_principal")
    
    def on_click_boton3(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos,keys,delta_ms,event):
        self.score = self.lvl_anterior.score_total
        self.score_label._text = f"SCORE: {self.score}"
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

        
    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)
        for aux_widget in self.lista_widget:    
            aux_widget.draw()