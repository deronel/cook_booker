import os
def read_cook_book(file):
    data = {}
    key = ['ingredient_name', 'quantity', 'measure']
    with open(file, 'r', encoding='utf-8') as f:
        while True:
            ingredients = []
            name = f.readline().rstrip()
            if not name:
                break
            ingredient_count = f.readline().rstrip()
            for i in range(int(ingredient_count)):
                ing = f.readline().rstrip()
                ing_list = ing.strip().split("|")
                ingredient = dict(zip(key, ing_list))
                ingredient['quantity'] = int(ingredient['quantity'])
                ingredients.append(ingredient)
            data[name] = ingredients
            f.readline().rstrip()
    return data


file = 'c_book.txt'
data = read_cook_book(file)
print(data)


# print(read_cook_book('c_book.txt'))

def get_shop_list_by_dishes(dishes, person_count):
    """
    :param dishes: список блюд из cook_book
    :param person_count: количество персон для кого мы будем готовить:
    :return: словарь с названием ингредиентов и его количества для блюда.
    типа
{
  'Картофель': {'measure': 'кг', 'quantity': 2},
  'Молоко': {'measure': 'мл', 'quantity': 200},
  'Помидор': {'measure': 'шт', 'quantity': 4},
  'Сыр гауда': {'measure': 'г', 'quantity': 200},
  'Яйцо': {'measure': 'шт', 'quantity': 4},
  'Чеснок': {'measure': 'зубч', 'quantity': 6}
}
    """
    cook_dict = {}
    for dish in dishes:
        if dish in data:
            for ingress_diets in data[dish]:
                dict_ing = {}
                if ingress_diets['ingredient_name'] in cook_dict:
                    quantity = cook_dict[ingress_diets['ingredient_name']].get('quantity') + \
                               ingress_diets['quantity'] * person_count
                    cook_dict[ingress_diets['ingredient_name']].update(quantity=quantity)
                else:
                    dict_ing['measure'] = ingress_diets['measure']
                    dict_ing['quantity'] = ingress_diets['quantity'] * person_count
                    cook_dict[ingress_diets['ingredient_name']] = dict_ing
    return cook_dict



print(get_shop_list_by_dishes({'Омлет', 'Фахитос', 'Запеченный картофель'}, 4))


def create_combined_list(directory):
    file_list = os.listdir(directory)
    combined_list = []

    for file in file_list:
        with open(directory + "/" + file) as cur_file:
            combined_list.append([file, 0, []])
            for line in cur_file:
                combined_list[-1][2].append(line.strip())
                combined_list[-1][1] += 1

    return sorted(combined_list, key=lambda x: x[2], reverse=True)


def create_file_from_directory(directory, filename):
    with open(filename + 'c_book .txt', 'w+') as newfile:
        for file in create_combined_list(directory):
            newfile.write(f'File name: {file[0]}\n')
            newfile.write(f'Length: {file[1]} string(s)\n')
            for string in file[2]:
                newfile.write(string + '\n')
            newfile.write('-------------------\n')


create_file_from_directory('text', 'mytext')









                






