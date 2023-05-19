from scr.utils import load_operations, date_time, filter_executed, card_number, account_numb

filenam = 'operations.json'
data_operation = load_operations(filenam)

data_filter_executed = filter_executed(data_operation)


def sort_date(x):
    date = date_time(x["date"])
    return date


data_sorted_time = sorted(data_filter_executed, key=sort_date, reverse=True)

for data in range(5):
    data_sort_five = data_sorted_time[data]
    date_time_mode = date_time(data_sort_five["date"])
    print()
    print(f"{date_time_mode.day}.{date_time_mode.month}.{date_time_mode.year} {data_sort_five['description']}\n"
          f"{card_number(data_sort_five.get('from'))} -> {account_numb(data_sort_five['to'])}\n"
          f"{data_sort_five['operationAmount']['amount']} {data_sort_five['operationAmount']['currency']['name']}")
