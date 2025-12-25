# Practice the following Recursive Functions:
# 1)	Sum of list elements. Done
# 2)	Sum of nested/all values of list. Note list may be nested.Done
# 3)	Count even odd numbers from list. Done
# 4)	Count specific value from list.Done
# 5)	Calculate factorial of specific number.Done
# 6)	Check if list contain palindrome value or not.Done
# 7)	Reverse the list using recursion.Done
# 8)	Count multiple of specific numbers from list.Done
# 9)	Count how many values are integer in list.Done
# 10)	What does the following   function   do?


# Sum Of List Recursive Function
def sum_list(a, sum=0):
    if a == []:
        return sum
    else:
        return sum_list(a[1:], a[0] + sum)


print("Sum = ", sum_list([1, 2, 4, 5, 6, 7, 8]))


# Sum OF Nested List All Values
def sum_nested(lst):
    total = 0
    for item in lst:
        if type(item) == list:
            total += sum_nested(item)
        else:
            total += item
    return total


nested_list = [1, [2, [3, 4], 5], 6]
print("Total sum Of Nested list :", sum_nested(nested_list))


# count even odd
def count_even_odd(n, even=0, odd=0):
    if n == []:
        return (even, odd)
    else:
        if n[0] % 2 == 0:
            even += 1
        else:
            odd += 1
        return count_even_odd(n[1:], even, odd)


print("Even,Odd Count", count_even_odd([1, 2, 5, 6, 8, 10, 12, 13]))


# Count Specific Value From list
def count_value(a, value, count=0):
    if a == []:
        return count
    else:
        if a[0] == value:
            count += 1
        return count_value(a[1:], value, count)


print("Count Specific Value = ", count_value([1, 2, 3, 2, 3, 3, 4, 6, 3], 3))


# Calculate Factorial Of Specific Value
def fact_value(value):
    if value == 0 or value == 1:
        return 1
    else:
        return value * fact_value(value - 1)


print("Factorial Of Value : ", fact_value(5))


# Check palindrome


def is_palindrome(val):
    val = str(val)
    return val == val[::-1]


def contains_palindrome_recursive(lst, index=0):
    if index >= len(lst):
        return False
    if is_palindrome(lst[index]):
        print("Palindrome found:", lst[index])


contains_palindrome_recursive(my_list)


# Reverse List
def reverse_list(lst):
    if len(lst) == 0:
        return []
    return [lst[-1]] + reverse_list(lst[:-1])


print("Reverse List : ", reverse_list([1, 2, 3, 4, 5]))


# Count Multiple of Specific Number
def count_multiples(a, value, count=0):
    if a == []:
        return count
    else:
        if a[0] % value == 0:
            count += 1
        return count_multiples(a[1:], value, count)


print("Count Of Multiples OF Specific Value : ", count_multiples([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))


# Count Values that Integers In list
def count_int(a, count=0):
    if a == []:
        return count
    else:
        if type(a[0]) == int:
            count += 1
        return count_int(a[1:], count)


print("Count Integers In List : ", count_int([1, 2, "a", 'ali', 4, 7, "Aitizaz"]))


# Print Table in Recursion
def table(n, start=1, end=10):
    if start > 10:
        return
    else:
        print(n, " * ", start, " = ", n * start)
        return table(n, start + 1)


print(table(10))
