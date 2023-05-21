from datetime import datetime

from scr.utils import card_number, account_numb, filter_executed, date_time


def test_card_number():
    assert card_number("Maestro 1913883747791351") == "Maestro 1913 88** **** 1351 -> "
    assert card_number("1913883747791351") == " 1913 88** **** 1351 -> "
    assert card_number("19138837477") == "Введите номер счета или карты"
    assert card_number("11492155674319392427") == " **2427 -> "
    assert card_number(None) == ""


def test_account_numb():
    assert account_numb("Счет 72645194281643232984") == "Счет **2984"
    assert account_numb("72645194281643232984") == " **2984"
    assert account_numb("7264519428164") == "Введите номер счета"


def test_filter_executed():
    assert filter_executed([{"state": "EXECUTED"}, {"state": "CANCELED"}, {"state": "EXECUTED"}]) == [
        {'state': 'EXECUTED'}, {'state': 'EXECUTED'}]
    assert filter_executed([{"date": "EXECUTED"}, {"state": "CANCELED"}, {"id": "EXECUTED"}]) == []


def test_date_time():
    assert date_time("2018-06-08T16:14:59.936274") == datetime.fromisoformat("2018-06-08T16:14:59.936274")
    assert date_time("2018-06-08T16:14:59.936274") != "2018-06-08T16:14:59.936274"
