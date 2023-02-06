import sys
from ting_file_management.file_management import txt_importer
# python3 -m pytest tests/test_file_process.py


def process(path_file, instance):
    file_txt_lines = txt_importer(path_file)
    qty_lines = len(file_txt_lines)
    transform_to_dict_format = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": qty_lines,
        "linhas_do_arquivo": file_txt_lines,
    }

    for file in range(len(instance)):
        searched_file = instance.search(file)
        if searched_file["nome_do_arquivo"] == path_file:
            return None

    instance.enqueue(transform_to_dict_format)

    return print(transform_to_dict_format, file=sys.stdout)


def remove(instance):
    if instance.__len__() != 0:
        file_poped = instance.dequeue()
        path_file = file_poped["nome_do_arquivo"]
        return print(
            f"Arquivo {path_file} removido com sucesso", file=sys.stdout)
    else:
        return print('Não há elementos', file=sys.stdout)


def file_metadata(instance, position):
    try:
        searched_file = instance.search(position)
        return print(searched_file)
    except IndexError:
        return print("Posição inválida", file=sys.stderr)
