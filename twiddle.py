import random


def twiddle_word(word):
    if len(word) <= 1:
        raise ValueError('word argument is too short to twiddle: {}'.format(word))
    if all(x == word[0] for x in word):
        raise ValueError('word argument has all the same letters: {}'.format(word))
    if not all(x.isalpha() for x in word):
        raise ValueError('word must contain only alphabetic characters: {}'.format(word))
    result = ''.join(random.sample(word, len(word)))
    while result == word:
        result = ''.join(random.sample(word, len(word)))
    return result


def twiddle_n_words(n, words):
    seen = set()
    original_n = n
    while n:
        try:
            i = random.randint(0, len(words) - 1)
            if i not in seen:
                seen.add(i)
                words[i] = twiddle_word(words[i])
                n -= 1
        except ValueError as e:
            pass
        if len(seen) + n > len(words):
            raise ValueError('n is greater than the number of valid words to twiddle: n={}'.format(original_n))


def twiddle_n_words_in_lines(n, lines):
    seen = set()
    original_n = n
    n_words = sum(len(l) for l in lines)
    while n:
        try:
            l = random.randint(0, len(lines) - 1)
            w = random.randint(0, len(lines[l]) - 1)
            if (l, w) not in seen:
                seen.add((l, w))
                lines[l][w] = twiddle_word(lines[l][w])
                n -= 1
        except ValueError as e:
            pass
        if len(seen) + n > n_words:
            raise ValueError('n is greater than the number of valid words to twiddle: n={}'.format(original_n))