# letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#
#
# def is_variable(pattern):
#     return (type(pattern) is str
#             and len(pattern) > 1
#             and pattern[0] == "?"
#             and pattern[1] != '*'
#             and pattern[1] in letters
#             and ' ' not in pattern
#             )
#
#
# print("Condition ", 1, is_variable("a*1"))
# print("Condition ", 2, is_variable("?"))
# print("Condition ", 3, is_variable("?a*"))
# print("Condition ", 4, is_variable("?*a"))
# print("Condition ", 5, is_variable(""))
# print("Condition ", 6, is_variable("8"))
# print("Condition ", 7, is_variable("L?*"))
# print("Condition ", 8, is_variable("?8K"))
# print("Condition ", 9, is_variable("*kh abc*"))
# print("Condition ", 10, is_variable(" ?b*"))
# print("Condition ", 11, is_variable("? BC*"))
# print("Condition ", 12, is_variable("?JKL"))
# print("Condition ", 13, is_variable("IO?*"))
# print("Condition ", 14, is_variable("?1d"))
# print("Condition ", 15, is_variable("P ?"))
# print("Condition ", 16, is_variable("09324"))
# print("Condition ", 17, is_variable(123))
# print("Condition ", 18, is_variable("?L"))
# print("Condition ", 19, is_variable("(?kj)"))
# print("Condition ", 20, is_variable("A"))

# update When variable not exist before
def match_variable(var, replacement, bindings={}):
    binding = bindings.get(var)
    if not binding:
        bindings.update({var: replacement})
        return bindings
    elif replacement == binding:
        return bindings
    return False


h = match_variable("a", "hello")
h = match_variable("b", "ali", h)
h = match_variable("b", "ali", h)
print(h)
