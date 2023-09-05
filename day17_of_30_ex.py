print("day 17 - Exception Handling")

try:
    print(10 + '5')
except:
    print("Data yang anda input Salah !!")

print("\n")

try:
    name = input("Input Nama:")
    year_born = int(input("Tahun Lahir :"))
    age = 2023 - year_born
    print(f"Namamu {name} dan umurmu {age}")
except TypeError:
    print('Type Data Error')
except ValueError:
    print('Value error')
except ZeroDivisionError:
    print('Zero Div Error')

print("\n")
try:
    nama_a = input("Masukan nama :")
    t_lahir = input("Tahun Lahir :")
    umur = 2023 - int(t_lahir)
    print(f"Namamu {nama_a} Umurmu {umur}")
except TypeError:
    print("Type Data Salah !")
except ValueError:
    print("Inputan Salah !")
except ZeroDivisionError:
    print("Pembagian Nol Tidak Bisa !")
else:
    print('Biasakan Menggunakan Blok Try')
finally:
    print('Selalu Dijalankan')

print('\n')
try:
    nama_b = input('Nama Anda :')
    t_lhr_b = input('Tahun Lahir :')
    umur_b = 2023 - int(t_lhr_b)
    print(f"Nama anda {nama_b} Umurmu {umur_b}")
except Exception as e:
    print(e)

print("\n")

def det_list(a,b,c,d,e):
    return a + b + c + d + e

print(det_list(1,2,3,4,5))
data = [4,5,6,7,8]
print(det_list(*data))
print("\n")

angka = range(2,7)
print(list(angka))

masukan = [4, 10]
deret = range(*masukan)
print(list(deret))
print("\n")

negara = ['Indonesia','Thailand','Singapore','Cambodia','Laos']
a, b , c, *x = negara
print(a, b, c, x )

print("\n")
#unpacing dictionaries

def unpack_kamus (nama, neg, kota, umur):
    return f"{nama} tinggal di {neg} pada kota {kota} berumur {umur} tahun"
data_dict ={
    'nama':'Anton',
    'neg':'Indonesia',
    'kota':'Madiun',
    'umur':26
    }
print(unpack_kamus(**data_dict))
print("\n")
#packing List

def total_angka(*data):
    t = 0
    for i in data:
        t += i
    return t

print(total_angka(5,6,7,8))

print("\n")
#Packing dictionaries
def kemas_info (**data):
    for key in data:
        print (f"{key} = {data[key]}")
    return data

print(kemas_info(nama='Anton', negara='Indonesia', kota='Madiun'))

print("\n")
#spreading in python

data_a = [1,2,3]
data_b = [4,5,6,7]
g_data = [0, *data_a, *data_b]
print(g_data)

print("\n")
neg_a = ['Indonesia','Singapore','Philipine']
neg_b = ['Brunei','Malaysia']
asian_countries = [*neg_a, *neg_b]
print(asian_countries)

neg_c = ['Indonesia']
for index, i in enumerate(neg_c):
    print('hi')
    if i == 'indonesia':
        print(f"the country {i} has been found at index")

print('\nZIP')

buah =['pisang','orange','mangga','jeruk']
sayur=['tomat','wortel','bayam','cipir','kubis']
buah_sayur =[]
for c,d in zip(buah, sayur):
    buah_sayur.append({'buah':c,'sayur':d})

print(buah_sayur)

print('\nExercise Day 17')
negari = ['Finland','Sweden','Norway','Denmark','Iceland','Estonia','Russia']
*nordic, es,ru = negari
print('Nordic :',nordic)
print('Es :', es)
print('RU:', ru)