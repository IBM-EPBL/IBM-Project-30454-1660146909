import random
temp=random.randint(20,100)
humid=random.randint(30,50)#normal humidity range:30 to 50 %
print("The Temperature is",temp)
print("The humidity is",humid)
if(temp>30):#normal room temp=20 to 30 (degree celsius)
 print("HIGH TEMPERATURE IS DETECTED!")
else:
 print("Temperature is within the range!")
