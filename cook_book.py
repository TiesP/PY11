def get_ingredient(ingredient_string):
    fields = ingredient_string.split('|')
    return {'ingredient_name': fields[0].strip(),
            'quantity': int(fields[1].strip()),
            'measure': fields[2].strip()}


def add_ingredients(f):
    ingredient_string = f.readline().strip()
    list_ingredients = []
    while '|' in ingredient_string:
        list_ingredients.append(get_ingredient(ingredient_string))
        ingredient_string = f.readline().strip()
    return list_ingredients


def add_dish(cook_book, line, f):
    dish_name = line.strip().lower()
    dish = {'person_count': int(f.readline()),
            'ingredients': add_ingredients(f)}
    cook_book[dish_name] = dish


def get_cook_book():
    cook_book = {}
    with open('recipes.txt', encoding='utf8') as f:
        for line in f:
            add_dish(cook_book, line, f)
    return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    for dish_name in dishes:
        dish = cook_book[dish_name]
        for ingredient in dish['ingredients']:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] *= person_count / dish['person_count']
            ingredient = new_shop_list_item['ingredient_name']
            if ingredient not in shop_list:
                shop_list[ingredient] = new_shop_list_item
            else:
                shop_list[ingredient]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list():
    cook_book = get_cook_book()
    print('В меню на сегодня:')
    for key in cook_book:
        print(key)
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    shop_list = get_shop_list_by_dishes(cook_book, dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()
