import json
from datetime import datetime
from re import sub


def load_operations(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def filter_executed(dictionary):
    filter_list = []
    for info in dictionary:
        if info.get("state") == "EXECUTED":
            filter_list.append(info)
    return filter_list


def card_number(card):
    """Номер карты замаскирован и не отображается целиком в формате  XXXX XX** **** XXXX"""
    if card == None:
        pass
    else:
        card_of_numb = []
        card_of_name = []
        card_split = card.split(' ')
        for i in card_split:
            if i.isdigit():
                card_of_numb.append(i)
            else:
                card_of_name.append(i)

        card_join = ''.join(card_of_numb)
        card_join_name = ' '.join(card_of_name)

        if len(card_join) == 16:
            masked_card = sub(r'(\d{4})(\d{2})\d{6}(\d{4})', r'\1 \2** **** \3', card_join)
            masked_card_with_name = f"{card_join_name} {masked_card}"
        else:
            return "Введите номер карты"

        return masked_card_with_name


def account_numb(account):
    """Номер счета замаскирован и не отображается целиком в формате  **XXXX"""
    account_of_numb = []
    account_of_name = []
    account_split = account.split(' ')
    for i in account_split:
        if i.isdigit():
            account_of_numb.append(i)
        else:
            account_of_name.append(i)

    account_join = ''.join(account_of_numb)
    account_join_name = ' '.join(account_of_name)

    if len(account_join) == 20:
        masked_account = sub(r'(\d{2})(\d{14})(\d{4})', r'**\3', account_join)
        masked_account_with_name = f"{account_join_name} {masked_account}"
    else:
        return "Введите номер счета"

    return masked_account_with_name


def date_time(number):
    """Дата перевода представлена в формате 2019-12-08T22:46:21.935582"""
    date_format = datetime.fromisoformat(number)
    return date_format
