num=int(input("Enter a two digit number:"))
#extracting the digits to get each number seperately
tens=num//10
ones=num%10
#reversing the number
rnum=ones*10 +tens
print("Reversed number:",rnum)