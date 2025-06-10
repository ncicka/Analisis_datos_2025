from os import path
from domain.dataset_csv import DatasetCSV
from domain.dataset_excel import DatasetExcel
from domain.dataset_json import DatasetJson
from data.data_saver import DataSaver  


# Ruta de CSV
csv_path = path.join(path.dirname(__file__),"files/indices-bursatiles.csv")
excel_path = path.join(path.dirname(__file__),"files/proveedores.xlsx")
json_path = path.join(path.dirname(__file__),"files/personas.json")

# Cargar y transformar
csv = DatasetCSV(csv_path)
csv.cargar_datos()
csv.mostrar_resumen()

excel = DatasetExcel(excel_path)
excel.cargar_datos()
excel.mostrar_resumen()

json = DatasetJson(json_path)
json.cargar_datos()
json.mostrar_resumen()

# Guardar en base de datos
#esto es de sqlite3
#db = DataSaver("db/recoleccion.db")

# para mysql solo se instancia la clase
db = DataSaver()
db.guardar_dataframe(csv.datos, "indices_bursatiles_csv")
db.guardar_dataframe(excel.datos, "proveedores_xlsx")
db.guardar_dataframe(json.datos, "personas_json")   

