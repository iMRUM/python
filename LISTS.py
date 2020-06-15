wizard_list=['spider legs','toe','eye','bat','slug','snake']
print(wizard_list)
print(wizard_list[2])
wizard_list[2]='tongue'
print(wizard_list[2])
print(wizard_list[1:4])

numbers=[1,2,3,4]
strings=['this','list','contains','lists, numbers and strings']
mylist=[numbers,strings]
print(mylist)

mylist.append('added item to the list')
print(mylist)

del mylist[2]
print(mylist,'deleted it')

print(wizard_list+mylist)

comblist=wizard_list+mylist
print(comblist)
