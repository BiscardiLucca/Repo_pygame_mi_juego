from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from background import Background

class FormMenuInstructions(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.music_path = r"music/title_theme.wav"
        self.static_background = Background(x=0,y=0,width=w,height=h,path="recursos/images/menu/instrucciones.png")

        self.button_menu = Button(master=self,x=600,y=715,w=190,h=90,color_background=None,color_border=None,image_background="recursos/images/buttoms/boton_1.png",on_click=self.on_click_boton3,on_click_param="form_menu_principal",text="VOLVER",font="Bauhaus 93",font_size=30,font_color=C_WHITE)
     
        self.lista_widget = [self.button_menu]
        
    
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