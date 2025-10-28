# write recursive function count element of flat list [1,2,3,4]
def count(a, c=0):
    if a == []:
        return c
    else:
        return count(a[1:], c + 1)


print(count([1, 2, 3, 4]))


def Factorial(x):
    if x == 1:
        return x
    else:
        return x * Factorial(x - 1)


print(Factorial(5))


# write a function that take lis of words and only return palindrom
def get_palindrom(a):
    plist = []
    for word in a:
        small = word.lower()
        reverse = ""
        for l in small:
            reverse = l + reverse
        if small == reverse:
            plist.append(word)
    return plist


print(get_palindrom(["python", "madam", "raddar"]))


# Another Method
def get_palindrom(a):
    plist = []
    for word in a:
        small = word.lower()
        if small == small[::-1]:  # reverse using slicing
            plist.append(word)
    return plist


print(get_palindrom(["python", "madam", "raddar"]))
