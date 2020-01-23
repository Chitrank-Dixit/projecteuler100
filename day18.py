import math


def day_of_week(year, month, day):
    # day 1 is sunday
    d = day
    m = (month - 3) % 12 + 1
    yr = year
    if m > 10:
        yr = year - 1
    y = yr % 100
    c = (yr - (yr % 100)) / 100
    w = (d + math.floor(2.6 * m - 0.2) + y + math.floor(y / 4) + math.floor(c / 4) - 2 * c) % 7
    return int(w)


def no_of_sundays(day, start_year, end_year):
    total = 0
    for year in range(start_year, end_year):
        for month in range(1, 13):
            if day_of_week(year, month, 1) == day:
                total += 1
    return total


print(no_of_sundays(0, 1901, 2001))
