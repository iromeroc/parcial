class Clientes:
    def __init__(self, nombre: str, apellido: str, id: int, direccion: str, telefono: int ):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id
        self.direccion = direccion
        self.telefono = telefono
        self.paquetes = []
    
    def agregar_paquetes(self, paquete):
        if len(self.paquetes) < 5:
            self.paquetes.append(paquete)
        else:
            print("El cliente ha alcanzado el límite de paquetes.")



#1c
#2c
#3c
#4b