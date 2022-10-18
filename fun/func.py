import os
import re
import shutil
from time import sleep


def fix_jr(nome):
    nome = re.sub(r'[\W_]+', ' ', nome)
    return f'{nome.strip().capitalize()}'


def copycopy(copy_arq, des_arq, path_local, bus_palabra, archivo):
    extens = copy_arq[-3:]
    try:
        os.makedirs(
            f'{path_local}/{bus_palabra}/{archivo[-3:]}', exist_ok=True)
        sleep(0.5)
        shutil.copy2(copy_arq, f'{des_arq}/{extens}')
    # If source and destination are same
    except shutil.SameFileError:
        print("Source and destination represents the same file.")

    # If destination is a directory.
    except IsADirectoryError:
        print("Destino es una carpeta.")

    # If there is any permission issue
    except PermissionError:
        print("Permision negada.")

    except KeyboardInterrupt:
        print('Cancelado por el usuario')
    # For other errors
    except:
        print("Error al copiar el archivo.")
