# Импортируем всё содержимое из utils
# Также импортируем json, чтобы прочитать файл
from utils import *
import json

# Открываем json-файл
with open('operations.json', 'r', encoding='utf-8') as file:
    text = json.load(file)
    # Фильтруем по 'EXECUDE' и сортируем по дате
    information = filter_and_sorted(text)

# Выводим конечное сообщение на экран
print(prepare_message(information))