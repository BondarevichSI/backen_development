# Последние 5 выполненных (EXECUTED) операций выведены на экран.
# Операции разделены пустой строкой.
# Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018).
# Сверху списка находятся самые последние операции (по дате).


import json
from datetime import datetime
from re import sub

filenam = 'operations.json'


def load_operations(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def card_number(card):
    """Номер карты замаскирован и не отображается целиком в формате  XXXX XX** **** XXXX"""
    card_of_numb = []
    card_split = card.split(' ')
    for i in card_split:
        if i.isdigit():
            card_of_numb.append(i)

    card_join = ''.join(card_of_numb)
    if len(card_join) == 16:
        masked_card = sub(r'(\d{4})(\d{2})\d{6}(\d{4})', r'\1 \2** **** \3', card_join)
    else:
        return "Введите номер карты"

    return masked_card


d = card_number("Visa Platinum 8990922113665229")
print(d)


def account_numb(account):
    """Номер счета замаскирован и не отображается целиком в формате  **XXXX"""
    account_of_numb = []
    account_split = account.split(' ')
    for i in account_split:
        if i.isdigit():
            account_of_numb.append(i)

    account_join = ''.join(account_of_numb)
    if len(account_join) == 20:
        masked_account = sub(r'(\d{2})(\d{14})(\d{4})', r'**\3', account_join)
    else:
        return "Введите номер счета"

    return masked_account


s = account_numb("Счет 72082042523231456215")
print(s)

def date_time(number):
    """Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018)"""
    date_format = datetime.fromisoformat(number)
    return f"{date_format.day}.{date_format.month}.{date_format.year}"

q = date_time("2019-12-08T22:46:21.935582")
print(q)