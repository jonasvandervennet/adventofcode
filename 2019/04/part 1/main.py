"""
Written by: Jonas Vander Vennet
on: 2019/12/04
Answer: 1079
"""


def is_valid_password(password: str):
    repetition = False
    previous = password[0]
    for letter in password[1:]:
        if letter == previous:
            repetition = True
        if int(letter) < int(previous):
            return False
        previous = letter
    return repetition


def crack_password(start, end):
    solutions = []
    for i in range(start, end + 1):
        if is_valid_password(str(i)):
            solutions.append(i)
    return solutions


def main():
    test_values = [
        ('111111', True),
        ('223450', False),
        ('123789', False)
    ]
    for pw, valid in test_values:
        assert(is_valid_password(pw) == valid)

    with open('../input.txt') as ifp:
        start, end = ifp.readline().split('-')
    start = int(start)
    end = int(end)
    passwords = crack_password(start, end)
    print(len(passwords))


if __name__ == '__main__':
    main()
