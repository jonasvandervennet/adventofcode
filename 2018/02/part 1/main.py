"""
Written by: Jonas Vander Vennet
on: 2019/12/02
Answer: 6200
"""


def exactly_n_occurences(word, n):
    if isinstance(word, list):
        return [exactly_n_occurences(w, n) for w in word]
    occurences = {}
    for letter in word:
        if letter not in occurences.keys():
            occurences[letter] = 0
        occurences[letter] += 1
    return n in occurences.values()


def main():
    test_values = [
        ('abcdef', 0, 0),
        ('bababc', 1, 1),
        ('abbcde', 1, 0),
        ('abcccd', 0, 1),
        ('aabcdd', 1, 0),
        ('abcdee', 1, 0),
        ('ababab', 0, 1),
    ]
    for test_word, num_2, num_3 in test_values:
        assert(num_2 == int(exactly_n_occurences(test_word, 2)))
        assert(num_3 == int(exactly_n_occurences(test_word, 3)))

    with open('../input.txt') as ifp:
        inputs = ifp.readlines()

    num_2_occurences = sum(exactly_n_occurences(inputs, 2))
    num_3_occurences = sum(exactly_n_occurences(inputs, 3))

    print(f'Checksum: {num_2_occurences * num_3_occurences}')


if __name__ == '__main__':
    main()
