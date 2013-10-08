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


patterns = (
        ('[sxz]$',              '$',    'es'),
        ('[^aeioudgkprt]h$',    '$',    'es'),
        ('(qe|[^aeiou])y$',     'y$',   'ies'),
        ('$',                   '$',    's')
        )

# generate match and apply functions with above regex patterns.
rules = [build_match_and_apply_functions(pattern, search, replace)
        for (pattern, search, replace) in patterns]


def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)


