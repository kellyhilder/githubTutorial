import numpy as np

my_matrix = np.identity(4)
# print(my_matrix)

another_matrix = np.random.randint(10, size=(3, 4))
print(another_matrix)

sorted_matrix = np.sort(another_matrix, axis=1)
print(sorted_matrix)