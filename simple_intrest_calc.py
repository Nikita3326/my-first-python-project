#program to calculate simple intrest
#asking user for principal amount,interst rate and time 
p=float(input("Enter principal amount:"))
r=float(input("Enter rate of intrest:"))
t=float(input("Enter time (in years):"))
#calculating simple intrest (principl amount*intrest rate*time)
si=(p*r*t)/100
print("simple intrest=",si)