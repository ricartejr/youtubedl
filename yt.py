from pytube import YouTube, Playlist
from pytube.cli import on_progress
from rich.console import Console
from funciones.func import fix_jr, MyConfig
from os import system, makedirs, path, walk

"""
https://www.youtube.com/watch?v=6vEUp3UFLIw
https://www.youtube.com/playlist?list=PLFHT61jJ5V-4VyZyqUlXAdADsHD2W2NZa
https://www.youtube.com/watch?v=HheT7RCxjDE&list=PLBAIwM2891DqJd0dAFPI93gwzFnbxVeiU
"""

system('cls')
C = Console()
url = C.input('[bright_red on bright_white b] YOUTUBE URL -> [/] ')
c_padron = r'D:/VIDEOS/Videos YT/1 - Python Downloads'

contador_total = 0
contador_descargas = 0
contador_error = 0
lista_de_errores = ['']

if url.find('playlist') != -1:
    p_url = Playlist(url)
    for video in p_url.video_urls:
        try:
            video = YouTube(video, on_progress_callback=on_progress)

            title_v = fix_jr(video.title)
            author_v = video.author
            author_p = p_url.owner
            title_p = p_url.title

            pastas = f'{path.abspath(c_padron + "/" + author_p + "/" + fix_jr(title_p))}'
            makedirs(pastas, exist_ok=True)

            video = video.streams.get_by_itag(22)
            new_name = f'{author_v + " - " + title_v}.mp4'
            C.print(
                f'\n\n-> [r b] {author_v} [/] [bright_red on grey93 b] {title_p} [/] [bright_green on grey93 b] {title_v} [/]')
            video.download(output_path=pastas, filename=new_name)
        except KeyboardInterrupt:
            C.print('\n[r b] Cancelado por usuario [/]\n')
            break
        except AttributeError:
            # ! Contador de errores y agrega a una lista
            contador_error += 1
            lista_de_errores.append(f'{author_v} - {title_v}')
        else:
            # ! Si descarga sin problema adiciona al contador
            contador_descargas += 1
        finally:
            # ! Conta el total de interaciones urls
            contador_total += 1
    else:
        print('')
        C.rule('')
        C.print(f'\n-> Download [ {contador_descargas} / {p_url.length} ]\n')
        C.print(
            f'-> Videos Privados [ [bright_red on grey93 b] {p_url.length - contador_descargas} [/] ]\n')
        if contador_error >= 1:
            C.print(
                f'-> Errores Total [bright_red on grey93 b] {contador_error} [/]')
            for nome in lista_de_errores:
                print(f'{nome}')
            else:
                print('')
        else:
            C.print(f'-> Errores Total [ [bright_red on grey93 b] 0 [/] ]\n\n')
else:
    yt = YouTube(url, on_progress_callback=on_progress)
    connect = MyConfig(yt)
    # ! Carpetas
    connect.crea_carpeta(c_padron)
    # ! Config DL
    connect.dl()
