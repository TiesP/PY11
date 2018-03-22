import requests
import time
import json

TOKEN = '7b23e40ad10e08d3b7a8ec0956f2c57910c455e886b480b7d9fb59859870658c4a0b8fdc4dd494db19099'
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
        err_code = response['error']['error_code']
        if err_code == 7 or err_code == 18:
            print('error! ', response)
            if type_data == 'count':
                return 0
            else:
                return []
        get_data.count_errors += 1
        get_data.time_to_query *= 2
        return get_data(func, params, type_data)
    return response['response'][type_data]


def get_groups_ext(id_user):
    params = {
        'access_token': TOKEN,
        'user_id': id_user,
        'v': '5.73',
        'extended': 1
    }
    return get_data('groups.get', params, 'items')


def get_groups(id_user):
    params = {
        'access_token': TOKEN,
        'user_id': id_user,
        'v': '5.73'
    }
    return get_data('groups.get', params, 'items')


def get_friends():
    params = {
        'access_token': TOKEN,
        'user_id': USER_ID,
        'v': '5.73'
    }
    return get_data('friends.get', params, 'items')


def get_members(group_id):
    params = {
        'access_token': TOKEN,
        'v': '5.73',
        'group_id': group_id
    }
    return get_data('groups.getMembers', params, 'count')


def save_file(result):
    with open('groups.json', 'w', encoding='utf8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)


def info_error():
    print('Кол-во ошибок превысило допустимое!')
    print('Корректные данные получить не удалось!')


def check(data):
    if data is None:
        info_error()
        return False
    return True


def get_result_groups():
    groups = get_groups(USER_ID)
    if not check(groups):
        return []
    groups_s = set(groups)
    friends = get_friends()
    if not check(friends):
        return []
    count = 0
    for f_id in friends:
        print('Этап 1 из 2. Осталось {0} из {1}'.format(len(friends) - count, len(friends)))
        count += 1
        f_groups_s = set(get_groups(f_id))
        # определяем общие (с текущим другом) группы
        common_groups_s = groups_s & f_groups_s
        # вычисляем разницу множеств и оставляем только группы, в которых не состоит друг
        groups_s -= common_groups_s
    return list(groups_s)


def find_by_id(find_id, cur_list):
    for obj in cur_list:
        if obj['id'] == find_id:
            return obj


def main():
    groups_ext = get_groups_ext(USER_ID)
    if not check(groups_ext):
        return
    result = []
    count = 0
    groups = get_result_groups()
    for group_id in groups:
        print('Этап 2 из 2. Осталось {0} из {1} групп'.format(len(groups) - count, len(groups)))
        count += 1
        group = find_by_id(group_id, groups_ext)
        group_name = group['name']
        group_members_count = get_members(group_id)
        if not check(group_members_count):
            return
        result.append({'name': group_name, 'gid': group_id, 'members_count': group_members_count})
    save_file(result)


main()
