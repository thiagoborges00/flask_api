import os
from dynaconf import FlaskDynaconf

here = os.path.dirname(os.path.abspath(__file__))

#para não acontecer o import circular
# vai habilitar o settings.toml
def configure(app):
    FlaskDynaconf(app, extensions_list="EXTENSIONS", root_path=here)
