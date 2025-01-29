num=int(input('enter the number'))
month=['january','february','march','april','may','june','july','august','september','october','november','december']
if num<1 or num>12:
    print('error')
else:
    print(month[num-1])


    num=int(input('enter the number'))
month={1:'january',2:'february',3:'march',4:'april',5:'may',6:'june',7:'july',8:'august',9:'september',10:'october',11:'november',12:'december'}
if num<1 or num>12:
    print('error')
else:
    print(month[num])

num=int(input('enter the number'))
month=('january','february','march','april','may','june','july','august','september','october','november','december')
if num<1 or num>12:
    print('error')
else:
    print(month[num-1])