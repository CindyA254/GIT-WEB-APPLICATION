#list
list1=[1,2,3,4,5,6,7,8,9,10]
sum(list1)
print(sum(list1))


#2 inputs; math and english
#if any of the inputs is less than 30, you fail
#if any of them is above 30 you have passed

print("Examination calculation")
name = input("what is the name of the student? ")
Mathematics = int(input("what is the mathematics grade of the student ? "))
English = int(input("what is the English grade of the student? "))

if Mathematics >= 30.0 or English >= 30.0:
    print("The student has passed the exam")
elif Mathematics <=29.9 or English <= 29.9:
    print("The Student has failed the exam")
else: ()



