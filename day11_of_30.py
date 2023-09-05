print('Exercise day 11 (Function)')
print("No 1 \nPenjumlahan")
def add_two_numbers(n1,n2):
    summary = n1 + n2
    return summary
print("Penjumalah :",add_two_numbers(2,3))

print("\nNo 2 \nLuas Lingkaran")

def l_lingkaran(jari):
    phi = 3.14
    luas_ling = str(phi *jari**2) + ' cm'
    return luas_ling
print(l_lingkaran(7))

print("\nNo 3")
def add_all_nums(*n_uptou):
    hitung = 0
    for tmbah in n_uptou:
        hitung += tmbah
    return hitung
print(add_all_nums(3,2,3))

print('\nNo 4')
def konv_fahrenheit(celcius):
    derajat = 32
    fahrenheit = str((celcius*9/5)+ derajat) +" F"
    return fahrenheit
print(konv_fahrenheit(10))

print("\nNo 5 Musim")

def musim(bulan):
    if bulan.lower() in ['semptember','oktober','november']:
        print("Musim Gugur")
    elif bulan.lower() in ['desember','januari','februari']:
        print("Musim Dingin")
    elif bulan.lower() in ['maret','april','mei']:
        print("Musim Semi")
    elif bulan.lower() in ["juni",'juli','agustus']:
        print("Musim Panas")
    else:
        print("bulan Salah")

print(musim('Januari'))

print("\nNo 6 \nMenghitung Kemiringan Persamaan Linier")

def h_miring(y1,x1,y2,x2):
    miring =(y2 - y1)/(x2 - x1)
    return miring
print(h_miring(5,3,1,2))

print("\nNo 7 ")
import math
def pers_kuadrat(a,b,c):
    discrim = b**2 - 4*a*c

    if discrim > 0:
        x1 = (-b + math.sqrt(discrim))/2*a
        x2 = (-b - math.sqrt(discrim))/2*a
        return x1,x2
    elif discrim == 0:
        x3 = -b / (2*a)
        return (x3)
    else:
        return()

def solusi():
    h_kuadrat = pers_kuadrat(10,12,-11)
    if h_kuadrat:
        print("Himpunan Solusi:", h_kuadrat)
    else:
        print("Bukan Himpunan")

print(solusi())

print('\nNo 8')

def print_list(*daftar):
    for hm in daftar:
        print(hm)

print(print_list('Anton','Febianto',"Singo","Boyo"))


def reversal_a(*list_a):
    mundur = []
    for undur in range(len(list_a)-1,-1,-1):
        mundur.append(list_a[undur])
    print(mundur)

print(reversal_a(1,2,3,4,5))
print(reversal_a("A","B","C","D"))

print('\nNo 9')
def capitalize_list_items(*d_data):
    data_transit = list()
    for isian in d_data:
        data_transit.append(isian.capitalize())
    return data_transit


m_data = ['e-budgeting','si-mamat','divisi-ex','e-bk','mtr-cc']
print(capitalize_list_items('e-budgeting','si-mamat','divisi-ex','e-bk','mtr-cc'))

print('\nNo 11')

def add_item(daftar,tambah):
    daftar.append(tambah)
    return daftar

food_staff= ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff,'Meat'))
print('\n')

def add_item_angk(daftar_a,tambah_a):
    daftar_a.append(tambah_a)
    return daftar_a
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))

print("\nNo 12")

def hapus (daftar, buang):
    daftar.remove(buang)
    return daftar
food_staff= ['Potato', 'Tomato', 'Mango', 'Milk']
print(hapus(food_staff,'Mango'))
print('\n')

def hapus_a(daftar_a,buang_a):
    daftar_a.remove(buang_a)
    return daftar_a
numbers = [2, 3, 7, 9]
print(hapus_a(numbers, 3))

print('\nNo 13')

def jumlah_a(angka):
    total = 0
    for i in range(angka+1):
        total += i
    return total
print(jumlah_a(5))

def jumlah_b(angka):
    total = 0
    for i in range (angka+1):
        total += i
    return total
print(jumlah_b(10))

def jumlah_c(angka):
    total = 0
    for i in range(angka+1):
        total += i
    return total
