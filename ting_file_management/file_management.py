import sys
# python3 -m pytest tests/test_file_management.py
# https://stackoverflow.com/questions/5574702/how-do-i-print-to-stderr-in-python
# http://devfuria.com.br/python/manipulando-arquivos-de-texto/


def txt_importer(path_file):
    try:
        if path_file.endswith(".txt"):
            with open(path_file) as file:
                data = file.read().split("\n")
                return list(data)
        else:
            print("Formato inválido", file=sys.stderr)
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
