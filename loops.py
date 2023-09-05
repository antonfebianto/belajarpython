print("Continue")
ulang_d = 1
while ulang_d < 20:
    if ulang_d == 16:
        ulang_d = ulang_d + 1
        continue
    print(ulang_d)
    ulang_d = ulang_d + 1


print('\n')

bil_bulat = [0,1,2,3,4,5]
for bil_bulat in bil_bulat:
    print(bil_bulat)

print("\n menggunakan String")

kata = "Python"
for nama in kata:
    print(nama)

print('\n')

for i in range(len(kata)):
    print(kata[i])


print('\nDengan tupple')
bil_a = (0,1,2,3,4,5,6)
for bil_a in bil_a:
    print(bil_a)

print("\nDengan Dictionary")

d_org = {
    'nama':'Anton',
    'umur':26,
    'pendidikan':'S-1',
    'negara':'Indonesia',
    'alamat':{
        'village':'Purwosari',
        'zipcode':'63157'
    }
}

for kunci in d_org:
    print(kunci)

print('\n')
for detail, value in d_org.items():
    print(detail," : ", value)

print('\n')
print("Bagian 2")

angka = (0,1,2,3,4,5)
for angka in angka:
    print(angka)
    if angka == 3:
        break

print('\n_____________')
angka_a = (0,1,2,3,4,5)
for angka_a in angka_a:
    print(angka_a)
    if angka_a == 3:
        continue
    print('Angka Berikutnya ', angka_a + 1)if angka_a != 5 else print("Sudah mandek")
print('Diluat perkiraan')

print('\n\n\n')

n_daftar = list(range(12))
print(n_daftar)
print('\n')
n_set = set(range(1, 12))
print(n_set)
print('\n')
n_list = list(range(0, 11, 2))
print(n_list)

print('\n')
for affah in range(11):
    print(affah)

print('\n')
d_manusia = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for id in d_manusia:
    if id == 'skills':
        for skill in d_manusia['skills']:
            print(skill)

print('\n')

for ongko in range(11):
    print(ongko)
else:
    print('Loops at ', ongko)
    pass