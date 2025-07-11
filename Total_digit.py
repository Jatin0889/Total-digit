# WAP to find the total digit in number 

count = 0 
n = int(input("enter your number:"))
while(n!=0):
    count = count + 1
    n = n//10
print(count)
