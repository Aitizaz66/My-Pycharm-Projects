# 1
l1 = [1, 2, 3, 7, 8, 9, 4, 66, 8, 1, 2, 99, 45, 78, 15]
l2 = []
l3 = ["ali", 34, 4.4, 'khan', 66, 0, 1, 8, 36.69]
print(l1[5] == 6)
print(1 == l1[0])
print(l3[0] == 'ali')
# 2
# l1.

# 3
l2.insert(0, 28)
print(l2)
l2.append(45)
print(l2)
l2.extend(l1)
print(l2)

# 4
l3.insert(0, 'ahmad')
print(l3)

# 5
l1.remove(99)
print(l1)
l2.pop()
print(l2)  # remove last index
l3.clear()
print("l3", l3)

# 6
print(l1[-1] == 15)
print(l2[0:-1] == 90)
print(l3[0:-1])

# 7
# l1.sort(l1,1,not)
l1.reverse()
print(l1)

# 8
# print(len(l1))
# print(max(l1)
# print(min(l1))
# print(sum(l1))
