from pytube import YouTube, Playlist
from pytube.cli import on_progress
from rich.console import Console
from funciones.func import fix_jr
from os import system, makedirs, path
"""
https://www.youtube.com/watch?v=6vEUp3UFLIw
https://www.youtube.com/playlist?list=PLFHT61jJ5V-4VyZyqUlXAdADsHD2W2NZa
"""

system('cls')
C = Console()
url = C.input('[bright_red on bright_white b] URL -> [/] ')
c_padrao = r'D:/VIDEOS/Videos YT/1 - Python Downloads'

if url.find('list') != -1:
    print('Encontrou')
else:
    yt = YouTube(url, on_progress_callback=on_progress)
    autor_v = fix_jr(yt.author)
    titulo_v = fix_jr(yt.title)
    # ! creando carpetas
    carpetas = f'{path.abspath(c_padrao + "/" + autor_v)}'
    makedirs(carpetas, exist_ok=True)
    # ! config Downloads
    yt = yt.streams.get_by_itag(22)
    renomear = f'{autor_v + " - " + titulo_v}.mp4'
    print(renomear[:-4])
    yt.download(output_path=carpetas, filename=renomear)
