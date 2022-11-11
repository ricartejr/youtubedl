from os import makedirs, path, system
from pytube import Playlist, YouTube
from pytube.cli import on_progress
from funciones.func import fix_jr
from rich.console import Console


system('cls')
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
        contador_videos += 1
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
            # video.download(output_path=pastas, filename=new_name)
        except KeyboardInterrupt:
            system('cls')
            C.print('[r b] Cancelado por usuario [/]\n')
            break
        except AttributeError:
            contador_error += 1
            lista_de_errores.append(f'{autor_v} - {titulo_v}')
        finally:
            pass
            # print(f'\n{"":-<120}')
    else:
        print(f'\n-> Download Total [ {contador_videos} ]\n')
        if contador_error >= 1:
            print(f'-> Errores Total [ {contador_error} ]')
            for nome in lista_de_errores:
                print(nome)
            else:
                print('\n')
        else:
            print(f'-> Errores Total [ 0 ]\n\n')
except KeyError:
    print('-> ERROR - Playlist Invalida')
