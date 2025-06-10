import pandas as pd
from domain.dataset import Dataset
import json

class DatasetJson(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)
        
   
    def cargar_datos(self):
        try:

            # Leer el JSON con manejo de errores
         
            with open(self.fuente, "r", encoding="utf-8") as archivo:
                djson = json.load(archivo)
            
            def es_lista(x):
                return isinstance(x, list)      

            # Convertir a DataFrame con validación de estructura
            if isinstance(djson, dict):
                for key, value in djson.items():
                    if es_lista(value):
                        print(key)
                        self.datos = pd.json_normalize(djson[key])

            print("JSON cargado correctamente.")
            return super().cargar_datos()

        except FileNotFoundError:
            print("Error: Archivo no encontrado.")
        except json.JSONDecodeError:
            print("Error: El archivo no tiene un formato JSON válido.")
        except Exception as e:
            print(f"Error inesperado: {e}")        
