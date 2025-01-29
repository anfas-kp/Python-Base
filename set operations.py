set1={1,2,3,4,5}
set2={5,6,7,8,9}
set3=set1.union(set2)
set4=set1.intersection(set2)
set5=set1.difference(set2)
print('unioun of set1 & set2=',set3)
print('intersection of set1 & set2=',set4)
print('diffrence of set1 & set2=',set5)

set1={1,2,3,4,5}
set2={5,6,7,8,9}
a={9,10,11,12,13,14}
tuple1=('apple','orange')
list1=[1,'q']
strg1=('a')
e=set1.union(tuple1,list1,strg1) #union set with all data type
c=set1.union(tuple1) #set&tuple
#all operation same as unioun
b=set1|set2|a 
set3=set1|set2 #unioun
set4=set1&set2 #intersection
set5=set1-set2 #diffrence
set6=set1^set2 #symmentric
print('intersection=',set4)
print('diffrence=',set5)
print('symmetric=',set6)#remove all common elemnt fron sets and print reamining unique elements
print(b)
print(c)
print(e)

a={1,2,3,4,5}
b={3,4,5,6,7,8}
a.intersection_update(b) #overwrite a by result of intersection of a&b
b.difference_update(a)
print('intersection update of b to a = ',a)
print('diffrence update of a to b = ',b)

a={1,2,3,4,5}
b={3,4,5,6,7,8}
a.symmetric_difference_update(b) 
print('symmetric diffr update=',a)

#subset&superset
a={1,2,3,4,5}
b={3,4,5}
print(b.issubset(a))
print(a<=b)
print(a.issuperset(b))
print(a<=b)