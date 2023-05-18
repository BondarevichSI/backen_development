from scr.utils import load_operations, date_time, filter_executed

filenam = 'operations.json'
data_operation = load_operations(filenam)

data_filter_executed = filter_executed(data_operation)


def sort_date(x):
    date = date_time(x["date"])
    return date


data_sorted = sorted(data_filter_executed, key=sort_date, reverse=True)

for data in range(5):
    data_operation_sort = data_sorted[data]

    #print(data_operation_sort)

m = date_time(data_operation_sort["date"])
print(f"{m.day}.{m.month}.{m.year} {data_operation_sort['description']}\n"
      f"{data_operation_sort['to']}")

