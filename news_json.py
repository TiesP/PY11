import json
import chardet


def get_words_from_json(data_json):
    # формат: rss - channel - items [ { 'description': ... } ]
    list_words = []
    for item in data_json['rss']['channel']['items']:
        list_words.extend(item['description'].split())
    return list_words


def find_big_words(min_length, data_json):
    list_words = get_words_from_json(data_json)
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


def show_top_words(count, data_json):
    dict_words = find_big_words(6, data_json)
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
        text = data.decode(result['encoding'])
        data_json = json.loads(text)
        return data_json


def process_file(file_name):
    print('для файла: ', file_name)
    data_json = open_file(file_name)
    show_top_words(10, data_json)


def main():
    print('топ 10 по частоте слов длиннее 6 символов')
    process_file('newsafr.json')
    process_file('newscy.json')
    process_file('newsfr.json')
    process_file('newsit.json')


main()
