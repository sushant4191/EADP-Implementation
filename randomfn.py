import random
a=int (input ("Input a value: "))
b=int (input ("Input b value greater than a: "))
if a<b:
    randno=random.randint(a,b)
elif a>b:
    randno=random.randint(b,a)
print(randno)
