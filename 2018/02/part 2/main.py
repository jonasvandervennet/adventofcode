"""
Written by: Jonas Vander Vennet
on: 2019/12/02
Answer: xpysnnkqrbuhefmcajodplyzw
"""


def neighbouring_words(wordlist):
    for word1 in wordlist:
        for word2 in wordlist:
            if len(word1) == len(word2):
                diff = 0
                for i in range(len(word1)):
                    if word1[i] != word2[i]:
                        diff += 1
                        if diff > 1:
                            break
                if diff == 1:
                    return word1, word2


def common_letters(word1, word2):
    common = ''
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            common += word1[i]
    return common


def main():
    test_values = [
        ([
            'abcde',
            'fghij',
            'klmno',
            'pqrst',
            'fguij',
            'axcye',
            'wvxyz',
        ], 'fgij'),
    ]
    for test_words, desired_output in test_values:
        neighbours = neighbouring_words(test_words)
        assert(desired_output == common_letters(*neighbours))

    with open('../input.txt') as ifp:
        inputs = ifp.readlines()

    neighbours = neighbouring_words(inputs)
    common = common_letters(*neighbours)

    print(f'Common letters of neighbours: {common}')


if __name__ == '__main__':
    main()
