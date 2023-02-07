# python3 -m pytest tests/test_word_search.py
def exists_word(word, instance):
    words_list = []

    for lines_word in range(0, instance.__len__()):
        data_lines = instance.search(lines_word)["linhas_do_arquivo"]
        data_file = instance.search(lines_word)["nome_do_arquivo"]
        format = {
            "palavra": word,
            "arquivo": data_file,
            "ocorrencias": []
        }

        for line in data_lines:
            if word.lower() in line.lower():
                format["ocorrencias"].append(
                    {"linha": data_lines.index(line) + 1})

        if len(format["ocorrencias"]) != 0:
            words_list.append(format)
    return words_list


def search_by_word(word, instance):
    pass
