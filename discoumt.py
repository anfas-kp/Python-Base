price=int(input('enter the price'))
if price>10000:
    print('discount is ',price*(20/100))
    print('net amount is ',price-(price*(20/100)))
elif price>7000 and price<=10000:
    print('discount is ',price*(15/100))
    print('net amount is ',price-(price*(15/100)))
elif price<=7000:
    print('discount is ',price*(10/100))
    print('net amount is ',price-(price*(10/100)))