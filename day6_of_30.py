##Excercise 
print('Level 1')
print("Soal No 1")

empty_tuple = ()

sister = ('Parvati','Laksmi','Saraswati','Sinta')
brother = ('Mahadewa','Wisnu','Brahma','Krisna')

print('Sister :', sister)
print('Brother :', brother)

kandung = sister + brother
print('Saudara Kandung :', kandung)

j_saudara = len(kandung)
print('Jumlah Saudara : ', j_saudara)

father = 'Yesus'
mother = 'Maria'

f_members = kandung + (father, mother)
print(f_members)

sdr1,sdr2,sdr3,sdr4,sdr5,sdr6,sdr7,sdr8, *ortu = f_members

print(f_members[:8])
print("Unpacking Ortu :",ortu)

print('\n')
print("__________________________")

buah = ('Jambu','Juwet','Ciplukan','Rambusa')
sayur = ('Lobak','Cabe','Wortel','Tomat')
kewan = ('Kucing','Asu','Jaran','Walang')

food_stuff_tp = buah + sayur + kewan
print(food_stuff_tp)

print('\n')
print("__________________________")
food_stuff_tp = list(food_stuff_tp)
print(food_stuff_tp)

print('\n')
print("__________________________")
print(food_stuff_tp[1:6])
print(food_stuff_tp[3:9])

del food_stuff_tp


print('\n')
print("__________________________")
nordic_countries = ('Denmark','Finland','Iceland','Norway','Sweden')

cek1 = 'Estonia' in nordic_countries
cek2 = 'Iceland' in nordic_countries

print("Yt Estonia : ",cek1)
print("Yt Iceland : ",cek2)

for i in range(len(buah)):
    print(buah[i])
