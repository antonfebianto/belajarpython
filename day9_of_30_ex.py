print('Days 9')
print('Conditionals')

a = 3
if a > 0:
    print(a,'Benar dan Positif Number')

b = 3
if b > 7:
    print('Benar')
else:
    print('Salah')


print('\n')
print("______________________")

even = 10
if even/2:
    print('Ganjil')
elif even/5:
    print('Genap')
else:
    print('takde')

c = -2
if c > 0:
    print('A is a positive number')
elif c < 0:
    print('A is a negative number')
else:
    print('A is zero')


print('\n')
print("______________________")
print('Menggunakan operator logika AND')

n1 = 0
if n1 > 0 and n1 % 2 == 0:
    print('N1 adalah bil.Genap dan Positif')
elif n1 > 0 and n1 % 2 != 0:
    print("N1 adalah bill.ganjil dan Posifif")
elif n1 == 0:
    print('N1 adalah Nol')
else:
    print('Bilangan Negatif')

print('\n')
print("______________________")
print('Menggunakan operator logika OR')
user = 'komisaris'
access_level = 1
if user =='head' or access_level >=3:
    print('Access Berhasil')
else:
    print("Access ditolak")
    