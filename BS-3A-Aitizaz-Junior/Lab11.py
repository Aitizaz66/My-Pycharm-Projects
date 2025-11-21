letters = "abcdefghijklmnopqrstuvwxyzABCEDFGHIJKLMNOPQRSTUVWXYZ"


def is_variable(pattern):
    return (type(pattern) is str
            and pattern[0] == '?'
            and len(pattern) > 1
            and pattern[1] != '*'
            and pattern[1] in letters
            and ' ' not in pattern)


######################################################################
def contains_tokens(pattern):
    return type(pattern) is list and len(pattern) > 0


######################################################################
def match_variable(var, replacement, bindings):
    binding = bindings.get(var)
    if not binding:
        bindings.update({var: replacement})
        return bindings
    if replacement == bindings[var]:
        return bindings
    return False


#######################################################################
def match_pattern(pattern, input, bindings=None):
    # print("P=",pattern,"I=",input,"B=",bindings)
    if bindings is False:
        return False
    if pattern == input:
        return bindings
    bindings = bindings or {}
    if is_segment(pattern):
        token = pattern[0]
        var = token[2:]
        return match_segment(var, pattern[1:], input, bindings)
    elif is_variable(pattern):
        var = pattern[1:]
        return match_variable(var, [input], bindings)
    elif contains_tokens(pattern) and contains_tokens(input):
        return match_pattern(pattern[1:], input[1:], match_pattern(pattern[0], input[0], bindings))
    else:
        return False


#######################################################################
def is_segment(pattern):
    return (type(pattern) is list
            and pattern
            and pattern and len(pattern[0]) > 2
            and pattern[0][0] == '?'
            and pattern[0][1] == '*'
            and pattern[0][2] in letters
            and ' ' not in pattern[0])


#####################################################################
def match_segment(var, pattern, input, bindings):
    if not pattern:
        return match_variable(var, input, bindings)
    word = pattern[0]
    try:
        pos = input.index(word)
    except ValueError:
        return False
    var_match = match_variable(var, input[:pos], dict(bindings))
    match = match_pattern(pattern, input[pos:], var_match)
    return match


bindings = {}
print(match_pattern(['?*a', 'Eliza', '?*b'], ['hello', 'Eliza', 'How', 'are ', 'you']))
print(match_pattern(['?*c', 'And', '?*d'], ['How', 'are', 'you', 'And', 'what', 'do', 'you', 'do']))
