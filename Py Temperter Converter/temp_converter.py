#here we ask the user for the temp input
temp = float(input("Enter temperature in Fahrenheit: "))
#add our coversion scale
celsius = (temp - 32) * 5/9
#and finally ask it to print our results.
#using the f string to shorten string instead of format.
print(f"{temp} in Fahrenheit is equal to {celsius} in Celsius")

#For Celsius to Fahrenheit, instead use below...
# temp = float(input("enter temperature in celcius:")) 
# Fahrenheit = (celsius*9/5)+32 
# print(f"{temp} in Celsius is equal to {Fahrenheit} in Fahrenheit") 
