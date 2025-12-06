letters = "abcdefghijklmnopqrstuvwxyzABCEDFGHIJKLMNOPQRSTUVWXYZ"


def reverse_op(op):
    if op == '+':
        return '-'
    elif op == '-':
        return '+'
    elif op == '*':
        return '/'
    elif op == '/':
        return '*'


def one_unknown2(equation):
    c = 0
    var = None
    for item in equation:
        if type(item) is list:
            ans = one_unknown2(item)
            c += ans[1]
            if ans[1] != 0:
                var = ans[0]
        else:
            flag = False
            for ch in item:
                if ch in letters:
                    flag = True
            if flag == True:
                c += 1
                var = item
    return var, c


def find_one_unknown(eqs):
    for eq in eqs:
        ans = one_unknown2(eq)
        count = ans[1]
        var = ans[0]
        if count == 1:
            return var, eq
    return None, []


print(reverse_op('+'))
print(reverse_op('-'))
print(reverse_op('/'))
print(reverse_op('*'))
print(reverse_op('**'))
print(reverse_op('*+'))
print(reverse_op('/*'))
print(reverse_op('+-'))
print(reverse_op('?'))
print(reverse_op('++'))
print(one_unknown2(['x', '+', '10', 'a', '=', '9']))
print(one_unknown2(['y', '/', '10', 'b', '=', '4']))
print(one_unknown2(['z', '*', '10', 'f', '=', '12']))
print(one_unknown2(['w', '-', '100']))
print(one_unknown2(['k', '+', '145']))
print(one_unknown2(['x', '-', '32']))
print(one_unknown2(['p', '*', 'p']))
print(one_unknown2(['x', '+', '96', 'a', '-', '9', 'o', '++', '7']))
print(one_unknown2(['o', '/', '78']))
print(one_unknown2(['x', '+', '1']))
print(find_one_unknown(['w', '-', '100', ['k', '+', '145'], 'q', '/', '2', ['d', '+', 'd']]))
print(find_one_unknown(['k', '+', '145', ['w', '-', 'i'], 'r', '*', 'r']))
print(find_one_unknown(['q', '-', '100', ['k', '+', '1'], 'y', '+', '2']))
print(find_one_unknown(['e', '-', '100', ['p', '+', '45'], 'b', '-', '2']))
print(find_one_unknown(['r', '*', 'b', ['a', '+', 'b'], 'n', '+', '2', ['g', '/', '78']]))
print(find_one_unknown(['t', '/', '100', ['y', '/', '15'], 'm', '//', '2']))
print(find_one_unknown(['g', '+', '100', ['o', '++', '5'], 'j', '**', 'y']))
print(find_one_unknown(['h', '**', '100', ['p', '*', '14'], 'l', '-', '2']))
print(find_one_unknown(['j', '-', '100', ['t', '-', 'p'], 'i', '*', '2', ['v', '-', '40']]))
print(find_one_unknown(['z', '*', 'z', ['k', '//', 'u'], 'u', '/', '2']))
