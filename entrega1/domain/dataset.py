#Clase abstracta de python
from abc import ABC, abstractmethod

class Dataset(ABC):
    def __init__(self, fuente):
        self.__fuente = fuente
        self.__datos = None

    # getter 
    @property
    def datos(self):
        return self.__datos
    
    @datos.setter
    def datos(self, value):
        #hacer validaciones
        self.__datos = value
        if self.validar_datos():
            self.transformar_datos()
    
    @property
    def fuente(self):
        return self.__fuente
    
    # obligar a las subclases a implementar este metodo
    @abstractmethod
    def cargar_datos(self):
        pass

    def validar_datos(self):
        if (self.datos.empty ):
            raise ValueError("El archivo no contiene datos")
        
        if self.datos.isnull().sum().sum() > 0:
            self.datos.fillna(0, inplace=True)

        if self.datos.duplicated().sum() > 0:
            self.__datos.drop_duplicates()
        
        return True

    def transformar_datos(self):
        self.__datos.columns = self.datos.columns.str.lower().str.replace(" ","_")
        for col in self.datos.select_dtypes(include="object").columns:
            self.__datos[col] = self.__datos[col].astype(str).str.strip()
        print("Transformaciones aplicadas")

    def mostrar_resumen(self):
        return print(self.datos.describe(include="all")) if self.datos is not None else print("No hay datos para mostrar")
    
    
