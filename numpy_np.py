#Python program to rename the namespace numpy as np and use it to get an array of elements

import numpy as np

a = np.array([0,1,2,3,4,5,6,7,8,9])
print(a)
print("Sum:",np.sum(a))
print("Avg:",np.mean(a))
print("Max:",np.max(a))
print("Min:",np.min(a))
print("Len:",np.size(a))
print("First:",a[0])
print("Last:",a[-1])
