from services.config import *
from services.utils import *

missing_folders = ["src","static","img","uploads","games"]


STATIC_PATH_GAMES = SEPARATOR_PATH.join(missing_folders[1:len(missing_folders)]) + SEPARATOR_PATH


print( STATIC_PATH_GAMES)