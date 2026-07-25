class Mensaje:
    
    @classmethod
    def informacion(cls,informacion='')->None:
        print()
        print("---------------------------")
        print(f"Info: {informacion}")
        print("---------------------------")
        print()
        
    @classmethod
    def error(cls,informacion='')->None:
        print()
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print(f"Error: {informacion}")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print()        