import re
from os import makedirs, path
from rich.console import Console

C = Console()


class MyConfig:
    def __init__(self, yt):
        self.author = yt.author
        self.title = yt.title
        self.yt = yt

    def crea_carpeta(self, c_padron):
        self.path_carpetas = f'{path.abspath(c_padron + "/" + self.author)}'
        makedirs(self.path_carpetas, exist_ok=True)

    def dl(self):
        yt_filter = self.yt.streams.get_by_itag(22)
        new_name = f'{self.author + " - " + fix_jr(self.title)}.mp4'
        if path.isfile(self.path_carpetas + '/' + new_name) != True:
            C.print(f'\n[r b] {new_name[:-4]}')
            yt_filter.download(
                output_path=self.path_carpetas, filename=new_name)
            print('\n')
        else:
            # ! File Exist
            C.print(f'\n[r b] {new_name[:-4]} [/]\n')


def fix_jr(nome):
    nome = re.sub(r'[\W_]+', ' ', nome)
    return f'{nome.strip().capitalize()}'
