from enum import Enum


class Day(Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7

    def difference(self, day):
        counter = day.value - self.value

        if counter > 3:
            counter -= 7
        elif counter < -3:
            counter += 7
        return counter


def nthDayFrom(n, day):
    return_day = day.value + n

    while return_day < 1:
        return_day += 7
    while return_day > 7:
        return_day -= 7

    return Day(return_day)
