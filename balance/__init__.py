import os

from flask import Flask

RUTA_FICHERO = os.path.join('balance', 'data', 'movimientos.csv')

app = Flask(__name__)
print('El nombre de la app flask es:', __name__)
