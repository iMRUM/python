x=0
while x<=20:
    print(x)
    x = x+2

ingredients=['bbq','chilli','mayo','ketchup','pickles']
p=1
for i in ingredients:
    print('%s, %s'%(p,i))
    p=p+1

weight = 80
for j in range(1,16):
    moonweight = weight*0.165
    print('at year %s moon weight is %s'%(j,moonweight))
    weight=weight+1
