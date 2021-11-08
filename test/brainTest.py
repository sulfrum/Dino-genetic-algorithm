import numpy as np


def mutate(W,B):
    W += np.random.uniform(-1, 1, (5,2))
    B += np.random.uniform(-1, 1, (1,2))

# obstacle params
#[distance height speed width, boh]
X = np.array([[100, 50, 10, 50, 22]])
print("X: \n", X)

#W = np.array([[1.1, 1.0], [1.5, -3.2], [0.1, 0.9], [0.2, 1.1]])
#np.random.seed(1)

W = np.random.rand(5,2)

print("W: \n", W)
#B = np.array([[7, -1]])

W = np.random.rand(5,2)
B = np.zeros((1,2))

mutate(W,B)
print("X: \n", X)

print("X shape ", X.shape)
print("W shape ", W.shape)
print("B shape ", B.shape)

Z = np.matmul(X, W) + (B)
print("Z: \n", Z)

print("-- negative --")
with np.nditer(Z, op_flags=['readwrite']) as it:
    for item in it:
        if(item<0):
            print(item)
            item[...] = 0
print("---")
print(Z[0][1])
print("---")
print(np.random.uniform(-500, 500, (4,2)))
print(np.random.uniform(-500, 500, (4,2)))
print(np.random.uniform(-500, 500, (4,2)))
print(np.random.uniform(-500, 500, (4,2)))
