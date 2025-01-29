a=input('enter the string')
def pallendrome(a):
    b=a[::-1]
    if a==b:
        print('pallendrome')
    else:
        print('not')
pallendrome(a)