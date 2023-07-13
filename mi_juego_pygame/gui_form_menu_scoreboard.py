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

class FormMenuScoreBoard(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.music_path = r"recursos/sounds/music/soundtrack_menu.mp3"
        self.static_background = Background(x=0,y=0,width=w,height=h,path="recursos/images/menu/scoreboard.png")

        self.puesto_1 = Label(master=self,x=525,y=250,w=400,text=f"1- XXX - XXX",color_border=None,font="Bauhaus 93",font_size=30,font_color=C_WHITE)
        self.puesto_2 = Label(master=self,x=525,y=300,w=400,text=f"2- XXX - XXX",color_border=None,font="Bauhaus 93",font_size=30,font_color=C_WHITE)
        self.puesto_3 = Label(master=self,x=525,y=350,w=400,text=f"3- XXX - XXX",color_border=None,font="Bauhaus 93",font_size=30,font_color=C_WHITE)
        self.puesto_4 = Label(master=self,x=525,y=400,w=400,text=f"4- XXX - XXX",color_border=None,font="Bauhaus 93",font_size=30,font_color=C_WHITE)
           
        self.button_menu = Button(master=self,x=1275,y=700,w=200,h=100,color_background=None,color_border=None,image_background="recursos/images/buttoms/boton_1.png",on_click=self.on_click_boton3,on_click_param="form_menu_principal",text="MENU",font="Bauhaus 93",font_size=30,font_color=C_WHITE)
   
           
        self.lista_widget = [self.puesto_1,self.puesto_2,self.puesto_3,self.puesto_4,self.button_menu]
    
    def on_click_boton3(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos,keys,delta_ms,event):
        lista_scoreboard = Sql.devolver_puntaje()
        self.probar_scoreboard(lista_scoreboard,self.puesto_1,1,0)
        self.probar_scoreboard(lista_scoreboard,self.puesto_2,2,1)
        self.probar_scoreboard(lista_scoreboard,self.puesto_3,3,2)
        self.probar_scoreboard(lista_scoreboard,self.puesto_4,4,3)

        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def probar_scoreboard(self,lista_sb,label,order,posicion_array,):    
        try:
            label._text = f"{order}- {lista_sb[posicion_array][0]} - {int(lista_sb[posicion_array][1])}"
        except:
            pass
            
        
    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)
        for aux_widget in self.lista_widget:    
            aux_widget.draw()