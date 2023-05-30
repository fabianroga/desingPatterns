from abc import ABC, abstractmethod 


#A continuación crearemos una interfaz Fabricante, que permitirá crear Microcontroladores a toda clase que la implemente:
class FabricaAbstracta(ABC):
    
    @abstractmethod
    def crearMemoria(self):
        pass

    @abstractmethod
    def crearProcesador(self):
        pass
    
    
        
class Memoria(ABC):
    
    def implementacion(self):
        print("..instalando memoria")
    
    @abstractmethod
    def operacion(self):
        pass
    
class Procesador(ABC):
    def implementacion(self):
        print("..instalando procesador")

    @abstractmethod
    def operacion(self):
        pass
    




class MemoriaAMD(Memoria):
    def __init__(self,name):
        self.name = name
    
    def operacion(self):
        print("....operando memoria AMD de"+ self.name)


class MemoriaIntel(Memoria):
    def __init__(self,name):
        self.name = name
        
    def operacion(self):
        print("....operando memoria Intel" + self.name)
        
        
        
        
class ProcesadorAMD(Procesador):
    def __init__(self,name):
        self.name = name
        
    def operacion(self):
        print("....operando procesador AMD" + self.name)

class ProcesadorIntel(Procesador):
    def __init__(self,name):
        self.name = name
        
    def operacion(self):
        print("....operando procesador Intel" + self.name)
        
        
    
    
# fabrica abstracta (fabrica principal) invoca las fabricas concretas de cada tipo

class FabricaAMD(FabricaAbstracta):
    
    @staticmethod
    def crearMemoria(nombre):
        return MemoriaAMD(nombre)
        
    @staticmethod
    def crearProcesador(nombre):
        return ProcesadorAMD(nombre)
    
   
class FabricaIntel(FabricaAbstracta):
    @staticmethod
    def crearMemoria(nombre):
        return MemoriaIntel(nombre)
    
    @staticmethod
    def crearProcesador(nombre2):
        return ProcesadorIntel(nombre2)
    
    


# clases para representar cualquier tipo de microcontrolador y las operacion qeu cada fabrica quiera para su microcontroldaor

    

if __name__ == "__main__":
    
    
    fabrica = FabricaAMD()
    
    partes = [fabrica.crearMemoria("20"), fabrica.crearProcesador(" melo")]
    for p in partes:
        p.implementacion()
        p.operacion()
 
    
    