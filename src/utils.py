from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

# load the .env file variables
load_dotenv()


def db_connect():
    import os
    engine = create_engine(os.getenv('DATABASE_URL'))
    engine.connect()
    return engine

def contar_modelos(grid):
    num_models = 1

    for param, values in grid.items():
        num_models *= len(values)

    return num_models
