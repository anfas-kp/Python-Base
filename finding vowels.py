a=(input('enter a word'))
count=0
C='aioeuAIOUE'
for i in a:
    if i in C:
        count=count+1
print(count)