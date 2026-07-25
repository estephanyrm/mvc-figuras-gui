# Importado de librerías
import sys

# Importado de abstracciones de consola
from controller.AppConsole import AppConsole
from view.console.Mensaje import Mensaje

# Importado de abstracciones de GUI
from controller.AppGUI import AppGUI


# Punto de entrada de la aplicación

# Establecer modo por defecto
modo = 'consola'

"""# Obtener información de consola
modo = sys.argv[1]"""

# Inicializar contenedor de la aplicación
app = None

# Establecer modo de ejecución de la aplicación
if modo == 'consola':    
    app = AppConsole()
    app.mainloop()
elif modo == 'GUI':
    app = AppGUI()
    app.mainloop()
else:
    # Reportar error por consola
    Mensaje.error("Modo de iniciación de la app inválido!")
    # Retornar error al sistema operativo
    sys.exit(0)
    

