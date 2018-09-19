from datetime import datetime, timedelta, date
import locale
locale.setlocale(locale.LC_TIME, 'ru_RU.utf-8')

dt_now = datetime.now() 


# функция изменения даты по месяцам:
def delta_month(input_date, monthes = 1):
    month_list = range(1, 13)
    my_month = month_list[(input_date.month - 1 + monthes)%12] #ok
    my_day = input_date.day
    my_year = input_date.year + (input_date.month + monthes)//12
    return date(my_year, my_month, my_day)


# перемотка дней, недель
def delta_day(date, days = 1, weeks = 0, operand = 'plus'):
    delta_day = timedelta(days, 0, 0, 0, 0, 0 , weeks)
    if operand == 'plus':
        return date + delta_day
    else:
        return date - delta_day


# функция перевода строки в объект datetime
def string_to_datetime(string_date):
    return datetime.strptime(string_date, '%d/%m/%y %H:%M:%S.%f')

# formate your date to human-frendly format
def beauty_date(non_beauty_date):
    return non_beauty_date.strftime('%d %B %Y года, %A')

if __name__ == '__main__':
    #сегодня
    print('today', beauty_date(dt_now))
    #вчера
    print('yestarday', delta_day(dt_now, 1, 0, 'minus'))
    #month ago
    print('month ago', delta_month(dt_now, -1))
    #str to datetime
    print('your date: ', string_to_datetime("01/01/17 12:10:03.234567"))
