import numpy as np

a = np.linspace(1, 20, 15)
print(a)

b = a.reshape((3, 5))
print(b)
# print("maximum is", np.max(b, axis=1))
t = np.where(b == np.max(b, axis=1, keepdims=True), 0, b)
print(t)
