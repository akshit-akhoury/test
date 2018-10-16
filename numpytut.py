import numpy as np
a = np.array([1,2,3])
print(a)

a = np.array([[1,2,3],[4,5]])       #complex number

a = np.array([1, 2, 3,4,5], ndmin = 2)  #now it is a 2d array

a = np.array([1, 2, 3], dtype = complex) #sets the data type as complex

a = np.linspace(10,20,5) 
a.ndim 

a = np.arange(10)
b= a[2:11]


a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 
# this returns array of items in the second column 
print('The items in the second column are:')  
print (a[...,1]) 
print ('\n'  )
# Now we will slice all items from the second row 
print ('The items in the second row are:' )
print (a[1,...])   
print ('\n')  
# Now we will slice all items from column 1 onwards 
print ('The items column 1 onwards are:' )
print (a[...,1:])

x = np.array([[1, 2], [3, 4], [5, 6]]) 
y = x[[0,1,2], [0,1,0]] #select (0,0) (1,1) and (2,0)

x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 
rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]]) 
y = x[rows,cols]    #prints corner element of 4x3 matrix

z = x[1:4,1:3]   #slicing

y = x[1:4,[1,2]]  #advanced slicing

print(x[x > 5])  #boolean slicing

a = np.array([np.nan, 1,2,np.nan,3,4,5]) 
print (a[~np.isnan(a)])  #removes nan element


#Brodcasting 
a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]]) 
b = np.array([1.0,2.0,3.0])  
print('First Array + Second Array' )
print(a + b)


np.sum(a)

