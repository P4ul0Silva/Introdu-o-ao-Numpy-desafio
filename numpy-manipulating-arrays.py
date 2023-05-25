import numpy as np


# Accessing Elements
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(f"A: {a} \n")


## Get a specific elemenet [r, c] (row / column)
print(f"A specific element [r, c]: \n{a[1, -2]} \n")

## Get specific row
print(f"A specific row a[0, :] \n{a[0, :]} \n")


## Get a specific column
print(f"A specific column a[:, 2] \n{a[:, 2]} \n")


## Slice [startindex:endindex:stepsize]
print(f"[startindex:endindex:stepsize] \n{a[0, 1:6:2]} \n")


## Changing Elements
a[1, 5] = 20
print(f"Change 13 for 20 \n {a} \n")


## Change all items on column 2 to "5"
a[:, 2] = 5
print(f"Change all items on column 2 to '5' \n {a[0]} \n {a[1]} \n")


## Change all items on cloumn 2 to '1' and '2' specifically
a[:, 2] = [1, 2]
print(f"Change all items on cloumn 2 to '1' and '2' specifically \n {a} \n")


## 3D example

b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f"Three dimensional Array \n")
print(f"{b} \n")


## Get specific element ( work oustide in)
print(f"Second element of first array in 3D array \n {b[0,1,1]} \n")
