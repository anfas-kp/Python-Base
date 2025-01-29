set={'anfas',21,True,'mes',2002,'vazhikkadavu'}
set1={'name','age','course'}
#set1=set(('mnlpdm'))-to create set using key word
print(set) #set has no index
print(len(set))#length
print(21 in set)# to find elements in set
set.add('arg') #adding element to set
print(set)
set.update(set1) #adding  2 sets
print(set)
set.remove(21) # to remove a selected element
set.discard(21)
set.discard('mes') #=.remove
print(set) 
set.pop() #to dlt a element
print(set)