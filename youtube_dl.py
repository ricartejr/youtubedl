from os import makedirs, path, system
from pytube import Playlist, YouTube
from pytube.cli import on_progress
from funciones.func import fix_jr
from rich.console import Console


system('cls')
cont_total = 0
contador_videos = 0
contador_error = 0
lista_de_errores = ['']
c_padrao = r'D:/VIDEOS/Videos YT/1 - Python Downloads'

C = Console()
C.rule('YOUTUBE - DOWNLOADS')

try:
    url_yt = Playlist(C.input('[r b] YOUTUBE URL [/] -> '))
    print('')
    for video in url_yt.video_urls:
        # print(f'{video}')
        try:
            video = YouTube(video, on_progress_callback=on_progress)
            titulo_v = fix_jr(video.title)
            autor_v = video.author
            p_autor = url_yt.owner
            p_titulo = url_yt.title
            pastas = f'{path.abspath(c_padrao + "/" + p_autor + "/" + fix_jr(p_titulo))}'
            makedirs(pastas, exist_ok=True)
            video = video.streams.get_by_itag(22)
            new_name = f'{autor_v + " - " + titulo_v}.mp4'
            C.print(
                f'-> [r b] {autor_v} [/] - [bright_red on grey93 b] {p_titulo} [/] - [bright_green on grey93 b] {titulo_v} [/]')
            video.download(output_path=pastas, filename=new_name)
        except KeyboardInterrupt:
            system('cls')
            C.print('[r b] Cancelado por usuario [/]\n')
            break
        except AttributeError:
            # ! Contador de errores y agrega a una lista
            contador_error += 1
            lista_de_errores.append(f'{autor_v} - {titulo_v}')
            pass
        else:
            # ! Si descarga sin problema adiciona al contador
            contador_videos += 1
        finally:
            # ! Conta el total de interaciones urls
            cont_total += 1
            pass
    else:
        C.rule('')
        C.print(f'\n-> Download [ {contador_videos} / {cont_total} ]\n')
        if contador_error >= 1:
            C.print(
                f'-> Errores Total [bright_red on grey93 b] {contador_error} [/]')
            for nome in lista_de_errores:
                print(f'{nome}')
            else:
                print('')
        else:
            C.print(f'-> Errores Total [bright_red on grey93 b] 0 [/]\n\n')
except KeyError:
    C.print('-> ERROR - Playlist Invalida')

# link de prueba 3 videos
# https://www.youtube.com/playlist?list=PLFHT61jJ5V-4VyZyqUlXAdADsHD2W2NZa

# link con 60 videos
# https://www.youtube.com/playlist?list=PLZF7DG3oXtDgylbBYyTxrZaHUhn4WHVH8
