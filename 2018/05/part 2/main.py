"""
Written by: Jonas Vander Vennet
on: 2019/12/04
Answer: 4652
"""


def scan_polymer(polymer):
    alphabet = set(polymer.lower())
    while True:
        changed = False
        for letter in alphabet:
            if f'{letter}{letter.upper()}' in polymer:
                changed = True
                polymer = polymer.replace(f'{letter}{letter.upper()}', '')
            if f'{letter.upper()}{letter}' in polymer:
                changed = True
                polymer = polymer.replace(f'{letter.upper()}{letter}', '')
        if not changed:
            return polymer


def main():
    test_values = [
        ('dabAcCaCBAcCcaDA', 10),
    ]

    for polymer, answer in test_values:
        result = scan_polymer(polymer)
        assert(len(result) == answer)

    with open('../input.txt') as ifp:
        polymer = ifp.readline().replace('\n', '')
    alphabet = set(polymer.lower())
    best_length = None
    for letter in alphabet:
        new_polymer = polymer.replace(letter, '')
        new_polymer = new_polymer.replace(letter.upper(), '')
        result = scan_polymer(new_polymer)
        if best_length is None or len(result) < best_length:
            best_length = len(result)
    print(best_length)


if __name__ == '__main__':
    main()
