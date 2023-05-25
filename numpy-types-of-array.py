import numpy as np

# All 0s matrix
print(f"Initialize all zeros matrix of length 2 \n{np.zeros((2))} \n")
print(f"Initialize all zeros 2 dimensional matrix of 2 x 3 \n {np.zeros((2, 3))} \n")
print(
    f"Initialize all zeros 3 dimensional matrix of 2 x 3 x 3 \n{np.zeros((2, 3, 3))} \n"
)
print(f"Initialize all zeros 4 Dimensional 2 x 3 x 3 x 2 \n{np.zeros((2, 3, 3, 2))} \n")


# All 1s matrix
print(
    f"Initialize all ones matrix with dtype int32 \n {np.ones((4, 2, 2), dtype='int32')} \n"
)


# Any other number
print(
    f"Initialize with any number a float32 dtype array 2 dimensional array \n {np.full((2, 2), 99, dtype='float32')} \n"
)

# Any other number (full_like) to reuse from other arrays
a = np.array((2, 2))
print(
    f"Any other number (full_like) to reuse from other arrays \n {np.full_like(a, 4)} \n"
)


# Random decimal numbers
print(f" Random decimal numbers \n {np.random.rand(4,2)} \n")

# Random Integer values
print(f" Random decimal numbers \n {np.random.randint(-4, 8, size=(3,3))} \n")


# The identity matrix (square matrix)
print(f"The identity matrix \n {np.identity(5)} \n")


# Repeat an array
arr = np.array([[1, 2, 3]])
r1 = np.repeat(arr, 3, axis=0)
print(f"Repeat an array: \n{r1} \n")
