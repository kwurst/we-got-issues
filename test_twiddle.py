import pytest
import random
from collections import Counter
from twiddle import twiddle_word
from twiddle import twiddle_n_words
from twiddle import twiddle_n_words_in_lines


def test_twiddle_word():
    random.seed(0)
    word = 'ab'
    word_twiddled = twiddle_word(word)
    assert word != word_twiddled
    assert Counter(word) == Counter(word_twiddled)


def test_twiddle_word_must_change():
    random.seed(1)
    word = 'ab'
    word_twiddled = twiddle_word(word)
    assert word != word_twiddled
    assert Counter(word) == Counter(word_twiddled)


def test_twiddle_word_too_short_raises_value_error():
    random.seed(0)
    word = 'a'
    with pytest.raises(ValueError):
        twiddle_word(word)


def test_twiddle_word_none_raises_type_error():
    random.seed(0)
    word = None
    with pytest.raises(TypeError):
        twiddle_word(word)


def test_twiddle_word_all_same_character_raises_value_error():
    random.seed(0)
    word = 'aaa'
    with pytest.raises(ValueError):
        twiddle_word(word)


def test_twiddle_word_non_alphabetic_raises_value_error():
    random.seed(0)
    word = 'aa.'
    with pytest.raises(ValueError):
        twiddle_word(word)


def test_twiddle_n_words():
    random.seed(0)
    text = 'The blessing of your happinesses will become harmoniously when you respect that intuition is the ego.'
    words = text.split()
    n = 5
    twiddle_n_words(n, words)
    result = ' '.join(words)
    assert result != text
    assert Counter(result) == Counter(text)
    words = text.split()
    twiddles = result.split()
    assert len(words) == len(twiddles)
    print(list(u != v for u, v in zip(words, twiddles)))
    assert len(words) == len(list(u != v for u, v in zip(words, twiddles)))
    assert n == sum(u != v for u, v in zip(words, twiddles))


def test_twiddle_n_words_n_too_large_raises_value_error():
    random.seed(0)
    text = 'The blessing of your happinesses will become harmoniously when you respect that intuition is the ego.'
    words = text.split()
    n = len(words)
    with pytest.raises(ValueError):
        twiddle_n_words(n, words)


def test_twiddle_n_words_in_lines():
    random.seed(0)
    lines = '''Who can absorb the living and affirmation of a therapist if he has the shining art of the thing?
    With zucchinis drink coconut milk. Hobble impatiently like a jolly wind. The emitter warps alarm
    like a greatly exaggerated collective. Resistance at the holodeck that is when ugly queens fly.
    Who can capture the art and courage of a creator if he has the inner joy of the visitor?
    The afterlife is a special ego. If you disturb or rise with a simple anger, fear needs you.
    '''.split('\n')
    lines = [l.split() for l in lines]
    n = 5
    twiddle_n_words_in_lines(n, lines)
    assert False