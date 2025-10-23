# write a fuction that take a list and find maximum number and return number
def max(*m):
    max = 0
    for i in m:
        if i > max:
            max = i
    return max


print(max(12, 34, 5345, 4545, 98, 234023))


# write a function that count even odd
def count_even(*eo):
    co = 0
    ce = 0
    for i in eo:
        if i % 2 == 0:
            ce += 1
        else:
            co += 1
    return "Odd = ", co, "Even = ", ce


print(count_even(123, 23, 5, 56, 9, 6, 8, 4, 10))


# write a functon to remove duplicate from list and return updated list with no duplicate.(take list as input)
def remove_duplicate(input_list):
    ulist = []
    for item in input_list:
        if item not in ulist:
            ulist.append(item)
    return ulist


my_list = [1, 2, 2, 3, 4, 4, 5]
updatelist = remove_duplicate(my_list)
print("without duplicates:", updatelist)


# write function tht filter long words and return new list of words that are less than n words
def filter_words(n, *wl):
    filter_list = []
    for w in wl:
        if len(w) < n:
            filter_list.append(w)
    return filter_list


filtered_list = filter_words(6, 'apple', 'mango', 'banana', 'orange', 'Guvava')
for word in filtered_list:
    print(word)
