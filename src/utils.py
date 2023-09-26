def filter_and_sorted(data: list) -> list:
    """
    Фильтруем   список словарей по EXECUDE
    Сортируем по дате, сначала новые.
    """
    item = [item for item in data if item.get('state') == 'EXECUTED']
    item.sort(key=lambda x: x.get('date'), reverse=True)
    return item


def prepare_message(inf: list):
    """
    Собираем все данные вместе  и выводим на экран
    """
    for i in inf[0:5]:
        print(get_date(i['date']), i['description'])
        if 'from' not in i.keys():
            print('->', final_mask(i['to']))
            print(i['operationAmount']['amount'], i['operationAmount']['currency']['name'], '\n')
            continue
        print(final_mask(i['from']), '->', final_mask(i['to']))
        print(i['operationAmount']['amount'], i['operationAmount']['currency']['name'], '\n')


def get_date(date: str) -> str:
    """
    Получем дату, работаем, как с типом данных 'str'
    """
    dt = date[0:10].split(sep='-')
    return dt[2] + '.' + dt[1] + '.' + dt[0]


def mask_account_num(msg: str) -> str:
    """
    Маскируем цифры счета, убираем слова
    """
    new = filter(str.isdecimal, msg)
    new_1 = ''.join(new)
    result = new_1.replace(new_1[0:16], '****************')
    return result


def mask_card_num(msg: str) -> str:
    """
    Маскируем цифры карты
    """
    meaning = ''.join(letter for letter in msg if letter.isalpha())
    let = filter(str.isdecimal, msg)
    let_new = ''.join(let)
    result_1 = let_new.replace(let_new[0:5], '******')
    result_2 = meaning + ' ' + result_1.replace(result_1[-3:], '****')
    return result_2


def final_mask(num: str) -> str:
    """
    Делаем выбор, что нам маскировать карту или счет
    """
    if 'Счет' in num:
        return f'Счет {mask_account_num(num)}'
    return mask_card_num(num)
