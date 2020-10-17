from Lab_3.day import Day


class Term:
    def __init__(self, day, hour, minute):
        self.hour = hour
        self.minute = minute
        self.duration = 90
        self._day = day
        self.day_to_str = {
            Day.MON: 'Poniedziałęk',
            Day.TUE: 'Wtorek',
            Day.WED: 'Środa',
            Day.THU: 'Czwartek',
            Day.FRI: 'Piątek',
            Day.SAT: 'Sobota',
            Day.SUN: 'Niedziela'
        }

    def __str__(self):
        return f"{self.day_to_str[self._day]} {self.hour}:{self.minute} [{self.duration}]"

    def earlierThan(self, termin):
        if self._day.value < termin._day.value:
            return True
        elif self._day.value > termin._day.value:
            return False

        if termin.hour > self.hour:
            return True
        elif termin.hour < self.hour:
            return False
        elif termin.minute > self.minute:
            return True
        else:
            return False

    def laterThan(self, termin):
        if self._day.value > termin._day.value:
            return True
        elif self._day.value < termin._day.value:
            return False

        if termin.hour < self.hour:
            return True
        elif termin.hour > self.hour:
            return False
        elif termin.minute < self.minute:
            return True
        else:
            return False

    def equals(self, termin):
        if self._day.value != termin._day.value:
            return False

        return True if termin.hour == self.hour and termin.minute == self.minute else False


term1 = Term(Day.TUE, 9, 45)
print(term1)
term2 = Term(Day.WED, 10, 15)
print(term2)
print(term1.earlierThan(term2))
print(term1.laterThan(term2))
print(term1.equals(term2))
