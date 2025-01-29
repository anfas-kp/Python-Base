a=int(input("enter the mark of maths:"))
name=input("enter your name: ")
if a>100:
    print('error')
elif a>=90:
    print(name,': A+')
elif a>=80:
    print(name,':A')
elif a>=70:
    print(name,": B")
elif a>=60:
    print(name,':C')
elif a>=50:
    print(name,': D')
else:
    print(name,': fail')