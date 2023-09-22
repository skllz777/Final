from datetime import datetime, date


class DateCheck:

    @staticmethod
    def is_date(date_value: str):
        date_list = date_value.split(".")
        if len(date_value) < 10 or len(date_list) != 3:
            raise ValueError("Дата не соответствует формату dd.mm.yyyy")
        for i in date_list:
            try:
                el = int(i)
            except ValueError:
                raise ValueError("Элемент в дате рождения не является целым числом")
        if 31 < int(date_list[0]):
            raise ValueError("Число дня больше 31")
        elif int(date_list[0]) < 1:
            raise ValueError("Число дня меньше 1")
        if 12 < int(date_list[1]):
            raise ValueError("Число месяца больше 12")
        elif int(date_list[1]) < 1:
            raise ValueError("Число месяца меньше 1")
        if datetime.strptime(date_value, '%d.%m.%Y').date() > date.today():
            raise ValueError("Дата рождения больше даты сегодняшнего дня")