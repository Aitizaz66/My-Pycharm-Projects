letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def is_variable(pattern):
    return (type(pattern) is str
            and len(pattern) > 1
            and pattern[0] == "?"
            and pattern[1] != '*'
            and pattern[1] in letters
            and ' ' not in pattern
            )


def match_variable(var, replacement, bindings={}):
    binding = bindings.get(var)
    if not binding:
        bindings.update({var: replacement})
        return bindings
    elif replacement == binding:
        return bindings
    return False


def contain_tokens(pattern):
    return (type(pattern) is list
            and len(pattern) > 0)


def match_pattern(pattern, input, bindings=None):
    if bindings is False:
        return False
    if pattern == input:
        return bindings
    bindings = bindings or {}
    if is_variable(pattern):
        var = pattern[1:]
        return match_variable(var, [input], bindings)
    elif contain_tokens(pattern) and contain_tokens(input):
        res = match_pattern(pattern[1:], input[1:],
                            match_pattern(pattern[0], input[0], bindings))
        return res
    else:
        return False


def match(pattern, input):
    return match_pattern(pattern.split(), input.split())


print(match('a ?b c', 'a b c'))
