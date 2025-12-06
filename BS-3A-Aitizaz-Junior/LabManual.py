perc = float(input("Enter percentage: "))
if 91 <= perc <= 100:
    g = "A+"
elif 81 <= perc <= 90:
    g = "A"
elif 71 <= perc <= 80:
    g = "B+"
elif 61 <= perc <= 70:
    g = "B"
elif 51 <= perc <= 60:
    g = "C"
else:
    g = "F"
print("Grade:", g)
# lab 4 Task
lst = [1, 8, 0, 1, 6, 7, 3, 1, 5]
search_value = 1
replacement = 100

for i in range(len(lst)):
    if lst[i] == search_value:
        lst[i] = replacement

print("Updated list:", lst)
# task 2
lst = [8, 11, 9, -4, 5, -3, 15, 10, -2]

for i in range(len(lst)):
    if lst[i] < 0:
        lst[i] = -lst[i]

print("All positives:", lst)
# task 3
lst = [9, 1, 10, 29, 35, 19, 52, 34, 16, 48, 11]

count_in = 0
count_out = 0

for num in lst:
    if 30 <= num <= 50:
        count_in += 1
    else:
        count_out += 1

print("Inside range:", count_in)
print("Outside range:", count_out)


# Lab 5
# flat list
def Count(a):
    c = 0
    for _ in a:
        c += 1
    return c


def Count_Z(a):
    return sum(1 for x in a if x == 0)


def Search(a, s, r):
    return [r if x == s else x for x in a]


def Reverse(a):
    out = []
    for x in a:
        out.insert(0, x)
    return out


def Delete(a, d):
    return [x for x in a if x != d]


# Nested List
def Count_nested(a):
    c = 0
    for x in a:
        if isinstance(x, list):
            c += Count_nested(x)
        else:
            c += 1
    return c


# Lab 6 Recursion
def Count_rec(a):
    if a == []:
        return 0
    head = a[0]
    tail = a[1:]
    if isinstance(head, list):
        return Count_rec(head) + Count_rec(tail)
    return 1 + Count_rec(tail)


def Reverse_rec(a):
    if a == []:
        return []
    return Reverse_rec(a[1:]) + [a[0]]


def Search_rec(a, s, r):
    if a == []:
        return []
    head = a[0]
    tail = a[1:]
    if isinstance(head, list):
        return [Search_rec(head, s, r)] + Search_rec(tail, s, r)
    return [(r if head == s else head)] + Search_rec(tail, s, r)


def Delete_rec(a, d):
    if a == []:
        return []
    head = a[0]
    tail = a[1:]
    if isinstance(head, list):
        return [Delete_rec(head, d)] + Delete_rec(tail, d)
    if head == d:
        return Delete_rec(tail, d)
    return [head] + Delete_rec(tail, d)


def CountZ_rec(a):
    if a == []:
        return 0
    head = a[0]
    tail = a[1:]
    if isinstance(head, list):
        return CountZ_rec(head) + CountZ_rec(tail)
    return (1 if head == 0 else 0) + CountZ_rec(tail)
