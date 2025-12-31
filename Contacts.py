#!/usr/bin/python3
import calendar
import datetime as d
from calendar import month_name, TextCalendar
from calendar import weekday
from os import path


def user_login() -> bool:
    def init_user() -> bool:
        if path.exists('./user_info'):
            return True

        else:
            print('No account found!')
            return False

    def user_setup(ask_answer) -> None:
        with open("./user_info", "w+t") as user_info:
            user_info.write(",".join(ask_answer))
            user_info.flush()
            return

    def login_success(put_answer) -> bool:
        with open("./user_info", "r+t") as user_info:
            user = str(user_info.read()).split(",")
            if put_answer[:1] and put_answer[1:2] in user:
                return True

            else:
                print("try again!")
                return False

    class info:
        def __init__(self) -> None:
            pass

        def ask(self) -> list[str]:
            return [
                input('Please Enter new Username: '),
                input('Enter new Password: ')
            ]

        def put(self) -> list[str]:
            return [
                input('Enter Username: '),
                input('Enter Password: ')
            ]

    login = False
    while login is False:
        if init_user() is True:
            login = login_success(
                put_answer=info().put()
            )

        if init_user() is False:
            user_setup(
                ask_answer=info().ask()
            )
        continue
    return True


class date_format:
    def __init__(self) -> None:
        self.current_date = list(map(int, str(
            d.datetime.now().date()).split('-')))

    def form_weekday(self) -> int:
        return weekday(
            *self.current_date[:]
        )


class form_calendar_current(date_format):
    def __init__(self) -> None:
        super().__init__()

    def year_schedule(self) -> str:
        return TextCalendar().formatyear(
            *self.current_date[:1]
        )

    def month_schedule(self) -> str:
        return TextCalendar().formatmonth(
            *self.current_date[:2]
        )

    def day_schedule(self) -> str:
        return TextCalendar().formatday(
            *self.current_date[2:3],
            weekday=self.form_weekday(),
            width=0
        )


class user_handling():
    def __init__(self) -> None:
        pass

    def month(self) -> int:
        return int(input('Enter a month #'))

    def year(self) -> int:
        return int(input('Enter year: '))

    def day(self) -> int:
        return int(input('Enter day #'))


def write_schedule(*args):
