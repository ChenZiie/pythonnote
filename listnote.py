list1=[1,2,3,4,5,6,7,8,9]

y=[10]

list1.append(10)
print(list1)

list1.extend(y)  # y is a list, this is as same as x+y
print(list1)

list1.insert(0,4)  # 0 is the position , 4 is the value you want to insert
print(list1)

list1.remove(4)   # only remove the first one  (the first 4 in the list)
print(list1)

list1.pop(0)    #  remove the vaule in the position 0
print(list1)

list1.reverse()  # reverse the list   ,  is the same as list1 = list[::-1] this is not change the list
print(list1)

list1.sort()     # 排序

list1.count(8)    # count how many time the 8(value) occur

list1.index(8)   # the position of the first value 8 occur

c=list(range(0,9,2))  # list the range from 0 to 9 by the distance 2   i.e.[0,2,4,6,8]

plist=[1,2,3,4,5]
plist[4]+=5
print(plist)

m = input().split()

print(' '.join(m[::-1]))