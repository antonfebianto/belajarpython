import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

normal_array = np.random.normal(80,15,30)
sns.set()
plt.hist(normal_array, color='green',bins=50)

matrix_ordo_4x4 = np.matrix(np.ones((4,4), dtype=float))
print(matrix_ordo_4x4)

np.asarray(matrix_ordo_4x4)[1] = 2
print(matrix_ordo_4x4)

print("\n",3*"=","Numpy Arange()",3*"=")

data_list = range(0,11,2) #(start, stop, loncatan)
print(data_list)

for i in data_list:
    print(i)

print("\n")
bil_bulat = np.arange(0,20,1)
print(bil_bulat)

bil_ganjil = np.arange(1,20,2)
print(bil_ganjil)
bil_genap = np.arange(0,20,2)
print(bil_genap)

print("\n",3*"=","linspace & logspace",3*"=")

data_a = np.linspace(1.0, 5.0,num=10)
print(data_a)
data_b = np.linspace(1.0, 5.0, num=5, endpoint=False) #(start, end, num(jl.data), endpoint)
print(data_b)

print("\nLogspace")
data_log = np.logspace(2, 4.0, num=5)
print(data_log)

print('\nType data complex')
x = np.array([1,2,3], dtype=np.complex128)
print(x)
print(x.itemsize)

print("\nindexing and Slicing NumPy")
data_np = np.array([(1,2,3),(4,5,6)])
print(data_np)
print("Baris Pertama :", data_np[0])
print("baris Ke-2 :", data_np[1])
print('Kolom Ke-1 :', data_np[:,0])