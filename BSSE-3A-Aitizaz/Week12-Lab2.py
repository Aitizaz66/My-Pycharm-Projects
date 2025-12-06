operators = "+-*/%"
numbers = "0123456789"
letters = "abcdefghijklmnopqrstuvwxyzABCEDFGHIJKLMNOPQRSTUVWXYZ"
student_rules = [
    ('find ?*a', ['To-find', '=', '?a']),
    ('?*a is equal to ?*b', ['?a', '=', '?b']),
    ('?*a makes ?*b', ['?a', '=', '?b']),
    ('?*a are calculated by ?*b', ['?a', '=', '?b']),
    ('?*a calculated by ?*b', ['?a', '=', '?b']),
    ('?*a can be calculated as ?*b', ['?a', '=', '?b']),
    ('?*a calculated as ?*b', ['?a', '=', '?b']),
    ('?*a can be ?*b', ['?a', '=', '?b']),
    ('?*a equal to ?*b', ['?a', '=', '?b']),
    ('?*a equals ?*b', ['?a', '=', '?b']),
    ('?*a is ?*b', ['?a', '=', '?b']),
    ('?*a are ?*b', ['?a', '=', '?b']),
    ('?*a in ?*b', ['?a', '=', '?b']),
    ('?*a plus ?*b', ['?a', '+', '?b']),
    ('?*a minus ?*b', ['?a', '-', '?b']),
    ('?*a divided by ?*b', ['?a', '/', '?b']),
    ('twice ?*a', ['2', '*', '?a']),
    ('sum ?*a and ?*b', ['?a', '+', '?b']),
    ('adding ?*a and ?*b', ['?a', '+', '?b']),
    ('distributed into ?*a and ?*b', ['?a', '+', '?b']),
    ('divided into ?*a and ?*b', ['?a', '+', '?b']),
    ('one half ?*a', ['?a', '/', '2']),
    ('half ?*a', ['?a', '/', '2']),
    ('square ?*a', ['?a', '*', '?a']),
    ('?*a times ?*b', ['?a', '*', '?b']),
    ('?*a multiplied by ?*b', ['?a', '*', '?b']),
    ('?*a multiplied with ?*b', ['?a', '*', '?b']),
    ('difference between ?*a and ?*b', ['?b', '-', '?a']),
    ('?*a % less than ?*b', ['?b', '/', ['1', '-', ['?a', '/', '100']]])
]


def is_variable(pattern):
    return (type(pattern) is str
            and pattern[0] == '?'
            and len(pattern) > 1
            and pattern[1] != '*'
            and pattern[1] in letters
            and ' ' not in pattern)


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


def is_segment(pattern):
    return (type(pattern) is list
            and pattern
            and pattern and len(pattern[0]) > 2
            and pattern[0][0] == '?'
            and pattern[0][1] == '*'
            and pattern[0][2] in letters
            and ' ' not in pattern[0])


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


def contains_tokens(pattern):
    return type(pattern) is list and len(pattern) > 0


def match_variable(var, replacement, bindings):
    binding = bindings.get(var)
    if not binding:
        bindings.update({var: replacement})
        return bindings
    if replacement == bindings[var]:
        return bindings
    return False


def toeqstr(elst):
    ans = ''
    if type(elst) is str:
        return elst
    for item in elst:
        if type(item) is list:
            ans = ans + " ( " + toeqstr(item) + " )"
        else:
            if ans == '':
                ans = item
            else:
                ans = ans + ' ' + str(item)
    return ans


def replace_item(n, o, lst):
    if lst == []:
        return []
    elif o == lst:
        return n
    elif type(lst) is not list:
        return lst
    else:
        ans = replace_item(n, o, lst[1:])
        ans.insert(0, replace_item(n, o, lst[0]))
        return ans


def tranlate_to_exp(eqwlst):
    print("Input : ", toeqstr(eqwlst), '""')
    for pattern, response in student_rules:
        pattern = pattern.split()
        bindings = match_pattern(pattern, eqwlst)
        if bindings:
            print('Rule: "', toeqstr(pattern), '"[', toeqstr(response), ']')
            print('Bindings : ', bindings)
            for var, val in bindings.items():
                tval = tranlate_to_exp(val)
                response = replace_item(tval, '?' + var, response)
            print('Output : ', response)
            return response
    if eqwlst == []:
        return eqwlst
    return eqwlst[0]


def remove_noise(txt):
    nwords = ['a', 'the', 'number', 'of', 'this', 'if', 'that', '$', 'his', 'while']
    for w in nwords:
        if txt.count(w) > 0:
            txt = [a for a in txt if a != w]
    return txt


def student():
    userinput = input("Enter Statement: ")
    userinput = userinput.lower()
    engEqs = userinput.split('.')
    eqs = []
    for engeq in engEqs:
        engeq = engeq.split()
        eqwlst = remove_noise(engeq)
        eq1 = tranlate_to_exp(eqwlst)
        eqs.append(eq1)
    eqs = [eq for eq in eqs if eq != []]
