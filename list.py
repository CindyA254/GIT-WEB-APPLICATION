#list
my_list =[1, 2, 3, 4, 5, 6, 7, 8]
print(my_list)
print(my_list[2]) #print 2nd index value
print(my_list[7]) #print 7th index value
print(my_list[1:4]) #print a range
my_list[1] = 200 #replace a value
print(my_list)
my_list[4] = 500 #replace a value
print(my_list)
my_list.append(73) #insert at the end of the list
print(my_list)

my_list.insert( 3,5)
my_list.extend([43,646,678])
print(my_list)

my_list.remove(6)
print(my_list)

del my_list[1]
print(my_list)

my_list.clear()
print(my_list)

my_list.extend([131,132,133,144,155])
print(my_list)
del my_list
#print(my_list)

my_list2 =[313,543,767,7888,9875]
print(my_list2)

my_list2.append(535)
print(my_list2)
if 535 in my_list2:
    print('The value is in the list')
else:
    print('The value is not found')

my_list3 = [100,200,300,400,500,600,700,800,100,200,300,400,500,600,700,800,100]
#counting number of times value is in a list
print(my_list3.count(100))

#identifying the maximum value in a list
max(my_list3)
print(max(my_list3))

#identify minimum value in a list
min(my_list3)
print(min(my_list3))

#Addition of all values in the list
sum(my_list3)
print(sum(my_list3))

#lenth of the list of values
print(len(my_list3))

#identify an index
print(my_list.index(400))

#create a list of 5 strings; add two more strings,
# check if a specific string is present or not,
# add three more integers.

my_list4 = [5000,'Sarah','Bob',3000,'Felix']
print(my_list4)

my_list4.append([200,400])
print(my_list4)

if 'Adam' in my_list4:
    print('The value is in the list')
    print(my_list4)
my_list4.append([200,300,400])











