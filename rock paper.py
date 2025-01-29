import random
a=['rock','papper','sciccor']
def game(u,c):
    print('your choice:',u)
    print('computr choice:',c)
    if u==c:
        print('draw')
    elif u=='papper' and c=='rock':
        print('win')
    elif u=='rock' and c=='papper':
        print('win')
    elif u=='scissor' and c=='papper':
        print('win')
    else:
        print('loss')       
while True:
    option=input('enter your choice(rock/papper/sciccor)\n')
    if option in a:
        computer_choice=random.choice(a)
        game(option,computer_choice)
        exit=input('do you want to countinue(yes/no)')
        if exit=='yes':
            continue
        else:
            break

#while True:
#def win