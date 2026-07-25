# Librerías del sistema
import sys
import tkinter

# Importar todo el modelo (mundo del problema)
from model.Lienzo import Lienzo
from model.Figura import Figura
from model.Punto import Punto

#Importar la vista (interacción con el usuario)
from view.gui.VentanaPrincipal import VentanaPrincipal

class AppGUI:
    
    def __init__(self):
        
        # Inicializar modelo
        self.modelo = Lienzo()
        self.modelo.inicializarLienzo()        
        
        # Inicializar la vista
        self.vista = VentanaPrincipal(pControlador=self)   
        
        # Conectar las acciones asociadas a la ventana principal
        self.vista.btnCargarFigurasLadoIzquierdo.config(command=self.mostrar_info_figuras)
        
    
    def actualizar_figura(self,puntosFigura,i):
        self.modelo.getFigura(i).setPuntos(puntosFigura)
    
    def mostrar_info_figuras(self):
        todasFiguras = self.modelo.getFiguras()        
        
        # Salida de diagnóstico
        print()
        print("#############################")
        [print(x) for x in todasFiguras]
        print("#############################")
        print()
        
        self.vista.cargarInfoFiguras(todasFiguras)        
    
    def mainloop(self):
        self.vista.mainloop()
        
    