import numpy as np
import pandas as pd

my_matrix = np.identity(5)
# print(my_matrix)

<<<<<<< HEAD
another_matrix = np.random.randint(10, size=(3, 4))
#print(another_matrix)
=======
another_matrix = np.random.randint(10, size=(3, 5))
print(another_matrix)
>>>>>>> master

sorted_matrix = np.sort(another_matrix, axis=1)
#print(sorted_matrix)

def my_func(matrix_1, matrix_2):
    try:
        return matrix_1 * matrix_2
    except ValueError:
        print("matrices are not aligned")
        return None

print(my_func(my_matrix, another_matrix))