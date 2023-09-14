#1. Print all integers from 0 to 150.
#2. Print all the multiples of 5 from 5 to 1,000
#3. Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
#4. Add odd integers from 0 to 500,000, and print the final sum.
#5. Print positive numbers starting at 2018, counting down by fours.
#6. Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, 
# print only the integers that are a multiple of mult. 
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)


#1.
for i in range(1,151):
    print(i)

#2.
for i in range(5,1005, 5):
    print(i)

#3.
for i in range(1, 101,):
    if i%10 == 0:
        print("Coding")
    elif i%5 ==0:
        print("Coding Dojo")
    else:
        print(i)

#4. 
#4. Add odd integers from 0 to 500,000, and print the final sum.
newlist = []
finalboss = 0

for i in range(0, 500000):
    if i%2 == 1:
        newlist.append(i)
        finalboss = finalboss + i
print(newlist)
print(finalboss)

#5.

for i in range(2018,0,-4):
    print(i)


#6. 

lownum = 2
highnum = 9
mult = 3

for i in range(lownum, highnum+1):
    if i%mult == 0:
        print(i)

# add odd integers from 0 - 5000 and print sum

#lets setup a for loop , in range (0,500000,)
#we need a temp variable to store the final sum, and we need an empty list to append my odd values to so that the right values can be addes
#use modulus to go through it 

list_to_add = []
finalnum = 0

for i in range(0,500000):
    if i%2 == 1:
        list_to_add.append(i)
        finalnum = finalnum + i
# print(list_to_add)
# print(finalnum)

#3. Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for i in range(1,100):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i%5==0:
        print("Coding")
    else:
        print(i)
        
        
#5. Print positive numbers starting at 2018, counting down by fours.

for i in range(2018, 0,-4):
    print(i)