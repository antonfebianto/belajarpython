import numpy as np

print(3*"=","Fungsi Statistik Numpy",3*"=")

np_normal_dt = np.random.normal(5, 0.5, 48)
print(np_normal_dt)
np_min = np_normal_dt.min()
np_max = np_normal_dt.max()
np_mean = np_normal_dt.mean()
np_std = np_normal_dt.std()

print("Min : ",np_min)
print("Max : ",np_max)
print("Mean : ",np_mean)
print("Std Deviasi :",np_std)

matrix_2d = np.array([(1,2,3),(4,5,6),(7,8,9)])
print(matrix_2d)

col_np_amin = np.amin(matrix_2d, axis=0)
col_np_amax = np.amax(matrix_2d, axis=0)
ro_np_amin = np.amin(matrix_2d, axis=1)
ro_np_amax = np.amax(matrix_2d, axis=1)

print("Kolom Min :",col_np_amin)
print("Kol Max :",col_np_amax)
print("Baris Min :",ro_np_amin)
print("Baris Max :",ro_np_amax)

print("\nRepeating Sequence")
data_a = [1,2,3]
print('Tile :', np.tile(data_a,2))
print('Repeat :',np.repeat(data_a, 2))

print(3*"=","Menghasilkan Bilangan Acak",3*"=")

acak_data = np.random.random(size=[2,3])
print(acak_data)

acak_huruf = np.random.choice(['a','i','u','e','o'], size=10)
print(acak_huruf)

print("\n")
rand_data = np.random.rand(2,2)
print(rand_data)
print("\n")

rand_data_b = np.random.randn(2,2) #membuat data minus
print(rand_data_b)
print("\n")

rand_int = np.random.randint(0,10, size=[5,3])
print(rand_int)

from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

nw_normal_dt = np.random.normal(5, 0.5, 48)
print(nw_normal_dt)

nw_min = np.min(nw_normal_dt)
nw_max = np.max(nw_normal_dt)
nw_mean = np.mean(nw_normal_dt)
nw_median = np.median(nw_normal_dt)
nw_modus = stats.mode(nw_normal_dt)
nw_std = np.std(nw_normal_dt)

print("Min :", nw_min)
print("Max :", nw_max)
print("Mean :", nw_mean)
print("Median :",nw_median)
print("Modus :", nw_modus)
print("StDev :", nw_std)

sns.set()
#plt.hist(nw_normal_dt, color='blue', bins=21)
#plt.show()

# numpy.dot(): Dot Product in Python using Numpy
# Dot Product
# Numpy is powerful library for matrices computation. For instance, you can compute the dot product with np.dot

# Syntax

# numpy.dot(x, y, out=None)
print(3*"=","Aljabar Linier",3*"=")
print("np.dot()")
## Linear algebra
### Dot product: product of two arrays
mtx_a = np.array([1,2,3])
mtx_b = np.array([4,5,3])

p_kali = np.dot(mtx_a, mtx_b)
print(p_kali)

print("\nnp.matmul()")

mtx_c =np.array([[1,2],[3,4]])
mtx_d =np.array([[5,6],[7,8]])

p_matmul = np.matmul(mtx_c, mtx_d)
print(p_matmul)

print("\nDeterminan")
p_determinan = np.linalg.det(mtx_d)
print(p_determinan)

p_zeros = np.zeros((8,8))
p_zeros[1::2,::2] = 1
p_zeros[::2,1::2] = 1
print(p_zeros)

print("\n")

nw_list = [x + 2 for x in range(0,11)]
print(nw_list)

np_arr = np.array(range(0,11))
print(np_arr + 2)

temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
print(pressure)


#plt.plot(temp,pressure)
#plt.xlabel('Temperature in oC')
#plt.ylabel('Pressure in atm')
#plt.title('Temperatur Vs Tekanan')
#plt.xticks(np.arange(0,6, step=0.5))

print("\nMetode Gaussian")

mu = 28
sigma = 15
sample = 1000

dx = np.random.normal(mu, sigma, sample)
ax = sns.distplot(dx)
ax.set(title="Covid-19(Used Random Data)",xlabel='x', ylabel='y')
plt.show()
