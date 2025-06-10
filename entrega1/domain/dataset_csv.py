import pandas as pd
from domain.dataset import Dataset

class DatasetCSV(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)
        
    
    def cargar_datos(self):
        try:
            df = pd.read_csv(self.fuente)
            self.datos = df
            print("CSV cargado")
        except FileNotFoundError:
            print("Error: El archivo CSV no se encontró. Verifica el nombre y la ubicación.")            
        except Exception as e:
            print(f"Error al cargar los datos CSV: {e}")
        return super().cargar_datos()
