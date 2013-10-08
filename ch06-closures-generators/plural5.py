import re


def build_match_and_apply_functions(pattern, search, replace):
    """
    Build match and apply functions based on given re pattern, search text, and replacement.
    """

    def matches_rule(word):
        """ Check if word contains pattern.
        """
        return re.search(pattern, word)

    def apply_rule(word):
        """ Replace text with replacement in word.
        """
        return re.sub(search, replace, word)

    return (matches_rule, apply_rule)


def rules(rules_filename):
    with open(rules_filename, encoding='utf-8') as pattern_file:
        for line in pattern_file:
            pattern, search, replace = line.split(None, 3)
            yield build_match_and_apply_functions(pattern, search, replace)


def plural(noun, rules_filename='plural5-rules.txt'):
    for matches_rule, apply_rule in rules(rules_filename):
        if matches_rule(noun):
            return apply_rule(noun)

    raise ValueError('no matches rule for {0}'.format(noun))
