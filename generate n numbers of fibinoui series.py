a=int(input('enter the range of series'))
def series(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return series(a-1)+series(a-2)
for i in range(0,a+1):
    print(series(i))