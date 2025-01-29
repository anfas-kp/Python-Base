import random
win_count=0
loss_count=0
draw_count=0
while True:
    a=['rock','papper','sciccor']
    option=input('enter your choice(rock/papper/sciccor)\n')
    computer_choice=random.choice(a)
    print('your choice:',option)
    print('computr choice:',computer_choice)
    if option==computer_choice:
        print('draw')
        draw_count+=1
    elif option=='papper' and computer_choice=='rock':
        print('win')
        win_count+=1
    elif option=='rock' and computer_choice=='papper':
        print('win')
        win_count+=1
    elif option=='scissor' and computer_choice=='papper':
        print('win')
        win_count+=1
    else:
        print('loss')
        loss_count+=1       
    exit=input('do you want to countinue(yes/no)')
    if exit=='yes':
        continue
    else:
        break
print('no:of win:',win_count,'\nno:of loss:',loss_count,'\nno:of draw',draw_count)    
