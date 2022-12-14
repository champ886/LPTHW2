import time
from calendar import isleap


def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False


def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28


leap_year = judge_leap_year(2020)
#for m in range(1, localtime.tm_mon):
#    day = day + month_days(m, leap_year)

print(month_days(2,leap_year))