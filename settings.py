import os
from os import path
import dotenv


dotenv_path = path.join(path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)

def getEnv(key):
    return os.environ.get(key)