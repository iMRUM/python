#def moon_weight(weight, years):
#    for i in range(1,years):
#                moonweight=weight*0.165
#                print('at year %s your moonweight is %s kg'%(i, moonweight))
#                weight=weight+1
#weights=float(input('whats your weight'))
#year=int(input('for how many years'))
#moon_weight(weights, year)
###
def moonManip(init_weight, incr_weight, num_of_years):
    for j in range(1,num_of_years):
        init_weight=init_weight+incr_weight
        print('in year %s you were %s kg'%(j,init_weight))
a=float(input('whats your weight'))
b=int(input('how many years'))
c=float(input('whats the increase'))
moonManip(a,c,b+1)
