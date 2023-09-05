#Day3_learn python

print("Soal nomor 1")
umur = 26
print('Umur Saya', umur)
print("_____________________")
print("Soal nomor 2")
print("tinggi badan", float(180), "cm")
print("_____________________")
print("Soal nomor 3")

bk1 = 5 + 10j
bk2 = 1j + 1
print(bk1," +", bk2)

hasil = bk1 + bk2
print(hasil)

print("_____________________")
print("Soal nomor 4")

alas = int(input("Alas : "))
tinggi = int(input("tinggi : "))
luassegi3 = 0.5 * alas * tinggi

print("alas :", alas)
print("tinggi :", tinggi)
print("Luas Segitiga =", int(luassegi3))

print("_____________________")
print("Soal nomor 5")
pa = int(input("Panjang : "))
le = int(input("Lebar : "))
ti = int(input("Tinggi :"))
kel= pa + le + ti

print("Panjang : ", pa)
print("Lebar : ", le)
print("Tinggi : ",tinggi)
print("Keliling Balok", kel)

print("_____________________")
print("Soal nomor 6")

panj = 20
lebar = 15
luasppj = panj * lebar
kelppj = 2 * (panj + lebar)

print("Panjang : ", panj)
print("Lebar : ", lebar)
print("Luas Persegi Panjang :", luasppj)
print("Keliling Persegi pnjang :", kelppj)

print("_____________________")
print("Soal nomor 7")

radius = int(input("Jari-jari : "))
phi = 3.14
luasling = phi * radius**2
kelling = 2 * phi * radius
print("jari-jari", radius)
print("Luas Lingkaran : ", luasling)
print("Keliling Lingkaran :", kelling)

print("_____________________")
print("Soal nomor 8")
print(" y = 2x - 2")
print("rumus y = mx + c")
gradient = 2

print("titik Potong")
x = 1
y = -2

print("Gradien :", gradient)
print("Titik x : ", (x, 0))
print("Titik y :", (0, y))

print("_____________________")
print("Soal nomor 9")
import math
x1 = 2
y1 = 2
x2 = 6
y2 = 10
print("koordinat ", (x1, y1) ,(x2, y2))
kemiringan = (y2 - y1) / (x2-x1) #kemiringan
jarak = math.sqrt((x2 -x1)**2) # jarak
print("Kemiringan :", int(kemiringan))
print("Jarak : ", int(jarak))

print("_____________________")
print("Soal nomor 10")

print("Perbandingan soal 8 & 9 memliliki hasil sama : ",gradient == kemiringan)

print("_____________________")
print("Soal nomor 11")
import sympy as sp
x = sp.symbol('x')
persamaan = x**2 + 6*x + 9
x_nil = [-10, 5, 0, 5 ,10]

for x_n in x_nil:
    y_n = persamaan.subs(x, x_n)
    print(f"Untuk x = {x_n}, y= {y_n}")

hasil = sp.hitung(persamaan, x)
print("Nilai X yang membuat Y mjd 0 :")
for hasil1 in hasil:
    print(hasil1)

print("belum isa ngerjain")

print("_____________________")
print("Soal nomor 12")

kata1 = "Python"
kata2 = "Dragon"

huruf1 = len(kata1)
huruf2 = len(kata2)
falsycomp = huruf1 != huruf2
print(kata1, " :" , huruf1)
print(kata2," : ", huruf2)
print("pebandingan palsu : ", falsycomp)

print("_____________________")
print("Soal nomor 13")

print("Python & Dragon", 'on' in 'Pyton and Dragon')

print("_____________________")
print("Soal nomor 14")

print("Jargon in i hope this course is no full of jargon", 'jargon' in 'i hope this course is no full of jargon')

print("_____________________")
print("Soal nomor 15")

print("on is not Dragon and pyton", 'on' not in 'dragon and python')


print("_____________________")
print("Soal nomor 16")

kt1 = "Python"
pj = len(kt1)
print(kt1)
print(float(pj))
print(str(pj))

print("_____________________")
print("Soal nomor 17")

angka = int(input("Masukan Nilai : "))

if angka % 2 == 0:
    print("Angka Genap")
else:
    print("Angka Ganjil")

print("_____________________")
print("Soal nomor 18")

floor = 7 // 3
konv = 2.7
print (floor)
print (str(konv), "&", str(floor), floor == konv )

print("_____________________")
print("Soal nomor 19")

print('10' == 10 )

print("_____________________")
print("Soal nomor 20")

print(int(9.8) == 10)

print("_____________________")
print("Soal nomor 21")

jker = int(input("Masukan Jam kerja :"))
jby =  int(input("Masukan Tarif /h :"))
pdp = jker * jby
print("Pendapan Anda : ", pdp,"$")

print("_____________________")
print("Soal nomor 22")

thn = int(input("Tahun Hidup : "))
hari = 365
detik = 3600
hday = 24
sday = detik * hday
shar = hari * sday
sth = thn * shar

print("Kamu Hidup : ",sth, "detik")
print("_____________________")
print("Soal nomor 23")

for num in range(1, 6):
    n1 = num ** 2
    n2 = num ** 3
    n3 = num ** 4
    print(f"{num} 1 {n1} {n2} {n3}")
