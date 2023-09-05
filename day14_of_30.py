print("Exercise Day 14")
print("Soal No 1")
print("""1.Perbedaan Map(), Filter, Reduce()
-> Maps() adalah fungsi yg dimana parameraternya fungsi dan iterable/list
-> filter() adalah fungsi yang di mana nilai kembaliannya ada bolean menggunakan iterable/list
-> reduce() seperti maps dan filter tetapi mengembalikan nilai tunggal
""")

print("""\nNo 2
-> Higher Order Function = fungsi yg dpt melakukan apapun/kasta tertinggi
-> Python Closure = fungsi didalam fungsi yg dapat mengakses lingkup luar dri fungsi
-> Decorator = memungkinkan mengambil fungsi lain
""")

print("\nNo 3")

data = [1,2,3,4,5,6]

def kubik(data):
    return data ** 3

pro_kubik = list(map(kubik, data))
print(pro_kubik)
print("\n")

def bil_ganjil(data):
    if data % 2 == 1:
        return True
    return False

pro_ganjil = list(filter(bil_ganjil, data))
print(pro_ganjil)
print('\n')

import functools
def bagi(z,y):
    return int(z) + int(y)

pro_bagi = functools.reduce(bagi, data)
print(pro_bagi)

print('\nNo 3')

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def det_neg(data):
    for i in data:
        print(i)

print(det_neg(countries))
print("\nNO 5")
nama = ['Anton','Febianto','Ramayana','Arjuna','Indra']
def det_nm(data):
    for i in data:
        print(i)
print(det_nm(nama))


print("\nNo 6")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def det_angk(data):
    for i in data:
        print(i)
print(det_angk(numbers))

print("Exercise Level 2")
print("No 1")

def u_kapital(data):
    return data.upper()

pro_kpt = list(map(u_kapital, countries))
print(pro_kpt)

print("\nNo 2")

def kuadrat(data):
    return data ** 2

pro_kuad = list(map(kuadrat, numbers))
print(pro_kuad)

print("\nNo 3")
def u_kpt_nm(data):
    return data.upper()

pro_kptnm = list(map(u_kpt_nm, nama))
print(pro_kptnm)

print("\nNo 4")

def contain_land(data):
    return 'land' in data

pro_land = list(filter(contain_land, countries))
print(pro_land)

print('\nNo 5')

def lim_karak(data):
    if len(data) >= 6:
        return True
    return False

pro_limkar = list(filter(lim_karak, nama))
print(pro_limkar)

print("\nNo 6")

def lim_neg(data):
    if len(data) >= 6:
        return True
    return False

pro_limneg = list(filter(lim_neg, countries))
print(pro_limneg)

print("\nNo 7")

def start_e(data):
    def p_neg(negara):
        return negara.startswith('E')
    p_filter = list(filter(p_neg, data))
    return p_filter

print(start_e(countries))

print('\nNo 8')
import functools
p_argumen = functools.reduce(lambda c , a : c + a,filter(lambda c : c % 2 == 0, map(lambda c : c * 2,numbers)))
print(p_argumen)

print("\nNo 9")

def get_str_list(data):
    p_str = [k for k in data if isinstance(k, str)]
    return p_str

m_data = [1,'Anton',3.14,'Febi','Elphin',10, 9.1,'Anggi']
print(get_str_list(m_data))

print('\nNo 10')
import functools
proses_hitung = functools.reduce(lambda f,e : f + e, numbers)
print(numbers)
print(proses_hitung)

print('\nNo 11')
from functools import reduce
negara =['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def gabung_negara(n,m):
    return f"{n}, {m}"

gabung_kata = reduce(gabung_negara, negara)
proses_gabung = f"{gabung_kata} negara bagian Eropa Utara"

print(proses_gabung)
import countries

print("\nNo 12")
def ktg_negara():
    detil_fil = ['land','ia','island','stan']
    ktg_neg = {detil: [] for detil in detil_fil}

    for neg in countries.countries:
        for detil in ktg_neg:
            if detil in neg.lower():
                ktg_neg[detil].append(neg)
    return ktg_neg

print(ktg_negara())

print("\nNo 13")
import countries
def p_initial():
    p_negdict ={}
    for i in countries.countries:
        initial_kt = i[0].upper()
        if initial_kt in p_negdict:
            p_negdict[initial_kt]+= 1
        else:
            p_negdict[initial_kt] = 1

    return p_negdict

print(p_initial())

print("\nNo 14")
import countries
def p_topten():
    topten = countries.countries[:10]
    return topten

print(p_topten())

print("\nNo 15")

import countries
def p_reverseten():
    reverseten = countries.countries[-10:]
    return reverseten

print(p_reverseten())
