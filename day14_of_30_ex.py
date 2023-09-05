print("Day 14 - Fungsi Tingkat Tinggi")
print("Function As a Parameter")

def t_nilai(nilai):
    return sum(nilai)

def fungsi_high(n, data):
    summary = n(data)
    return summary

output = fungsi_high(t_nilai, [1,2,3,4,5])
print(output)

print("\nFungsi sebagai Return Value")

def persegi(j):
    return j ** 2

def balok(x):
    return x ** 3

def absolute(o):
    if o >= 0:
        return o
    else:
        return -(o)

def fungsi_high_b(type):
    if type == 'persegi':
        return persegi
    elif type == 'balok':
        return balok
    elif type == 'absolute':
        return absolute

hasil_persegi = fungsi_high_b('persegi')
hasil_balok =  fungsi_high_b('balok')
hasil_abs = fungsi_high_b('absolute')

print(hasil_persegi(5))
print(hasil_balok(6))
print(hasil_abs(-8))

print("\nFungsi di Dalam fungsi")

def tambah_10():
    n_10 = 10
    def p_tambah(angka):
        return angka + n_10
    return p_tambah

f_aktif = tambah_10()
print(f_aktif(5))
print(f_aktif(10))


print("\nCreating Decorator")
#Fungsi normal
def salam():
    return "Hallo Anton"

def uppercase_dec(fungsi):
    def bungkus():
        fungsiku = fungsi()
        p_upper = fungsiku.upper()
        return p_upper
    return bungkus

cb = uppercase_dec(salam)
print(cb())

@uppercase_dec
def salam_a():
    return 'Anton Febianto'

print(salam_a())

print("\nMenerapkan Banyak dekorator ke 1 fungsi")

def upper_deco(fungsi):
    def balutan():
        fungsiku = fungsi()
        r_upper = fungsiku.upper()
        return r_upper
    return balutan

def split_string(fungsi):
    def bungkusan():
        fungsiku = fungsi()
        split_str = fungsiku.split()
        return split_str
    return bungkusan

@split_string
@upper_deco
def ucapan():
    return 'Selamat Belajar'

print(ucapan())

print("\nMenerima Parameter dlm Fungsi Decorator")
def deco_dg_param(fungsi):
    def kapsul_param(param_a,param_b,param_c):
        fungsi(param_a,param_b,param_c)
        print(f"ak tinggal di {param_c}")
    return kapsul_param

@deco_dg_param
def print_fullnm(nm_a,nm_b,negara):
    print('I Am {} {}. i Love to teach.'.format(nm_a,nm_b,negara))

print_fullnm("Anton","Febianto","Indonesia")

print("\nFungsi Urutan Tinggi Bawaan")

angka_a = [1,2,3,4,5]
def persegi_b(c):
    return c ** 2
angka_persegi = map(persegi, angka_a)
print(list(angka_persegi))

angka_persegi_b = map(lambda v:v**2, angka_a)
print(list(angka_persegi_b))

print("\nFungsi Map/Map Function")
#Map Function adalah fungsi yang menggunakan fungsi dan iterasi sbg parameter

iterasi = [1,2,3,4,5]

hasil_persegi = map(persegi, iterasi)
print(list(hasil_persegi))

#pake lambda
h_persegi = map(lambda k : k ** 2, iterasi)
print(list(h_persegi))

angk_str = ['1','2','3','4','5']
angk_int = map(int, angk_str)
print(list(angk_int))

nm_org = ['Anton','Andreas','Kevin','Wiliam']

def ubah_kapital(nama):
    return nama.upper()

pro_ubah = map(ubah_kapital, nm_org)
print(list(pro_ubah))

pro_ubahb = map(lambda c :c.upper(), nm_org)
print(list(pro_ubahb))

print('\nFungsi Filter (Filter Func)')
#fungsi yg memanggil return boolean pada setiap item iterable/daftar

iter_list = [1,2,3,4,5,6]

def bil_gnp(data):
    if data % 2 == 0:
        return True
    return False

pro_genap = filter(bil_gnp, iter_list)
print(list(pro_genap))

dt_nm = ['Anton','Febianto','Jerome','Nicolas','Vincentyous']
def pj_nm(data):
    if len(data) > 6:
        return True
    return False

pro_nm = filter(pj_nm, dt_nm)
print(list(pro_nm))


print('\nReduce Function')
#fungsi seperti filter dan maps tp tdk mengembalikan nilai iterasi
#melainkan nilai tunggal

import functools
dt_str = ['1','2','3','4','5']
def pro_tbh(k,l):
    return int(k) + int(l)

pro_tot = functools.reduce(pro_tbh, dt_str)
print(pro_tot)