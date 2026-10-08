# arr = [1,2,3,4,5]
# print(arr)

# Creating a 1D array using numpy
""""import numpy as np
array_1D =  np.array([1,2,3,4,5,6])
print(array_1D)"""


#2D_array
# Creating a 2D array using numpy
"""import numpy as np
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

print("2D Array:\n", array_2d)"""

#MD_array
# Creating a Multi-Dimensional array using numpy
"""import numpy as np
array_md = np.array([[[1, 2], [3, 4]],
                     [[5, 6], [7, 8]]])
print("Multi-dimensional Array:\n", array_md)"""

#Matrix
# Creating a matrix using numpy
"""matrix = np.matrix([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
print("Matrix:\n", matrix)"""



#Creating with default array
#np.zeros(shape) (3) for 1D, (3,3) for 2D
"""import numpy as np
zeroes_array = np.zeros(3)
print(zeroes_array)"""

#np.ones(shape)
"""import numpy as np
ones_array = np.ones((2,3))
print(ones_array)"""

#full(shape,values)
"""import numpy as np
filled_array = np.full((2,2),7)
print(filled_array)"""