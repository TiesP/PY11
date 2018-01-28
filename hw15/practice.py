import requests


def get_text(file_source):
    with open(file_source) as f:
        return f.read()


def save_text(file_result, text_result):
    with open(file_result, 'w', encoding='utf8') as f:
        f.write(text_result)


def translate_it(file_source, file_result, lang_source, lang_result='ru'):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    params = {
        'key': key,
        'lang': '{}-{}'.format(lang_source, lang_result),
        'text': get_text(file_source),
    }
    response = requests.get(url, params=params).json()
    text_result = ' '.join(response.get('text', []))
    save_text(file_result, text_result)


translate_it('DE.txt', 'DE-RU.txt', 'de')
translate_it('ES.txt', 'ES-RU.txt', 'es')
translate_it('FR.txt', 'FR-RU.txt', 'fr')
