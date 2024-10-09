import numpy as np 

original = np.array([[1,2,3 ], [4,5,6] , [7,8,9]])

# permuted_array = np.random.permutation(original) 

permuted_rows = np.random.permutation(original)
permuted_cols = np.random.permutation(original.T).T

# print("original array : " , original)
# print("Permutation  array : " , permuted_array)

print("permuted Rows : " , permuted_rows)
print("permuted cols : " , permuted_cols)