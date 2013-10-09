
class LazyRules:
    # our stored regex rules
    rules_filename = 'plural6-rules.txt'

    def __init__(self):
        self.pattern_file = open(self.rules_filename, encoding='utf-8')
        # store match and apply functions in cache once they're created.
        self.cache = []

    def __iter__(self):
        # on iteration, move through cache of functions using this index.
        self.cache_index = 0
        return self

    def __next__(self):
        self.cache_index += 1
        # we have funcs left so return next set.
        if len(self.cache) >= self.cache_index:
            return self.cache[self.cache_index - 1]

        # exhausted our regex list so we're done.
        if self.pattern_file.closed:
            raise StopIteration

        line = self.pattern_file.readline()
        # end of file so we're done.
        if not line:
            self.pattern_file.close()
            raise StopIteration

        # get regex and turn into match and apply funcs.
        pattern, search, replace = line.split(None, 3)
        funcs = build_match_and_apply_functions(pattern, search, replace)
        # store funcs in our cache.
        self.cache.append(funcs)
        return funcs

rules = LazyRules()


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
