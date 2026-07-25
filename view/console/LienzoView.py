from turtle import *
import turtle
import time
from tkinter import TclError
from model.Lienzo import Lienzo
from model.Figura import Figura

class LienzoView:     
    
    # Se vuelve True apenas el usuario cierra la ventana de dibujo con la X
    ventana_cerrada = False
    
    @classmethod
    def presentar_figura_consola(cls,figura:Figura):
        print()
        print("############")
        print(figura)
        print("############")
        print()
        
    
    @classmethod
    def presentar_lienzo_completo_consola(cls,lienzo:Lienzo):
        print("*")
        print(lienzo)
        print("*")
        
        
    @classmethod
    def dibujar_todas_figuras(cls,lienzo:Lienzo):        
        figurasEnLienzo = lienzo.numeroFigurasRegistradas()        
        for i in range(figurasEnLienzo):
            if cls.ventana_cerrada:
                break
            cls.dibujarFigura(figura=lienzo.getFigura(i))    
        
    
    @classmethod
    def dibujarFigura(cls,
                      diametro_punto:int=10,
                      color_punto:str='blue',
                      color_segmento:str='black',
                      velocidad_lapiz:int=4,
                      figura:Figura=None):
        
        # Si el usuario ya cerró la ventana de dibujo, no intentar dibujar de nuevo
        if cls.ventana_cerrada:
            print("\n[Aviso] La ventana de dibujo fue cerrada. No es posible seguir dibujando en esta sesión.\n")
            return
        
        try:
            # Establecer parámetros del lápiz/tortuga
            lapiz = Turtle()
            lapiz.speed(velocidad_lapiz)
            lapiz.penup()
            
            # Iniciar el dibujado en el primer punto o vértice de la figura
            lapiz.goto(
                figura.getPunto(0).getX(),
                figura.getPunto(0).getY()
            )
            lapiz.pendown()        
            lapiz.color(color_punto)
            lapiz.dot(diametro_punto)
            lapiz.color(color_segmento)
            
            # Dibujar el resto de puntos        
            for i in range(1,figura.getNumeroVertices()):
                lapiz.color(color_segmento)
                lapiz.goto(
                    figura.getPunto(i).getX(),
                    figura.getPunto(i).getY()
                )
                lapiz.color(color_punto)
                lapiz.dot(diametro_punto)
            
            # Segmento de cierre de la figura
            lapiz.color(color_segmento)
            lapiz.goto(
                figura.getPunto(0).getX(),
                figura.getPunto(0).getY()
            )
            lapiz.color(color_punto)
            lapiz.dot(diametro_punto)
            
            # Terminar ciclo de dibujado
            time.sleep(4)
            clearscreen()
        
        except (turtle.Terminator, TclError):
            # El usuario cerró la ventana de turtle manualmente (con la X) mientras se dibujaba
            cls.ventana_cerrada = True
            print("\n[Aviso] Cerraste la ventana de dibujo. Vuelve a abrir el programa si deseas dibujar de nuevo.\n")