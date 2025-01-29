a=int(input('enter 1st number'))
b=int(input('enter 2nd number'))
c=input('enter the operators')
if c=='+':
    answer=a+b
elif c=='-':
    answer=a-b
elif c=='*':
    answer=a*b
elif c=='/':
    answer=a/b
elif c=='**':
    answer=a**b
elif c=='%':
    answer=a%b
elif c=='//':
    answer=a//b
print(a,c,b,'=',answer)