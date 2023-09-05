print("Day 13 List Comprehension")

bahasa = 'Python'
daftar = list(bahasa)
print(bahasa)
print(daftar)

daftar_b = [i for i in bahasa]
print(daftar_b)
print('\n')

number_a = [i for i in range(11)]
number_b = [i*i for i in range(11)]
number_c = [(i, i * i) for i in range(11)]

print(number_a)
print(number_b)
print(number_c)

print('\nMenggunakan conditional')

bil_genap = [i for i in range(21) if i % 2 == 0]
bil_ganjil = [i for i in range(21) if i % 2 == 1]
print(bil_genap)
print(bil_ganjil)

angka = [-8,-7,-3,-1,0,1,2,4,5,7,6,8,10]
bil_postf = [i for i in angka if i % 2 == 0  and i > 0]
print(bil_postf)

list_of_list = [[1,2,3],[4,5,6],[7,8,9]]
bil_gabung = [i for i in list_of_list for i in i]
print(bil_gabung)

print('\nMembuat Fungsi Lambda')

def tambah(a,b):
    hasil = a+b
    return hasil

print(tambah(2,2))

tambah_2 = lambda a, b: a + b
print(tambah_2(4,4))

kuadrat = lambda x:x**2
print(kuadrat(3))

kubik = lambda z:z**3
print(kubik(4))

var_campuran = lambda k,l,m: k ** 2 - 3 * l + 4 * m
print(var_campuran(5,5,3))

print("\nFungsi Lambda dalam func lain")

def kuat (x):
    return lambda n : x ** n

kubus = kuat(2)(2)
print(kubus)
