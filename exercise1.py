a = int(input("Write a number."))
Sum1=0
Sum2=0
count=-1
for i in range(1,a+1,2):
    Sum1=Sum1+i
print("Sum of odd numbers from 1 to",a,"is=",Sum1)
for k in range (0,a+1,2):
    Sum2=Sum2+k
    count=count+1
print("Average of even numbers from 1 to",a,"is=",Sum2/count)