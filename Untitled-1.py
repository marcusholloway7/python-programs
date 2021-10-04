import random
lower="abcdefghijklmpqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="!@*"
all= lower+upper+numbers+symbols 
length= 16
password="".join(random.sampleCall,length)
print(password)
