##scientific computing language. 
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)

#2d and 3d array
b = np.array([[1,2,3],[4,5,6]])
print(b)

c= np.array([[[1,2],[3,4]],[[4,5],[5,6]]]) #-tensor

#dtype = used to change the datatype of a list
new = np.array([1,2,3],dtype=float)
print(new)

new2 = np.array([1,2,3],dtype=complex)
print(new)

#np.arange: just like pythons range 
np.arange(1,11)

#with reshape = use to make diff types of matrix  
np.arange(1,13).reshape(4,3)

#np.ones and np.zeroes = use to make an array with 1s or 0s
#use case = to initialize arrays 
np.ones(3,4)
np.zeros(3,3)
rand = np.random(3,4)
print(rand)


