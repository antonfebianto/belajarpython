import numpy as np
print('numpy :', np.__version__)
# print(dir(np))

print("\n",3*"=","Array W/ Numpy",3*"=")
d_angka = [1,2,3,4,5]
print("type data :" , type(d_angka))
print(d_angka)




print('\nMembuat Vector') #Membuat Vector
a = np.array([1,2,3,4,5])
b = np.array([1.3,2.4,3.5])
print(a)
print(b)

print('\nMembuat Range') #Membuat Range
c = np.arange(1,10,2)
print(c)

print('\nMembuat Linspace') #Membuat Linspace/jarak spasi
d = np.linspace(1,10,4)
print(d)

print('\nArray Multidimensi/Matrix') #Membuat Matrix
e = np.array([(1,2,3),(4,5,6)])
print(e)

print('\nMatrix Dengan Nol') #Membuat matrix dengan 0
f = np.zeros((5,5))
print(f)

print('\nMatrix Dengan 1') #Membuat matrix dengan 1
g = np.ones((5,5))
print(g)

print('\nMatrix identitas') #Membuat matrix identitas u/ AI
h1 = np.identity(5)
h2 = np.eye(5)

print(h1)
print("\n",h2)



print(2*'\n')

two_dd = [[0,1,2],[3,4,5],[6,7,8]]
print(two_dd)

array_numpy = np.array(d_angka)
print(type(array_numpy))
print(array_numpy)

print("\n",3*"=","Array W/ Numpy (float)",3*"=")
array_numpy1 = np.array(d_angka, dtype=float)
print(array_numpy1)

print("\n",3*"=","Array W/ Numpy (Boolean)",3*"=")
d_angka2 = [0,1,-1,0,0]
array_numpy2 = np.array(d_angka2, dtype=bool)
print(array_numpy2)

print("\n",3*"=","Array W/ Numpy (Mltidimensi)",3*"=")
twodd_list = np.array(two_dd)
print(type(twodd_list))
print(twodd_list)

print("\n",3*"=","Konversi Array Numpy (List)",3*"=")
np_to_list = array_numpy.tolist()
print(type(np_to_list))
print('1D Array :', np_to_list)
print("2D Arrasy :", twodd_list.tolist())

print("\n",3*"=","Array Numpy dari Tuple",3*"=")
python_tuple = (1,2,3,4,5)
print(type(python_tuple))
print('Tuple : ', python_tuple)

np_array_from_tuple = np.array(python_tuple)
print(type(np_array_from_tuple))
print("Array :",np_array_from_tuple)

print("\n",3*"=","Metode shape Array Numpy",3*"=")
nums = np.array([1,2,3,4])
print(nums)
print('Shape of nums : ', nums.shape)
print(twodd_list)
print('Shape of 2D : ', twodd_list.shape)

data_2d = [[4,5,6,2], [9,6,7,10],[4,7,6,8]]
print(data_2d)
d_2d_array = np.array(data_2d)
print(d_2d_array)
print(d_2d_array.shape)

print("\n",3*"=","Type Data Array Numpy",3*"=")
int_list = [-3,-2,-1,0,1,2,3]
int_array = np.array(int_list)
float_array = np.array(int_array, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)

print("\n",3*"=","Size Array Numpy",3*"=")
data_array = np.array([1,2,3,4,5])
data_2d_array = np.array([[0,1,2],[3,4,5],[6,7,8]])
print('The Size 1D :', data_array.size)
print('The Size 2D : ', data_2d_array.size)

