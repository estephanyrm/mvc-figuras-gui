from model.Lienzo import Lienzo
from model.Figura import Figura
from model.Punto import Punto
from view.console.Mensaje import Mensaje
from typing import List, Union

import enum

class TipoFormulario(enum.Enum):
    MENU_PRINCIPAL = 1
    ADICIONAR_ELEMENTO = 2
    ELEGIR_FIGURA = 2
    CONFIRMACION = 3    

class Formulario:    
    
    def __init__(self, tipo_formulario:TipoFormulario=TipoFormulario.MENU_PRINCIPAL):        
        self.validacion = None
        self.tipoFormulario =tipo_formulario
        
    def presentarElegirFigura(self,numero_figuras)->int:
        while True:
            entrada = input(f'Ingresar código de figura (0 a {numero_figuras - 1}): ')
            try:
                figura_elegida = int(entrada)
            except ValueError:
                Mensaje.error(f"'{entrada}' no es un número válido. Ingresa solo dígitos, por ejemplo: 0")
                continue
            
            if figura_elegida >= numero_figuras or figura_elegida < 0:
                Mensaje.error(f"Código fuera de rango. Debe estar entre 0 y {numero_figuras - 1}")
            else:
                return figura_elegida
    
    
    def presentarMenuPrincipal(self)->int:
        print()
        print("/////////////// MVC Objetos //////////////////")
        print("1) Imprimir figuras en consola")
        print("2) Dibujar figura")
        print("3) Dibujar todas las figuras")
        print("4) Adicionar figura aleatoria")        
        print("5) Adicionar figura específica")
        print("0) Salir")
        print("///////////////////////////////////////////////")
        while True:
            entrada = input('Ingresar opción (0-5): ')
            try:                
                return int(entrada)
            except ValueError:
                Mensaje.error(f"'{entrada}' no es válido. Ingresa solo el número de una opción del menú (0-5)")
        
        
    def getValidacion(self)->Union[None,bool]:
        return self.validacion
    
    def validar(self):
        if self.tipoFormulario == TipoFormulario.MENU_PRINCIPAL:
            pass
        elif self.tipoFormulario == TipoFormulario.ADICIONAR_ELEMENTO:
            pass
        
    
            
        
    
    