print(jumlah_c(100))
print('\nNo 14 & 15')

def genap(rentang):
    t_genap = 0
    for i in range(rentang+1):
        if i %2 == 0:
            t_genap += i
    return t_genap

print('ini data genap :',genap(100))

def ganjil(rentang):
    t_ganjil = 0
    for i in range(rentang+1):
        if i % 2 == 1:
            t_ganjil += i
    return t_ganjil
print("ini data ganjul :", ganjil(100))


print('\nLevel 2')
print('No 1')
def ganjilgenap(rentang):
    h_ganjil = 0
    h_genap = 0
    #rentang_str = str(rentang)
    for i in range(rentang+1):
        if i % 2 == 0:
            h_genap += 1    
        else:
            h_ganjil += 1
    print("Angka Genap Jumlah", h_genap)
    print("Angka Ganjil Jumlah :",h_ganjil)
print(ganjilgenap(100))

print('\n No 1')

def faktorial (angka):
    pengx = 1
    for i in range(1, angka+1):
        pengx *= i
    return pengx
n = int(input("input angka : "))
print("Bilangan Faktorial dari",n ,"! :", faktorial(n))
print('\n')

def is_empty (daftar, data):
    ytoke = data in daftar
    return ytoke
buah = ['Mangga','Melon','Anggur','Semangka']
print(is_empty(buah,'Mangga'))

print('\n')

def statistik(daftar):
    median_idx= int(len(daftar)/2)
    median = daftar[median_idx]
    print ("Nilai Tengah:", median)

    avg_idx = int(len(daftar))
    sum_avg = sum(daftar)
    avg = sum_avg/avg_idx
    print("Rerata :", avg)

    n_max = max(daftar)
    n_min = min(daftar)
    rentang = n_max - n_min
    print("Rentang :" , rentang)

    std_dev_idx = int(len(daftar))
    n_x = sum_avg / std_dev_idx
    return()

data = [19,29,21,22,20]
print(statistik(data))

print("\n")

def hitung_statistik(daftar):
    h_mean = sum(daftar)/len(daftar)

    h_urut = sorted(daftar)
    h_pjg = len(h_urut)
    h_tgh = h_pjg //2

    if h_pjg & 2 == 0:
        h_median = (h_urut[h_tgh - 1] + h_urut[h_tgh])/2
    else:
        h_median = h_urut[h_tgh]

    h_freq = {}
    for angka in daftar:
        h_freq[angka] = h_freq.get(angka,0)+1

    h_modus = []
    max_freq = max(h_freq.values())

    for angka, freq in h_freq.items():
        if freq == max_freq:
            h_modus.append(angka)
    
    h_range = max(daftar) - min(daftar)
    h_akar_kuadrat = [(x - h_mean) **2 for x in daftar]
    h_var = sum(h_akar_kuadrat) / len(daftar)
    h_std = h_var ** 0.5

    print("Nilai Rata-Rata :",h_mean)
    print("Nilai Tengah : ",h_median)
    print("Modus : ",max_freq)
    print("Nilai Range :",h_range)
    print("Nilai variance :",h_var)
    print("Standart Deviasi :",h_std)


deret = [19,29,21,22,20]
print(hitung_statistik(deret))

print("\nLevel 3")
print("\nNo 1")

def bil_prima(data):
    if data < 2:
        return False
    
    for i in range(2, int(data**0.5)+1):
        if data % i == 0:
            return False
    return True

print(bil_prima(4))

print('\nNo 2')

def data_unik(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False

print("YT ada data Unik :",data_unik([1,3,5,7,7,8]))
print("YT ada data unik :",data_unik(['Mangga','Apel','Semangga']))

print('\nNo 3')
def redudancy(daftar):
    if len(daftar) == 0:
        return True
    
    tipe_data = type(daftar[0])

    for i in daftar:
        if type(i) != tipe_data:
            return False
    return True

print("YT Ada sama :",redudancy([1,2,'head']))
print("YT Ada sama :",redudancy([1,2,3]))

print('\nNo 4')
def p_variable(data):
    if data.isidentifier():
        return True
    else:
        return False

print(p_variable('haucek5'))
print(p_variable('1111'))
print('\nNo 5')