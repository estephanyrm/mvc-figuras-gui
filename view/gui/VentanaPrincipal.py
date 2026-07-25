import tkinter

from view.gui.FormularioFigura import ActualizarFigura
from functools import partial

from PIL import Image, ImageTk

class VentanaPrincipal(tkinter.Tk):
    
    def __init__(self,
                 pTitle="Gestor Figuras",
                 pGeometry=f"{800}x{600}",
                 pControlador=None):
        
        # Atributos de control de la ventana
        self.botonesDinamicos = []
        
        # Frames para presentar la información de las figuras
        self.framesFiguras = []
        
        # Indicar la instanciación de la herencia
        super().__init__()
        
        # Establecer valores de la herencia (ventana específica)
        self.geometry(pGeometry)
        self.title(pTitle)
        
        self.controlador = pControlador
        
        #Crear cada widget y ubicarlo
        #---------------------------
        
        self.frameIzquierdo = tkinter.Frame(self)
        self.frameIzquierdo.grid(row=0,column=0,sticky="w")
        
        self.frameDerecho = tkinter.Frame(self)
        self.frameDerecho.grid(row=0,column=1,sticky="e")
        
        # Botones del lado izquierdo
        self.btnCargarFigurasLadoIzquierdo = tkinter.Button(
            self.frameIzquierdo,
            text="Mostrar Info Figuras"            
        )
        self.btnCargarFigurasLadoIzquierdo.grid(
            row=0,
            column=0,
            sticky="ew",
        )
        
        self.btnAgregarBoton = tkinter.Button(
            self.frameIzquierdo,
            text="+",
            command=self.agergarBoton,
        )
        self.btnAgregarBoton.grid(
            row=1,
            column=0,
            sticky="ew",
        )
        
    def cargarInfoFiguras(self,figurasCompletas,numeroColumnas=1):                
        
        # Limpiar el contenedor de frames de las figuras
        self.framesFiguras.clear()
        
        # Contador para la ubicación de los widgets
        contadorColumnas = 0
        contadorFilas = 0
        
        # Recorrer todas las figuras del lienso
        for i,figura in enumerate(figurasCompletas):
            
            # Crear un frame por cada figura
            frameAuxiliar = tkinter.Frame(self.frameDerecho,bd=2,relief="solid")            
            # Ubicarlo al lado derecho
            frameAuxiliar.grid(row=contadorColumnas,column=contadorFilas,sticky="wnse" )            
            
            # Ubicar la información básica de la figura
            tipoFigura = "Cuadrado" if figura.getTipo() == 'CUA' else "Triángulo"
            lblTipo = tkinter.Label(frameAuxiliar,text=tipoFigura)
            lblTipo.grid(row=0,column=0,sticky="nsew")
            
            imagenOriginal = Image.open("./assets/img/CUA.png") if figura.getTipo() == 'CUA' else Image.open("./assets/img/TRI.png")            
            imagenRedimensionada = imagenOriginal.resize((70,70))
            logoFigura = ImageTk.PhotoImage(imagenRedimensionada)        
            self.lblLogoFigura = tkinter.Label(frameAuxiliar,image=logoFigura)
            self.lblLogoFigura.image = logoFigura        
            self.lblLogoFigura.grid(row=1,column=0,sticky="nsew")
            
            btnEditarPuntos = tkinter.Button(frameAuxiliar,text="Editar",command=partial(ActualizarFigura,self,pFigura=figura,pIdFigura=i,referencia_controlador=self.controlador))
            btnEditarPuntos.grid(row=2,column=0,sticky="nsew")
            
            # Ubicar los elementos en el frame
            j = 3
            for punto in figura.getPuntos():
                lblX = tkinter.Label(frameAuxiliar,text="X -> "+str(punto.getX()))
                lblX.grid(row=j,column=0,sticky="w")
                
                lblY = tkinter.Label(frameAuxiliar,text="Y -> "+str(punto.getY()))
                lblY.grid(row=j+1,column=0,sticky="w")                
                
                j += 2
                
            # Incrementar el contador de columnas
            contadorColumnas += 1
            
            # Acumular el frame creado para la figura
            self.framesFiguras.append(frameAuxiliar)
            
            #Revisar para reiniciar
            if contadorColumnas == numeroColumnas:
                contadorFilas += 1
                contadorColumnas = 0
                
            
        
    def agergarBoton(self):
        
        self.botonesDinamicos.append(
                tkinter.Button(
                self.frameDerecho,
                text="Figura "+str(len(self.botonesDinamicos))            
            )            
        )
        
        self.botonesDinamicos[-1].grid(
            row=len(self.botonesDinamicos)-1,
            column=0,
            sticky="e",
        )
        
        