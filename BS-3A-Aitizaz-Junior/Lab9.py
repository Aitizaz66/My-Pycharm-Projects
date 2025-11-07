# Not Doing Anything. Mam taking Feedback of lab
# write a recursive function that sum the values of a dictionary nd return sum

def sum_nested(dic):
    total = 0
    for item in dic.values():
        if type(item) == dict:
            total += sum_nested(item)
        else:
            total += item
    return total


dic_sum = {'a': 10, 'b': {'c': 35, 'd': 48}, 'e': 39}
print("Total sum Of Nested Dict:", sum_nested(dic_sum))
