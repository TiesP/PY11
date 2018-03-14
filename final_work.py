import requests
import time
import json

TOKEN = '5dfd6b0dee902310df772082421968f4c06443abecbc082a8440cb18910a56daca73ac8d04b25154a1128'
USER_ID = 5030613


def is_error(res):
    return True if 'error' in res.keys() else False


def get_data(func, params, type_data):
    if not hasattr(get_data, 'count_errors'):
        get_data.count_errors = 0
    if not hasattr(get_data, 'time_to_query'):
        get_data.time_to_query = 0.05
    if get_data.count_errors > 10:
        return None
    time.sleep(get_data.time_to_query)
    response = requests.get('https://api.vk.com/method/' + func, params).json()
    if is_error(response):
        get_data.count_errors += 1
        get_data.time_to_query *= 2
        return get_data(func, params, type_data)
    return response['response'][type_data]


def get_groups():
    params = {
        'access_token': TOKEN,
        'user_id': USER_ID,
        'v': '5.73',
        'extended': 1
    }
    result = get_data('groups.get', params, 'items')
    return None if result is None else result


def get_members_friends(group_id):
    params = {
        'access_token': TOKEN,
        'v': '5.73',
        'group_id': group_id,
        'filter': 'friends'
    }
    result = get_data('groups.getMembers', params, 'count')
    return None if result is None else result


def get_members(group_id):
    params = {
        'access_token': TOKEN,
        'v': '5.73',
        'group_id': group_id
    }
    result = get_data('groups.getMembers', params, 'count')
    return None if result is None else result


def save_file(result):
    with open('groups.json', 'w', encoding='utf8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)


def info_error():
    print('Кол-во ошибок превысило допустимое!')
    print('Корректные данные получить не удалось!')


def main():
    groups = get_groups()
    if groups is None:
        info_error()
        return
    result = []
    count = 0
    for group in groups:
        count += 1
        print('Обрабатывается {0} из {1}'.format(count, len(groups)))
        group_id = group['id']
        friends_members = get_members_friends(group_id)
        if friends_members is None:
            info_error()
            return
        elif friends_members == 0:
            members_count = get_members(group_id)
            if members_count is None:
                info_error()
                return
            result.append({'name': group['name'], 'gid': group_id, 'members_count': members_count})
    save_file(result)


main()
