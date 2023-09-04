import numpy as np
a = np.array([[0, 0, 0],
             [1, 1, 1]]
             )
print(a)
# print(np.add.reduce(X, 0))
print(np.reshape(a, (3, 2)))
print("-"*40)
print(np.arange(3, 7))
print("-"*40)

print(a[1, 1])  # accessing elements of the matrix
print(a.shape)
print(a[:, 1])
print("-"*40)
print(a.max(axis=1))  # prints row wise maximum element
print(a.max(axis=0))  # prints column wise maximum element
print("squrt", np.sqrt(a))
print(np.std)

print("-"*40)


# generate a matrix

mat1 = np.arange(36).reshape(6, 6)
print(mat1)
mat2 = np.arange(36).reshape(6, 6)
print(mat2)
print("-"*40)
# print(np.vstack((mat1, mat2)))
# print(np.hstack((mat1, mat2)))
# print("-"*40)
print(mat1[-2])
print(mat1[1:3])  # gives two rows
boolean_mask = mat1 > 5
print(boolean_mask)
# np.concatenate(mat1, mat1)
# genrating random numbers
# res = np.random.RandomState(100)
# print(res.randint(100))
# print(res.standard_normal())
# print(res.random())

# print(a.ndim) #get dimension of the array


# structed array in numpy

x = np.array([('Rex', 9, 81.0), ('Fido', 3, 27.0)],

             dtype=[('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])

# print(x.Rex)
print(np.sort(x, order="age"))
print(np)
print(np.std(x['age']))
print(np.max(x['age'] > 25))
print(x[(x['age'] < 5) & (x["weight"] > 20)])
