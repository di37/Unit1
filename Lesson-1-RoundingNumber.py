#Homework - Rounding Numbers

x = 3.14159
num = x  + 0.5 #Main variable + 0.5 that allows to round off
s = str(num)
point = s.find('.')
final = float(s[:point]) #0,1
print (final)
