#Sample Coding Questions 01 Week 01
#AHAMMAD BIN KABIR AL SAGOR

import array as arr
array1 = arr.array('i', [1, 4, 7, 9])
print(array1)

a = 1
b = 2
c = 3
d = 4
e = ((a - ((b ** c) // d)) + (a % c))
print(e)

temperature = 32.6
print("The temperature today is: {:.3f} degrees Celsius".format(temperature))

userAge = int(input("Enter your age: "))
userAge = userAge + 22
print("Now showing the shop items filtered by age:", userAge)