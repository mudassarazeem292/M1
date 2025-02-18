import numpy as np
# --------Creating Arrays---------
a = np.array([1,2,3])
print("a = ", a)
b = np.array([(1.5, 2, 3), (4,5,6)], dtype=float)
print("b = ", b)
c = np.array([[(1.5, 2, 3),(4, 5, 6)], [(3, 2, 1),(4, 5, 6)]], dtype=float)
print("c = ", c)
print(np.zeros((3,4)))
print(np.ones((2,3,4), dtype=np.int16))
# print(d = np.arange(10,25,5))
# print(e = np.full((2,2),7))
print(np.random.random((2,2)))
print(np.empty((3,2)))


# --------I/O--------
# np.loadtxt("myfile.txt")
np.save('my_array', a)
np.savez('array.npz', a, b)
np.load('my_array.npy')
np.savetxt("myarray.txt", a, delimiter=" ")


# --------Asking for help--------
np.info(np.ndarray.dtype)


# --------Inspecting your array--------
print(a.shape)
print(len(a))
print(b.ndim)
print(b.size)
print(c.dtype)
print(b.dtype.name)
print(b.astype(int))


# --------Array Mathematics--------
g = a - b
print(g)
print(np.subtract(a,b))
print(b+a)
print(np.add(b,a))
print(a / b)
print(np.divide(a,b))
print(a * b)
print(np.multiply(a,b))
print(np.exp(b))
print(np.sqrt(b))
print(np.sin(a))
print(np.cos(b))
print(np.log(a))
print(b.dot(a))
print(a == b)
print(a < 2)
print(np.array_equal(a,b))

print(a.sum())
print(a.min())
print(b.max(axis=0))
print(b.cumsum(axis=1))
print(a.mean())
print(np.median(b))
print(np.corrcoef(a))
print(np.std(b))


# --------Copying Arrays--------
h = a.view()
np.copy(a)
h = a.copy()
print(h)
