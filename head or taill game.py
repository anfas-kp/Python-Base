import random
prize=100
while True:
    coin_toss=('head','tail')
    a=input('enter (head/tail)\n')
    a.lower()
    computer_choice=random.choice(coin_toss)
    print('computer choice is:',computer_choice)
    if a==computer_choice:
        print('win')
        prize+=10
    else:
        print('loss')
        prize-=1
    if prize==200 or prize==0:
        break
    end=input('do you want to exit(yes/no)\n')
    if end=='yes':
        continue
    else:
        break
print('yourbalance is:',prize)