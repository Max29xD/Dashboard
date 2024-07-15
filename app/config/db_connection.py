from sqlalchemy import create_engine
import app.config.setting as setting

# Conectar a la base de datos
def create_db_engine(auth=True):
    if auth:
        return create_engine(
            f'mssql+pyodbc://{setting.SERVER}/{setting.DATABASE}?driver=ODBC+Driver+17+for+SQL+Server;trusted_connection=yes'
        )
    else:
        return create_engine(
            f'mssql+pyodbc://{setting.USERNAME}:{setting.PASSWORD}@{setting.SERVER}/{setting.DATABASE}?driver=ODBC+Driver+17+for+SQL+Server'
        )