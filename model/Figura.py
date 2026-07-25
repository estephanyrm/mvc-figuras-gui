# Importado de librerías
import pprint as pp
import random
from typing import List
from turtle import *

# Importado de abstracciones del modelo
from model.Punto import Punto

class Figura:
    
    # Constructor
    def __init__(self,
                 tipo:str='Sin especificar',
                 puntos:List[Punto]=[],
                 creacion_aleatoria:bool=False)->None:
        
        # Inicializar atributos con los parámetros que llegan del constructor o por defecto
        self.__tipo = tipo
        self.__puntos = puntos
        
        # Si la bandera llega activa
        if creacion_aleatoria:
            
            # Colocar los atributos en el estado adecuado (prevenir combinaciones equivocadas)
            self.__tipo = ''
            self.__puntos = []
            
            # Elección de tipo y construcción aleatoria
            tipo_elegido = random.randint(0,1)
            if tipo_elegido == 0:
                self.__tipo = 'TRI'
                for _ in range(3):
                    self.adicionarVertice(nuevoPunto=Punto(
                        x=random.randint(-200,200),
                        y=random.randint(-200,200),                        
                    ))
            elif tipo_elegido == 1:
                self.__tipo = 'CUA'
                longitud_cuadrado = random.randint(40,70)
                esquina_superior_izquierda = Punto(
                        x=random.randint(-200,200),
                        y=random.randint(-200,200),                        
                    )
                self.adicionarVertice(nuevoPunto=esquina_superior_izquierda)
                esquina_superior_derecha = Punto(
                        x=esquina_superior_izquierda.getX()+longitud_cuadrado,
                        y=esquina_superior_izquierda.getY(),                        
                    )
                self.adicionarVertice(nuevoPunto=esquina_superior_derecha)
                esquina_inferior_derecha = Punto(
                        x=esquina_superior_derecha.getX(),
                        y=esquina_superior_derecha.getY()-longitud_cuadrado,
                    )
                self.adicionarVertice(nuevoPunto=esquina_inferior_derecha)
                esquina_inferior_izquierda = Punto(
                        x=esquina_superior_izquierda.getX(),
                        y=esquina_inferior_derecha.getY(),
                    )
                self.adicionarVertice(nuevoPunto=esquina_inferior_izquierda)
            
        
    def adicionarVertice(self,nuevoPunto:Punto=Punto())->int:
        self.__puntos.append(nuevoPunto)
        return len(self.__puntos)
    
    def dibujarFigura(self,
                      diametro_punto:int=10,
                      color_punto:str='blue',
                      color_segmento:str='black',
                      velocidad_lapiz:int=4):
        
        # Establecer parámetros del lápiz/tortuga
        lapiz = Turtle()
        lapiz.speed(velocidad_lapiz)
        lapiz.penup()
        
        # Iniciar el dibujado en el primer punto o vértice de la figura
        lapiz.goto(
            self.__puntos[0].getX(),
            self.__puntos[0].getY()
        )
        lapiz.pendown()        
        lapiz.color(color_punto)
        lapiz.dot(diametro_punto)
        lapiz.color(color_segmento)
        
        # Dibujar el resto de puntos        
        for i in range(1,len(self.__puntos)):
            lapiz.color(color_segmento)
            lapiz.goto(
                self.__puntos[i].getX(),
                self.__puntos[i].getY()
            )
            lapiz.color(color_punto)
            lapiz.dot(diametro_punto)
        
        # Segmento de cierre de la figura
        lapiz.color(color_segmento)
        lapiz.goto(
            self.__puntos[0].getX(),
            self.__puntos[0].getY()
        )
        lapiz.color(color_punto)
        lapiz.dot(diametro_punto)
        
        lapiz.clearscreen()
        
    def getPunto(self,i):
        return self.__puntos[i]
    
    def setPuntos(self,nuevosPuntos):
        self.__puntos = nuevosPuntos
    
    def getTipo(self):
        return self.__tipo
    
    def getPuntos(self):
        return self.__puntos
    
    def getNumeroVertices(self):
        return len(self.__puntos)    
        
    def __str__(self)->str:
        cadena = str()
        cadena += f"****************************\n\n"
        cadena += f"Tipo: {self.__tipo}\n\n"
        for punto in self.__puntos:
            cadena += str(punto)
            cadena += f"\n****************************\n"
        return cadena    