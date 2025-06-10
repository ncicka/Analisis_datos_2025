import pandas as pd
from domain.dataset import Dataset

class DatasetExcel(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)
        
    def cargar_datos(self):
        try:
            df = pd.read_excel(self.fuente)
            self.datos = df
            print("Excel cargado")
            
        except FileNotFoundError:
            print("Error: El archivo excel no se encontró. Verifica el nombre y la ubicación.")    
        except Exception as e:
            print(f"Error al cargar los datos Excel: {e}")
        return super().cargar_datos()
