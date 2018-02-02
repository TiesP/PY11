import requests


class YandexMetrikaUser:
    def __init__(self, token):
        self.token = token

    @property
    def counter_list(self):
        headers = {
            'Authorization': 'OAuth {}'.format(self.token),
            'Content-Type': 'application/json'
        }
        url = 'https://api-metrika.yandex.ru/management/v1/counters'
        response = requests.get(url, headers=headers, params={'pretty': 1})
        counters = response.json()['counters']
        return [count['id'] for count in counters]


class YandexMetrikaCounter:
    def __init__(self, user):
        self.url = 'https://api-metrika.yandex.ru/stat/v1/data'
        self.counter_id = user.counter_list[0]
        self.token = user.token

    def get_headers(self):
        return {
            'Authorization': 'OAuth {}'.format(self.token),
            'Content-Type': 'application/json'
        }

    def get_params(self, metrics):
        return {
            'ids': self.counter_id,
            'metrics': metrics,
            'date1': '2018-02-02'  # с даты установки счетчика
        }

    def get_data(self, metrics):
        headers = self.get_headers()
        url = 'https://api-metrika.yandex.ru/stat/v1/data'
        params = self.get_params(metrics)
        response = requests.get(url, params=params, headers=headers)
        return response.json()['totals'][0]

    @property
    def visits(self):
        return 'visits: {}'.format(self.get_data('ym:s:visits'))

    @property
    def pageviews(self):
        return 'pageviews: {}'.format(self.get_data('ym:s:pageviews'))

    @property
    def users(self):
        return 'users: {}'.format(self.get_data('ym:s:users'))


TOKEN = ''
user = YandexMetrikaUser(TOKEN)
counter = YandexMetrikaCounter(user)

print(counter.visits)
print(counter.pageviews)
print(counter.users)
