import numpy as np

# initialize array
a = np.array([1, 2, 3])
print(f"Print array A: \n{a} \n")

# To specify data size
# a = np.array([1,2,3], dtype='int16')

# Initialize 2 dimension array
b = np.array(
    [
        [
            9.0,
            8.0,
            7.0,
        ],
        [6.0, 5.0, 4.0],
    ]
)
print(f"Print array B: \n{b} \n")


# Get dimension
print(f" A Dimension: {a.ndim} dimension \n")
print(f" B Dimension: {b.ndim} dimension \n")

# Get Shape
print(f"A Shape: {a.shape} Its just a vector so it prints the length \n")
print(f"B Shape: {b.shape} rows and columns \n")


# Get data type
print(f"A data type: {a.dtype} \n")


# Get Item size
print(f" A item size: {a.itemsize} bytes \n")

# Get total size
print(f"A size: {a.nbytes} bytes \n")
