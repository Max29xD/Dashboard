from app.config.db_connection import create_db_engine
from dash import Dash, dcc, html
import pandas as pd
from app.query.query import query_zero
from app.conts.table_names import table_names

engine = create_db_engine(auth=True)

print('Database connected')

# Ejecutar la consulta y obtener el DataFrame de las tablas
df = {}
with engine.connect() as connection:
    for table in table_names:
        df[table] = pd.read_sql(f'SELECT * FROM {table}', connection)

usuario = df['usuario']
despachador = df['despachador']

print(despachador)

# Dashboard
app = Dash(__name__)

"""
app.layout = html.Div([
    html.H1(children='Dashboard', style={'textAlign': 'center'}),
    dcc.Graph(
        id='graph_one',
        figure={
            'data': [
                {'x': df['nombres'], 'y': df['id'], 'type': 'bar', 'name': 'SF'},
            ],
            'layout': {
                'title': 'Gráfico #1'
            }
        }
    ),
    dcc.Graph(
        id='graph_two',
        figure={
            'data': [
                {'x': df['nombres'], 'y': df['id'], 'type': 'bar', 'name': 'SF'},
            ],
            'layout': {
                'title': 'Gráfico #2'
            }
        }
    ),
    dcc.Graph(
        id='graph_three',
        figure={
            'data': [
                {'x': df['nombres'], 'y': df['id'], 'type': 'bar', 'name': 'SF'},
            ],
            'layout': {
                'title': 'Gráfico #3'
            }
        }
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True) """