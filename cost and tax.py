cost=int(input('enter price of the bike'))
if cost>=100000:
    print('total cost=',cost+(cost*15/100))
    print('tax=',cost*15/100)
elif cost>=50000:
        print('total cost=',cost+(cost*1/100))
        print('tax=',cost*10/100)
elif cost<=50000:
    print('total cost=',cost+(cost*5/100))
    print('tax=',cost*5/100)