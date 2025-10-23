# Recursive Function :
def re_func(a):
    if a == 1:  # Base Condition
        return 1
    else:
        return a * re_func(a - 1)


print(re_func(5))
 
# Do Lab Manual Tasks Related to this topic
