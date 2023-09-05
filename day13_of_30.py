print("Exercise Day 13")
print("Soal No 1")

daftar_angka = [-4,-3,-2,-1,0,2,4,6]
angk_positif = [i for i in daftar_angka if i <= 0]
print(angk_positif)

print('\nNo 2')

daftar_in_daftar = [[1,2,3],[4,5,6],[7,8,9]]
gabung = [i for i in daftar_in_daftar for i in i]
print(gabung)

print('\nNo 3')
angka_a = [(i,1,1 * i, i ** i, i ** i * i,i ** i * i * i  ) for i in range(11) ]
print(angka_a)

print("\nNo 4")
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
r_gabung = [[i[0][0], i[0][0][:3], i[0][1]] for i in countries]
print(r_gabung)

print("\nNo 5")
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
gabung_b = [' '.join(i[0]) for i in names]
print(gabung_b)

print('\n')
fungsi_linier = lambda j, k, l:k * j + l
print(fungsi_linier(0,2,3))