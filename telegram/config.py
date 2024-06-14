from os import environ, path
import sys
from os.path import join, dirname, exists
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
if exists(dotenv_path):
    env = load_dotenv(dotenv_path)
path = path.abspath(path.join(path.dirname(__file__), ".."))
if not path in sys.path:
    sys.path.insert(1, path)
del path


ADMIN_ID = environ["ADMIN_ID"]
BOT_TOKEN = environ["BOT_TOKEN"]
PATH_TO_TEMPORARY_STORAGE = "./temporary_storage_of_graphics"
