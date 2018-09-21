from datetime import datetime, timedelta, date
import locale
locale.setlocale(locale.LC_TIME, 'ru_RU.utf-8')

dt_now = datetime.now() 


# функция изменения даты по месяцам:
def delta_month(input_date, months=1):
    month_list = range(1, 13)
    my_month = month_list[(input_date.month - 1 + months) % 12]  # ok
    my_day = input_date.day
    my_year = input_date.year + (input_date.month + months)//12
    return date(my_year, my_month, my_day)


# перемотка дней, недель
def delta_day(date_now, days=1, weeks=0, operand='plus'):
    day_diff = timedelta(days, 0, 0, 0, 0, 0, weeks)
    if operand == 'plus':
        return date_now + day_diff
    else:
        return date_now - day_diff


# функция перевода строки в объект datetime
def string_to_datetime(string_date):
    return datetime.strptime(string_date, '%d/%m/%y %H:%M:%S.%f')

# format your date to human-friendly format


def beauty_date(non_beauty_date):
    return non_beauty_date.strftime('%d %B %Y года, %A')


if __name__ == '__main__':

    # сегодня
    print('today', beauty_date(dt_now))
    # вчера
    print('yesterday', delta_day(dt_now, 1, 0, 'minus'))
    # month ago
    print('month ago', delta_month(dt_now, -1))
    # str to datetime
    print('your date: ', string_to_datetime("01/01/17 12:10:03.234567"))
