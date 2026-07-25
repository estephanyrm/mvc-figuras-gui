import tkinter
from functools import partial

from model.Punto import Punto

class ActualizarFigura(tkinter.Toplevel):
    
    def __init__(self,
                 padre,
                 pTitle="Editar Figura",
                 pFigura=None,
                 pIdFigura=None,
                 referencia_controlador=None
                 ):        
        
        #Atributos del formulario
        self.idFigura = pIdFigura
        self.figura = pFigura
        self.coleccionEntradasPuntos = dict()
        self.referencia_controlador=referencia_controlador
        
        # Indicar la instanciación de la herencia
        # super().__init__()
        tkinter.Toplevel.__init__(self,padre)
        
        # Establecer valores de la herencia (ventana específica)        
        self.title(pTitle)
        self.geometry(f"{250}x{350}")        
        
        #Crear cada widget y ubicarlo
        #-----------------------------
        
        print()
        print(f"ID Recibido->{self.idFigura}")
        print()
        
        # Ubicar los elementos en la ventana
        j = 1
        for i,punto in enumerate(self.figura.getPuntos()):
            entryX = tkinter.Entry(self)            
            # entryX.insert(0,"X -> "+str(punto.getX()))
            entryX.insert(0,str(punto.getX()))
            entryX.grid(row=j,column=0,sticky="w")
            
            entryY = tkinter.Entry(self)
            # entryY.insert(0,"Y -> "+str(punto.getY()))
            entryY.insert(0,str(punto.getY()))
            entryY.grid(row=j+1,column=0,sticky="w")
            
            self.coleccionEntradasPuntos[i] = {
                'entradaX'  :   entryX,
                'entradaY'  :   entryY,
            }
            
            j += 2
            
        self.btnActualizar = tkinter.Button(self,command=self.actualizarVertices,text="Update")
        self.btnActualizar.grid(
            row=len(self.figura.getPuntos())*2+2,
            column=0
        )
        
        
        
    def actualizarVertices(self):
        
        nuevosPuntos = []
        
        for llave,valor in self.coleccionEntradasPuntos.items():
            
            nuevosPuntos.append(
                Punto(x=int(valor['entradaX'].get()),
                      y=int(valor['entradaY'].get()))
            )
        
        self.referencia_controlador.actualizar_figura(nuevosPuntos,self.idFigura)
            
         