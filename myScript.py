import numpy as np
import pandas as pd

my_matrix = np.identity(5)
# print(my_matrix)

another_matrix = np.random.randint(10, size=(3, 5))
print(another_matrix)

sorted_matrix = np.sort(another_matrix, axis=1)
print(sorted_matrix)