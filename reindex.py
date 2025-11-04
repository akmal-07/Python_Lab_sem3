import numpy as np
import pandas as pd
# data_list = pd.Series([10,20,30,40,50])
# print("pandas series created from lists :",data_list)
# data_list = data_list.tolist()
# print(data_list)
# print("type of the converted object:",type(data_list))
s1 = pd.Series([1,2,3],index=["a","b","c"])
s2 = pd.Series([10,20,30],index=["b","c","d"])
print(s1+s2)
