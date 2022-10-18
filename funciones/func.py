import re


def fix_jr(nome):
    nome = re.sub(r'[\W_]+', ' ', nome)
    return f'{nome.strip().capitalize()}'
