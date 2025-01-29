f=float(input('enter the teamp'))
def convert(f):
    celsius=(f-32)*5/9
    return celsius
farenheat=convert(f)
print(farenheat)

c=float(input('enter the teamp'))
def convert(c):
    farenheat=9*c/5+32
    return farenheat
celsius=convert(c)
print(celsius)