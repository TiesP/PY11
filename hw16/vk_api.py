import requests

TOKEN = ''


def get_mutual_friends(target_uid):
    params = {
        'access_token': TOKEN,
        'target_uid': target_uid
    }
    response = requests.get('https://api.vk.com/method/friends.getMutual', params)
    list_response = response.json()['response']
    list_mutual_friends = []
    for cur_id in list_response:
        list_mutual_friends.append({
            'id': cur_id,
            'url': 'https://vk.com/id{}'.format(cur_id)
        })
    return list_mutual_friends


mutual_friends = get_mutual_friends(4442387)
print(mutual_friends)
