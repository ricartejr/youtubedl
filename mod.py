from pytube import Playlist, YouTube
from os import makedirs, path, system
from funciones.func import fix_jr


system('cls')

link_yt = str(input('URL -> '))
c_padron = r'D:/VIDEOS/Videos YT/1 - Python Downloads'
link_playlist = Playlist(link_yt)

lista_de_links = ['']
contador_de_links = 0


for link in link_playlist.video_urls:
    try:
        contador_de_links += 1
        video = YouTube(link)

        title_video = fix_jr(video.title)
        author_video = video.author
        author_playlist = link_playlist.owner
        title_playlist = fix_jr(link_playlist.title)

        check_nome = f'{path.abspath(c_padron + "/" + author_playlist + "/" + title_playlist)}'
        if path.exists(check_nome) != True:
            print(f'Download -> {contador_de_links} - {check_nome}')
        else:
            print(
                f'{contador_de_links} - {path.abspath(check_nome + "/" + author_video + " - " + title_video)}.mp4')
    except KeyboardInterrupt:
        break
    except Exception:
        lista_de_links.append(link)
