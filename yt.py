from pytube import YouTube, Playlist
from pytube.cli import on_progress
from rich.console import Console
from funciones.func import fix_jr, MyConfig
from os import system, makedirs, path, walk

"""
https://www.youtube.com/watch?v=6vEUp3UFLIw
https://www.youtube.com/playlist?list=PLFHT61jJ5V-4VyZyqUlXAdADsHD2W2NZa
"""

system('cls')
C = Console()
url = C.input('[bright_red on bright_white b] YOUTUBE URL -> [/] ')
c_padron = r'D:/VIDEOS/Videos YT/1 - Python Downloads'

try:
    if url.find('list') != -1:
        ...
    else:
        yt = YouTube(url, on_progress_callback=on_progress)
        connect = MyConfig(yt)
        # ! Carpetas
        connect.crea_carpeta(c_padron)
        # ! Config DL
        connect.dl()
except KeyboardInterrupt:
    C.print('\n[b r] Cancelado por el usuario [/]\n')
else:
    ...
finally:
    ...
