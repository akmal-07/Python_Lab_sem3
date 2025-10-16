import numpy as np

arrey = np.array([[10,20,5],[30,15,25],[24,32,78]])
print(arrey)
maximum_indeces = np.argmax(arrey,axis=1)
minimum_indeces = np.argmin(arrey,axis=1)
print("\nIndeces of maximum values along each rows:",maximum_indeces)
print("\nIndeces of minimum values along each rows:",minimum_indeces)
max_val = arrey[np.arange(len(arrey)),maximum_indeces]
minimun_value = arrey[np.arange(len(arrey)),minimum_indeces]
print("\nMaximun elements:",max_val)
print("\nMiniimun elements:",minimun_value)
