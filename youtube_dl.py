from os import makedirs, path, system
from pytube import Playlist, YouTube
from pytube.cli import on_progress
from funciones.func import fix_jr
from rich.console import Console


system('cls')
contador_total = 0
contador_descargas = 0
contador_error = 0
lista_de_errores = ['']

c_padrao = r'D:/VIDEOS/Videos YT/1 - Python Downloads'

C = Console()
C.rule('YOUTUBE - DOWNLOADS')
url = C.input('[r b] YOUTUBE URL [/] -> ')
print('')
try:
    p_url = Playlist(url)
    for video in p_url.video_urls:
        try:
            video = YouTube(video, on_progress_callback=on_progress)
            titulo_v = fix_jr(video.title)
            autor_v = video.author
            p_autor = p_url.owner
            p_titulo = p_url.title
            pastas = f'{path.abspath(c_padrao + "/" + p_autor + "/" + fix_jr(p_titulo))}'
            makedirs(pastas, exist_ok=True)
            video = video.streams.get_by_itag(22)
            new_name = f'{autor_v + " - " + titulo_v}.mp4'
            C.print(
                f'-> [r b] {autor_v} [/] [bright_red on grey93 b] {p_titulo} [/] [bright_green on grey93 b] {titulo_v} [/]')
            video.download(output_path=pastas, filename=new_name)
        except KeyboardInterrupt:
            C.print('[r b] Cancelado por usuario [/]\n')
            break
        except AttributeError:
            # ! Contador de errores y agrega a una lista
            contador_error += 1
            lista_de_errores.append(f'{autor_v} - {titulo_v}')
            pass
        else:
            # ! Si descarga sin problema adiciona al contador
            contador_descargas += 1
        finally:
            # ! Conta el total de interaciones urls
            contador_total += 1
            pass
    else:
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
except KeyError as e_error:
    C.print(f'\n Error -> [bright_red on grey93 b]{e_error =}[/] \n')
