count_even=0
count_odd=0

sum=0

sum_even=0
sum_odd=0

avg_even=0
avg_odd=0
avg=0

for i in range (0,20):
    num=int(input("Enter : "))
    if num%2==0:
        count_even=count_even+1
        sum_even=num+sum_even
    else:
        count_odd=count_odd+1
        sum_odd=num+sum_odd
        
sum=sum_odd+sum_even
count=count_odd+count_even

print(f"Count of even numbers is : {count_even}")
print(f"Count of odd numbers is : {count_odd}")
print(f"Sum of even numbers is : {sum_even}")
print(f"Sum of odd numbers is : {sum_odd}")
print(f"Average of even numbers is : {sum_even/count_even}")
print(f"Average of odd numbers is : {sum_odd/count_odd}")    
print(f"Sum of all numbers is : {sum}")
print(f"Average of all numbers is : {sum/count}")    
        
    