my_tuple = (123,232,332,454,545)
print(my_tuple)
print(my_tuple[2])
print(my_tuple[2:4])
print(len(my_tuple))
del my_tuple
#print(my_tuple)

my_tuple2 = (100,200,'cooking')
if 'cooking' in my_tuple2:
    print(' yes cooking is present')

else:
    print('no,cooking is present')

print(max(my_tuple2))
print(min(my_tuple2))
print(my_tuple2)
print(sum(my_tuple2))
print(my_tuple2.count(100))
print(sum(my_tuple2)/len(my_tuple2))
#my_tuple2[2] = 'eating'
#tuple does not allow modification of values
#print(my_tuple2)

