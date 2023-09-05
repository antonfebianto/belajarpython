
#day6_of_30 
#tuples / tupel
###perbedaan tuples/tupel dengan list adalah tandan kurung,
## List menggunakan [], dengankan tuples menggunakan ()
## list dapat diubah,dihapus,dan di tambah
## tuples/tuple tidak dapat melakukan crud

empty_tuple = ('Anton','Febianto','S.Kom')
print(empty_tuple)
print(len(empty_tuple))

buah = ('Pisang','Apel','Pear','Persik')
buah_1 = buah[0]
buah_2 = buah[1]
buah_3 = buah[2]
print(buah_1)
print(buah_2)
print(buah_3)

print(buah[:3])
print(buah[1:3])
print(buah[0:2])

buah = list(buah)
print(buah)

