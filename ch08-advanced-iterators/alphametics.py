import re
import itertools


def solve(puzzle):
    # match one or more sets of upper-case letters in puzzle string.
    words = re.findall('[A-Z]+', puzzle.upper())
    # pull out all unique chars from words
    unique_chars = set(''.join(words))
    # Can't have more unique letters than digits.
    # Note that assert can get optimized away since it's if __debug__.
    assert len(unique_chars) <= 10, 'Too many letters'
    # grab set of letters
    first_letters = {word[0] for word in words}
    n = len(first_letters)
    # get string of unique chars with first letters of words coming first.
    sorted_chars = ''.join(first_letters) + ''.join(unique_chars - first_letters)
    # get ASCII representations of characters
    characters = tuple(ord(c) for c in sorted_chars)
    # get ASCII representations of digit characters
    digits = tuple(ord(c) for c in '0123456789')
    zero = digits[0]
    # get permutations of digit representations, one for each char.
    # switch chars for digits and check if equation holds. If it does, return it.
    print(digits)
    print(characters)
    for guess in itertools.permutations(digits, len(characters)):
        if zero not in guess[:n]:
            equation = puzzle.translate(dict(zip(characters, guess)))
            if eval(equation):
                return equation

if __name__ == "__main__":
    import sys
    for puzzle in sys.argv[1:]:
        print(puzzle)
        solution = solve(puzzle)
        if solution:
            print(solution)
