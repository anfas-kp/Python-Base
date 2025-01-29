list1=[]
a=int(input('enter the length of list'))
for i in range(0,a):
    b=int(input('enter the numbers'))
    list1.append(b)
    print(list1)
def add(list1):
    length=len(list1)
    sum1=sum1+add(length)
    return sum1
result=add([a])
print(result)