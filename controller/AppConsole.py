# Librerías del sistema
import sys

# Importar todo el modelo (mundo del problema)
from model.Lienzo import Lienzo
from model.Figura import Figura
from model.Punto import Punto

#Importar la vista (interacción con el usuario)
from view.console.Formulario import Formulario
from view.console.Mensaje import Mensaje
from view.console.Formulario import TipoFormulario
from view.console.LienzoView import LienzoView

class AppConsole:
    
    SALIR = 0
    IMPRIMIR_FIGURAS_CONSOLA = 1
    DIBUJAR_FIGURA = 2
    DIBUJAR_TODAS_FIGURAS = 3
    ADICIONAR_FIGURA_ALEATORIA = 4
    ADICIONAR_FIGURA_ESPECIFICA = 5
    
    def __init__(self)->None:
        
        # Inicialización de la aplicación
        self.formulario_menu_principal = Formulario(tipo_formulario=TipoFormulario.MENU_PRINCIPAL)
        self.modelo = Lienzo()
        self.modelo.inicializarLienzo()
        
    def imprimir_figuras_consola(self):
        LienzoView.presentar_lienzo_completo_consola(lienzo=self.modelo)
        
    def dibujar_todas_figuras(self):
        LienzoView.dibujar_todas_figuras(lienzo=self.modelo)
        
    def dibujar_figura(self):        
        numero_actual_figuras = self.modelo.numeroFigurasRegistradas()
        if numero_actual_figuras == 0:
            Mensaje.error("No hay figuras registradas todavía. Agrega una primero (opción 4 o 5).")
            return
        
        LienzoView.presentar_lienzo_completo_consola(lienzo=self.modelo)
        formulario_elegir_figura = Formulario(tipo_formulario=TipoFormulario.ELEGIR_FIGURA)
        indice_figura_elegida = formulario_elegir_figura.presentarElegirFigura(numero_actual_figuras)
        figura_elegida = self.modelo.getFigura(indice_figura_elegida)
        LienzoView.dibujarFigura(figura=figura_elegida)
        
    def adicionar_figura_aleatoria(self,lienzo:Lienzo):
        lienzo.adicionarFiguraAleatoria()
        Mensaje.informacion(informacion="Última figura creada (aleatoriamente)")
        ultima_figura_adicionada = lienzo.getUltimaFiguraCreada()
        LienzoView.presentar_figura_consola(figura=ultima_figura_adicionada)
        LienzoView.dibujarFigura(                      
                      color_punto='red',
                      color_segmento='brown',                      
                      figura=ultima_figura_adicionada)        
        
        
    def mainloop(self):
        
        app_activa = True
        while app_activa:
            
            opcion_ingresada = self.formulario_menu_principal.presentarMenuPrincipal()
            try:
                if opcion_ingresada == self.IMPRIMIR_FIGURAS_CONSOLA:
                    
                    self.imprimir_figuras_consola()
                    
                elif opcion_ingresada == self.DIBUJAR_FIGURA:
                    
                    self.dibujar_figura()
                    
                elif opcion_ingresada == self.DIBUJAR_TODAS_FIGURAS:
                    
                    self.dibujar_todas_figuras()
                    
                elif opcion_ingresada == self.ADICIONAR_FIGURA_ALEATORIA:
                    
                    self.adicionar_figura_aleatoria(lienzo=self.modelo)
                    
                elif opcion_ingresada == self.SALIR:
                    
                    Mensaje.informacion("Hasta Luego!")
                    app_activa = False
                
                else:
                    Mensaje.error(f"Opción '{opcion_ingresada}' no existe. Elige un número del 0 al 5.")
            
            except Exception as error:
                # Red de seguridad: cualquier error inesperado se muestra de forma clara
                # y el programa vuelve al menú en vez de detenerse con un traceback.
                Mensaje.error(f"Ocurrió un problema inesperado: {error}")
                
        
        # Terminación exitosa de la aplicación (interacción con el sistema operativo)
        sys.exit(0)       