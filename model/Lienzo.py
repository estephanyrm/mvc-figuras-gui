from typing import List

from model.Figura import Figura
from model.Punto import Punto

class Lienzo:    
    
    def __init__(self,                 
                 figuras:List[Figura]=[])->None:
        self.__figuras = figuras
        
    def inicializarLienzo(self,numero_figuras_iniciales=3):
        for _ in range(numero_figuras_iniciales):
            self.__figuras.append(
                Figura(creacion_aleatoria=True)
            )
            
    def adicionarFiguraAleatoria(self):
        self.__figuras.append(
            Figura(creacion_aleatoria=True)
        )
            
    def getFigura(self,i):
        return self.__figuras[i]
    
    def setFigura(self,nuevaFigura,i):
        self.__figuras[i] = nuevaFigura
    
    def getFiguras(self):
        return self.__figuras
    
    def getUltimaFiguraCreada(self):
        return self.__figuras[-1]
    
    def numeroFigurasRegistradas(self):
        return len(self.__figuras)
    
    def __str__(self)->str:
        cadena = str()
        cadena += f"%%%%%%%%%%%%%%%%%%%%% Lienzo %%%%%%%%%%%%%%%%%%%%%\n\n"        
        for i,figura in enumerate(self.__figuras):
            cadena += f"Figura ({i})\n"
            cadena += str(figura)            
        cadena += f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n"
        return cadena    