import xml.etree.ElementTree as ET
import chardet


def clean_text(text):
    new_text = text
    new_text = new_text.replace('<a href="//www.votpusk.ru/country/country.asp?CN=CY">', ' ')
    new_text = new_text.replace('<br>/', ' ')
    new_text = new_text.replace('<br>', ' ')
    new_text = new_text.replace('/', ' ')
    new_text = new_text.replace(',', ' ')
    return new_text


def get_words_from_xml(data_xml):
    # формат: (rss) = channel - item - description
    list_words = []
    items = data_xml.findall('channel/item/description')
    for item in items:
        description = clean_text(item.text)
        list_words.extend(description.split())
    return list_words


def find_big_words(min_length, data_xml):
    list_words = get_words_from_xml(data_xml)
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


def show_top_words(count, data_xml):
    dict_words = find_big_words(6, data_xml)
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
        data_xml = ET.fromstring(text)
        return data_xml


def process_file(file_name):
    print('для файла: ', file_name)
    data_xml = open_file(file_name)
    show_top_words(10, data_xml)


def main():
    print('топ 10 по частоте слов длиннее 6 символов')
    process_file('newsafr.xml')
    process_file('newscy.xml')
    process_file('newsfr.xml')
    process_file('newsit.xml')


main()
