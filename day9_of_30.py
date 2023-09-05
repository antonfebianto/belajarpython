print('Exercise Days 9')

usia = int(input("Masukan usia anda :"))
kurang = 18 - usia
if usia >= 18:
    print("Anda Sudah Cukup umur untuk mengemudi")
elif usia < 18:
    print('Tidak cukup umur ya nak, tunggu', kurang ," tahun lgi")


print('\n')
print('_____________________')
umurmu = int(input('Masukan Umurmu :'))
umurku = 26
gap_1 = umurmu - umurku
gap_2 = umurku - umurmu
if umurmu > umurku:
    print('Umurmu lebih tua dari mu :',gap_1, "tahun")
elif umurku > umurmu:
    print('Umurku lebih tua dari mu',gap_2,' tahun')
elif umurku == umurmu:
    print('Seumuran')
else:
    print('yang bener aje')

print('\n')
print('______________________')

nilai1 = int(input("Nilai-1 :"))
nilai2 = int(input('Nilai 2 :'))

if nilai1 > nilai2:
    print(nilai1,"Lebih Besar Dari ", nilai2)
elif nilai1 < nilai2:
    print(nilai1,"Lebih kecil dari ", nilai2)
else:
    print("Sama Dengan")


print('\n')
print('Exercise level 2')

n_mhs = int(input("Masukan Nilai : "))

if n_mhs >= 90 and n_mhs <= 100:
    print('Grade A')
elif n_mhs <=89 and n_mhs >=70:
    print('Grade B')
elif n_mhs <=69 and n_mhs >=60:
    print("Grade C")
elif n_mhs <=59 and n_mhs >=50:
    print("Grade D")
else:
    print('Grade F')

print('\n')
print('________________________')

bulan = str(input('Masukan Bulan :'))
if bulan.lower() in ['desember','januari','februari']:
    print('Musim Gugur')
elif bulan.lower() in ['september','oktober','november']:
    print('Muasim Gugur')
elif bulan.lower() in ['maret','april','mei']:
    print('Musim Semi')
elif bulan.lower() in ['juni','juli','agustus']:
    print('Musim Panas')
else :
    print('Kliru too hmm!!')

print('\n')
print('________________________')

masuk = str(input("Masukan buah : "))
buah = ['banana','orange','mango','lemon']

if masuk.lower() in buah:
    print(masuk, 'Sudah Ada di ')
else:
    print("Oke Data berhasil Ditambah")
    buah.append(masuk)
    print(buah)


 


