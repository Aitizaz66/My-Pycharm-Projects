#Data Structure in Python
# List , Set , Tuple, Dictionary
# 1: List
# Lists Store Multiple types of Data.Support Indexing. []use symbol.positive index start from 0 and reading left to right
# while negative index start from -1 and read from right to left.support sequence matters.support Duplicate.
l=[1,2,3,4,"Ali",2.33]
print(l[-1])

# 2: Set
# Use curly brackets{}.Not Support indexing.Not support sequence.Not Support Duplicate Skip it.
s={1,2,3,4,"Ali",1.1,55,3,2}
print(s)

#Mutable
l[1]=33
l.pop()
s1={1,2,3,4,5,6,7,8,9,0,"4545",11,34,554}
s1.add(9999)
print(s1)
#pop use for removing if we not pass index then it will remove last item
#remove use for remove value

# 3: Tuple
# use parenthesis bracket. Support indexing. support Sequence.not support changing in data or adding new data. Immutable.
t1=(1,2,3,4,5,6,7,8,9)
print(t1[1])
