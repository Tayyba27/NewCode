# Numpy Function Series
import numpy as np
array2d = np.array([[3,4,5] , [4,5,6] , [2,4,6]])
print(array2d)
array2d[:2]
arr = np.arange(1,11)
print(arr)

# boolean return krty hn
cond__arr = arr>5
print(cond__arr)
arr[cond__arr]
arr_2d = np.arange(50).reshape(5,10)
print(arr_2d)

arr_2d[2:4 , 4:]
# # Numpy Operation
# - Array with scalar , 
# - Array with array ,
# - Universal array function.
import numpy as np
arr = np.arange(0, 11)
print(arr)
add = arr +arr
print(add)
subtract = arr - arr
print(subtract)


scalar = arr +100
print(scalar)

scalar = arr * 50
print(scalar)

division = arr/100
print (division)

exponent = arr**3
print(exponent)

sqrt = np.sqrt(arr)
print(sqrt)

sin0 = np.sin(arr)
print(sin0)

cos0 = np.cos(arr)
print(cos0)


