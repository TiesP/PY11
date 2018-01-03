import chardet


def find_big_words(min_length, file_text):
    list_words = file_text.split()
    words = {}
    for word in list_words:
        if len(word) > min_length:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
    return words


def dict_to_list(dict_words):
    list_words = []
    for word in dict_words:
        list_words.append({'word': word, 'count': dict_words[word]})
    return sorted(list_words, key=lambda k: k["count"], reverse=True)


def show_top_words(count, file_text):
    dict_words = find_big_words(6, file_text)
    sort_words = dict_to_list(dict_words)
    i = 1
    for word in sort_words:
        print(word['word'], word['count'])
        i += 1
        if i > count:
            break


def open_file(file_name):
    with open(file_name, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        return data.decode(result['encoding'])


def process_file(file_name):
    print('для файла: ', file_name)
    file_text = open_file(file_name)
    show_top_words(10, file_text)


def main():
    print('топ 10 по частоте слов длиннее 6 символов')
    process_file('newsafr.txt')
    process_file('newscy.txt')
    process_file('newsfr.txt')
    process_file('newsit.txt')


main()
