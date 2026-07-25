class Punto:
    
    def __init__(self,x:int=0,y:int=0,etiqueta:str='TAG'):
        self.__x = x
        self.__y = y
        self.__etiqueta = etiqueta
    
    def getX(self)->int:
        return self.__x
    
    def getY(self)->int:
        return self.__y
    
    def __str__(self):
        cadena = str()
        cadena += f"--------------\n"
        cadena += f"Etiqueta: {self.__etiqueta}\n"
        cadena += f"x: {self.__x}\n"
        cadena += f"y: {self.__y}\n"
        cadena += f"--------------\n"
        return cadena
    
    