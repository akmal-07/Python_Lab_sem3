import numpy as np
arr = np.array([[10,20,5],[30,15,25]])
target = 18
less_than  = arr[arr<target]
greater_than = arr[arr>target]
print("Less than target : ",less_than)
print("Greater than target :",greater_than)
