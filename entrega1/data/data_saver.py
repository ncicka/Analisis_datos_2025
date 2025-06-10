import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from decouple import config

class  DataSaver:
    def __init__(self):
        user = config('DB_USER')
        password = config('DB_PASSWORD')
        host=config('DB_HOST')
        port = config('DB_PORT')
        database=config('DB_NAME')
        
        url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        self.engine = create_engine(url)
        

    def guardar_dataframe(self, df, nombre_tabla):
        if df is None:
            print(f"No se puede guardar un dataframe vacío para {nombre_tabla}.")
            return
        
        if not isinstance(df, pd.DataFrame):
            print(f"tipo invalido se esperaba un dataframe, se recibio {type(df)}")
            return 

        try:
            df.to_sql(nombre_tabla, con=self.engine, if_exists='replace', index=False)
            
            print(f"Se guardó la tabla {nombre_tabla} en la base de datos.")
        
        except SQLAlchemyError as e:
            print(f"Error al guardar el dataframe en la base de datos: {e}")