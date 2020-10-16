import sys
import getopt
from types import lists
from types import dicts


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], '', "moduł=")
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    for o, a in opts:
        if o == '--moduł' and a == 'lista':
            string = input()
            lists.zapisz(string)
            print(lists.wypisz())
        elif o == '--moduł' and a == 'slownik':
            string = input()
            dicts.zapisz(string)
            print(dicts.wypisz())


if __name__ == '__main__':
    main()
