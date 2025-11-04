import numpy as np
# help(np.add)
array = np.array([0,2,3,4,5])
# print("None of elements is zero : ", np.all(array !=0))#return true or false
array2 = np.array([1,7,2,5,4])
print("Greater :", np.greater(array , array2))
print("Greater Equall :", np.greater_equal(array , array2))
print("Less : ", np.less(array , array2))
print("Less Equall: ", np.less_equal(array , array2))
print("Equall : ", np.equal(array , array2))
