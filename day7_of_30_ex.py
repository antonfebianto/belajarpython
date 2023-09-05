print('day7')
print("""Set adalah kumpulan item yang menggunakan tanda himpunan
 atau kurung kurawal""")

set_data = {}
#or
set_data2 = set()

print("Contoh Set")

buah = {'Pisang','Jeruk','Anggur','Kesemek'}
print(buah)
print("Panjang Set :", len(buah))

print('Mengakses item dalam set')
print("Apakah Ada Jeruk di set ?",'Jeruk' in buah)
print("Apakah Ada Kesemek ?", 'Kesemek' in buah)
print('Apakah Ada Melon ?', 'Melon' in buah)
print('Apakah Ada Mangga ?', 'Mangga' in buah)

print("\n")
print("Menambah Item Ke set")
buah.add('Stowberry')
buah.add('Nanas')
print(buah)

print("\n")
sayur = ('Tomat','Kubis','Sawi','Wortel')
buah.update(sayur)
print(buah)

print("\n")
print('Menghapus Item dari Set')
print('1. Menggunakan remove()')
buah.remove('Pisang')
print(buah)

print('2. Menggunakan pop()')
buah.pop()
show_pop = buah.pop()
print("Hasil data random dihpus :", show_pop)

print('\n')

print("Mengapus dengan clear dan del")
buah.clear()
print("Hasil Dengan Clear() :",buah)
del buah
print("Hasil dengan del : ")
print("_________________________")
print("\n")
print("Konversi List ke Set")

daftar = ['Pisang','Jeruk','Mangga','Semangka']
print("List :",daftar)
daftar = set(daftar)
print("Set :",daftar)

print('\n')
print("Menggabungkan dengan set")
print("Menggunakan Metode Union() dan Update()")

dt1 = daftar.copy()
print(dt1)
dt2 = {'Tomat','Kubis','Pare','Cabe'}
gbg_1 = dt1.union(dt2)
print("Menggunakan Union() :",gbg_1)
print('\n')
dt1.update(dt2)
print("Menggunakan update() :",dt1)

hewan = {'Macan','Kodok','Ular','Singa'}
bunga = {'Mawar',"Melati","Anggrek","Kenanga"}
un_gbg = hewan.union(bunga)
print(un_gbg)

hewan.update(bunga)
print(hewan)
('\n')
print("Menemukan Intersection/Persimpangan :")
#intersection memotong 2 himpunan atau lebih yang memiliki data sama didalam gabungan himpunan

bil_bulat = {0,1,2,3,4,5,6,7,8,9,10}
bil_genap = {0,2,4,6,8,10}
simpang_set = bil_bulat.intersection(bil_genap)
print(simpang_set)

nim1 = {1801,1802,1803,1804}
nim2 = {18005,1804,1802,1806}
nim3 = {1809,1804,1802,1800}
simpangin = nim1.intersection(nim2,nim3)
print(simpangin)

spell_a = {'A','N','T','O','N'}
spell_b = {'F','E','B','I','A','N','T','O'}
cek_simpang = spell_a.intersection(spell_b)
print(cek_simpang)
print('\n')
print('Subset dan Superset')

print(spell_a.issubset(spell_b))
print(nim2.issuperset(nim1))
print(bil_bulat.issuperset(bil_genap))
print(bil_genap.issuperset(bil_bulat))

print('\n')
print("Memeriksa Perbedaan 2 Himpunan")
print(spell_b.difference(spell_a))

print('\n')
print("Menemukan Perbedaan simetris 2 Himpnan")
print(bil_bulat ^ bil_genap)
print(bil_bulat.symmetric_difference(bil_genap))

print('\n')
print(spell_a ^ spell_b)
print(spell_a.symmetric_difference(spell_b))

print('\n')
print('Join Dengan Set Metode isdisjoint()')

print(bil_bulat.isdisjoint(bil_genap))

ang_1 ={2,4,6,8,10,12}
ang_2 = {3,5,7,9,11}
print(ang_1.isdisjoint(ang_2))
