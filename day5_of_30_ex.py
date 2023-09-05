#List
lst = list ()
print (len(lst))

empty_list = []
print(len(empty_list))


#list dengan nilai use len()

fruit = ['pisang','Jeruk','mangga','lemon']
vegetables = ['tomat','kentang','Kubis','Bawang Putih', 'Wortel']
animal_products = ['Susu', 'daging','Mentega','Yougurt']
web_techs = ['HTML','JS', 'React', 'Redux', 'Node', 'MongDB']
countries = ['Indonesia','Finlandia','Denmark', 'Swedem']

print('Buah :', fruit)
print("Jumlah Data :",len(fruit))
print('Sayuran :', vegetables)
print('Jumlah Data : ', len(vegetables))
print("Hasil Ternak : ", animal_products)
print('Jumlah Data : ', len(animal_products))
print('Bahasa Program :', web_techs)
print('Jumlah Data :', len(web_techs))
print('Negara :', countries)
print('Jumlah Data :' , len(countries))

#list dengan type data yang berbeda

list_beda = ['Anton', 1997 , True,{'Negara':'Indonesia','Kota' : 'Madiun'}]
print (list_beda[1])

print('_________________________________________')
#Mengakses item/data didalam List menggunakan index positif

data_item = ['Banana', 'Orange', 'Mango', 'Lemon']
buah_1 = data_item[0]
buah_2 = data_item[1]
buah_3 = data_item[2]
buah_4 = data_item[3]
akhir = len(data_item) - 1
print(data_item)
print(buah_1)
print(buah_2)
print(buah_3)
print(buah_4)
print(akhir)
print('_________________________________________')

#Mengakses item/data didalam list menggunakan index negatif
buah_c = data_item[-1]
buah_b = data_item[-2]
buah_a = data_item[-3]
print(buah_c)
print(buah_b)
print(buah_a)
print('_________________________________________')

#Membongkar List

dt_buah = ['Pisang','Mangga','Jeruk','Apel','Melon']
buah_ke1,buah_ke2,buah_ke3, *sisa = dt_buah
print(buah_ke1)
print(buah_ke2)
print(buah_ke3)
print(sisa)

dt_sayur = ['kangkung','Bayam','Tomat','Wortel','kecambah','cabe','Brambang']
sayur_ke1,sayur_ke2,sayur_ke3, *sisasayur = dt_sayur
print(sayur_ke1)
print(sayur_ke2)
print(sayur_ke3)
print(sisasayur)
print('_________________________________________')

s_sayur = dt_sayur[0:]
kang_bay = dt_sayur[0:2]
gini = dt_sayur[::2]
gini2 = dt_sayur[::3]
gini3 = dt_sayur[1:]
print(s_sayur)
print(kang_bay)
print(gini)
print(gini2)
print(gini3)
print('_________________________________________')

#negative index
sm_sayur = dt_sayur[-7:]
reverse = dt_sayur[::-1]

print('_________________________________________')

#Modifikasi List (data didalam list)

brand = ['Samsung','Apple','Redmi','Oppo']
brand[3] = 'Itel'
print(brand)

brand[3] = 'Sonny'
print(brand)

akh_idx = len(brand) - 2
brand[akh_idx] = 'Huawai'
print(brand)

print('_________________________________________')

#Checking List (data didalam list)
#cari = str(input("Cari data :"))
yt_ada = 'Samsung' in brand
print(yt_ada)

print('_________________________________________')

#adding/ menambah data di dalam List
 
motor_brand = ['Honda','Kawasaki','Yamaha','Daihatsu']
motor_brand.append('Toyota')
print(motor_brand)

print('_________________________________________')

#Insert/Memasukan data di dalam List
lptop_brand = ['Asus','Hp','Mac','Axio']
lptop_brand.insert(4, 'Redmi')
print(lptop_brand)

print('_________________________________________')
#Removing/Memasukan data di dalam List
lptop_brand.remove('Hp')
print(lptop_brand)

#remove menggunakan Pop()

lptop_brand.pop()
print("Menggunakan POP() :",lptop_brand)
sv_akh = lptop_brand.pop()
print(sv_akh)

lptop_brand.pop(1)
print(lptop_brand)

#remove menggunakan del
sambel = ['S.Matah','S.Terasi','S.Tomat','S.Embe']
print(sambel)

del sambel[0]
print(sambel)

del sambel[2:1]
print(sambel)

del sambel [1:2]
print(sambel)

sambel.clear()
print(sambel)

print('___________________________')
#Copy data dalam list
copy_sambel = lptop_brand.copy()
print(copy_sambel)

