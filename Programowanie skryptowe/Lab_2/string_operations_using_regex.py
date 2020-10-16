import re


def logic(string):
    final_string = ''
    while string:
        text = re.match(r'[a-zA-ZĄąĆćĘęŁłŃńÓóŚśŹźŻż]+', string)
        number = re.match(r'[0-9]+', string)
        if text:
            final_string += f'\tWyraz: {text.group()}\n'
            string = string[text.span()[1]:]
        if number:
            final_string += f'\tLiczba: {number.group()}\n'
            string = string[number.span()[1]:]
    return final_string


if __name__ == '__main__':
    while True:
        try:
            string = input()
        except EOFError:
            break
        print(logic(string))
