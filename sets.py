Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])

#We cannot access individual values in a set. We can only access all the elements together

for item in Days:
    print(item)

#removing an item from set
Days.discard("Sun")
print(Days)    

#adding items in a set
Days.add("Sunday")
print(Days)

#union of sets
a = set(['1','2','3'])
b = set(['3','4','5'])
allset = a|b
print(allset)

#intersection of sets
allset = a & b
print(allset)

#difference of sets
allset = a - b
print(allset)

#compare sets
subset = a <= b
superset = a >= b
print(subset)
print(superset)