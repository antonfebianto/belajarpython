import numpy as np
print(3*"=","Operasi Matematika",3*"=")

data_numpy = [1,2,3,4,5]
r_numpy = np.array(data_numpy)
print('Ori Array :',r_numpy)
print("Tambah")
p_add = r_numpy + 10
print(p_add)

print("\nPengurangan")
p_kurang =  r_numpy - 10
print(p_kurang)

print("\nPerkalian")
p_kali = r_numpy * 10
print(p_kali)

print('\nPembagian')
p_bagi = r_numpy / 10
print(p_bagi)

print('\nModulus')
p_modulus = r_numpy & 3
print(p_modulus)

print("\nFloor Dev")
p_floor = r_numpy // 10
print(p_floor)

print('\nPangkat')
p_pangkat = r_numpy ** 2
print(p_pangkat)

print(3*"=","Memerika Type Data",3*"=")
data_int = [1,2,3,4,5]
data_float = [2.3,2.1,5.4,3.1]
data_bool = [-3,-2,0,1,2,3]

r_int = np.array(data_int)
r_float = np.array(data_float)
r_bool = np.array(data_bool, dtype='bool')
print(r_int)
print(r_int.dtype)
print(r_float)
print(r_float.dtype)
print(r_bool)
print(r_bool.dtype)

print(3*"=","Jenis konversi/Casting",3*"=")
print('integer to float')

d_int_float = np.array(data_int, dtype='float')
print(d_int_float)

d_float_int = np.array(data_float, dtype='int')
print(d_float_int)

d_int_bool = np.array(data_bool, dtype='bool')
print(d_int_bool)

d_int_str = np.array(data_int, dtype='<U21')
print(d_int_str)

print(3*"=","Array Multidimensi",3*"=")

matrik_2d = np.array([(1,2,3),(4,5,6),(7,8,9)])
print(type(matrik_2d))
print(matrik_2d)
print('Shape :', matrik_2d.shape)
print('Size :', matrik_2d.size)
print('Data Type:', matrik_2d.dtype)

print(3*"=","Getting Item From Numpy",3*"=")

print('Pisah Perbaris')
baris_1 = matrik_2d[0]
baris_2 = matrik_2d[1]
baris_3 = matrik_2d[2]
print('Baris Ke-1 :', baris_1)
print('Baris Ke-2 :', baris_2)
print('Baris Ke-3 :',baris_3)

print('\nPisah Perkolom/ transpose Baris jadi kolom')

kolom_1 = matrik_2d[:,0]
kolom_2 = matrik_2d[:,1]
kolom_3 = matrik_2d[:,2]
print('Kolom ke 1 :', kolom_1)
print('Kolom ke 2 :', kolom_2)
print('Kolom ke 3 :', kolom_3)

print(3*"=","Slicing Array Numpy/Mengiris",3*"=")
# aturan penulisan [baris, kolom]
baris_kol_1_2 = matrik_2d[0:2, 0:2]
print(baris_kol_1_2)

print("\nmatrix 2D")
print(matrik_2d[::])
print('matrix Terbalik/Reverse')
print(matrik_2d[::-1,::-1])


matrik_2d[0,0] = 55
matrik_2d[1,1] = 44
matrik_2d[2,2] = 45
print(matrik_2d)

print("\n")
matrik_nol = np.zeros((3,3), dtype=int, order='C')
print(matrik_nol)

print("\n",3*"=","Matrik 1",3*"=")
matrik_satu = np.ones((3,3), dtype=int, order='C')
print(matrik_satu)
print("\nKali 2")
kali_2 = matrik_satu * 2
print(kali_2)

print("\n",3*"=","Reshape",3*"=")
shape_1 = np.array([(1,2,3), (4,5,6)])
print(shape_1)
re_shape_1 = shape_1.reshape(3,2)
print(re_shape_1)

print("\n",3*"=","Flatten",3*"=")
flat_1 = re_shape_1.flatten()
print(flat_1)

print("\n",3*"=","Horisontal/Vertikal Stack",3*"=")
np_arr_a = np.array([1,2,3])
np_arr_b = np.array([4,5,6])
print(np_arr_a + np_arr_b)

print("Horizontal Append:", np.hstack((np_arr_a , np_arr_b)))
print("Vertikal Append:", np.vstack((np_arr_a, np_arr_b)))

print("\n",3*"=","Random Number",3*"=")

random_float = np.random.random()
print(random_float)
print("\n")

random_floats = np.random.random(5)
print(random_floats)

print("\n",3*"-","Range Acak",3*"-")
random_int = np.random.randint(0,5) #range ->> (start, end)
print(random_int)

random_int_a = np.random.randint(2,10, size=(2,2))
print(random_int_a)

print("\n",3*"-","Matrik Range Acak",3*"-")

normal_array = np.random.normal(80,15,30)
print(normal_array)