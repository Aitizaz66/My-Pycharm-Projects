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


#################################################################

rules = [
    ("?*X HELLO ?*Y", ["How do you do. Please state your problem."]),
    ("?*X COMPUTER ?*Y", ["Do computers worry you?",
                          "What do you think about machines?",
                          "Why do you mention computers?",
                          "What do you think machines have to do with your problem?", ]),
    ("?*X NAME IS ?*Y", ["I am not interested in names",
                         "what do you do ?Y"]),
    ("?*X NEED ?*Y", ["What if ?X get ?Y", "why ?X need ?Y"]),
    # ("?*X I NEEED ?*Y COMPUTER ?*Z", ["Matching multiple values"])
    
]

default_responses = ["Very interesting",
                     "I am not sure I understand you fully",
                     "Please continue"]
###########################################################################
import random


def replace(word, replacements):
    for old, new in replacements:
        if word == old:
            return new
    return word


###########################################################################
def switch_viewpoint(words):
    replacements = [('I', 'YOU'), ('YOU', 'I'), ('ME', 'YOU'),
                    ('MY', 'YOUR'), ('AM', 'ARE'), ('ARE', 'AM')]
    return [replace(word, replacements) for word in words]


###########################################################################
def respond(rules, input, default_responses):
    input = input.split()
    matching_rules = []
    for pattern, responses in rules:
        pattern = pattern.split()
        bindings = match_pattern(pattern, input)
        if bindings:
            matching_rules.append((responses, bindings))
    if matching_rules:
        responses, bindings = random.choice(matching_rules)
        response = random.choice(responses)
    else:
        bindings = {}
        response = default_responses[0]
    for variable, value in bindings.items():
        value = ' '.join(switch_viewpoint(value))
        if value:
            response = response.replace('?' + variable, value)
    return response


###########################################################################
def Eliza(prompt, rules, default_responses):
    while True:
        try:
            userinput = input(prompt).upper()
            if not userinput:
                continue
        except:
            break
        print(respond(rules, userinput, default_responses))


Eliza('Eliza> ', rules, default_responses)
# output
# (match_segment('?*a', ['hello', '?*b'], ['test', 'hello', 'eliza'], bindings))
# #output
# print(match_segment('?*a', ['hello', '?b'], ['test', 'hello', 'eliza'], bindings))
# #output
#
# print(match_pattern(['a', '?d', '?e'], ['a', 'b', 'c']))
#
# print(match_segment('?*a', ['hello', '?b'], ['test', 'hello', 'eliza'], bindings))
# #output
#
# print(match_segment('?*a', ['hello', '?*b'], ['test', 'hello', 'eliza'], bindings))
# #output
#
# print(match_segment('?*a', ['hello', '?*b'], ['test', 'hello', 'eliza', 'how', 'are', 'you'], bindings))
# #output
