#from название файла без py import * - все имена
#from название файла без py import какие-то названия


def get_min_items(items):
    min_item = items[0]
    for item in items[1:]:
        if item < min_item:
            min_item = item
    return min_item


items1 = [1,2,3,4,5]
items2 = list(range(-50,50,2))
print(get_min_items(items1))
print(get_min_items(items2))
