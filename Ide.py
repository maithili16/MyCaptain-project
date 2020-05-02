# cook your dish here
n=int(input("enter the number of terms:"))

a=0
b=1 
count=0

if n<=0:
    print("please enter positive number of terms.")
elif n==1:
    print("The fibo sequence is:")
    print(a)
else:
    print("The fibonacci sequence is:")
    while count <n:
        
        print(a)
        c=a+b 
        
        a=b 
        b=c 
        count=count+1 