#exercise
print('Exercise Day 7')
print('Level 1')

it_companies = {'Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'}
print("Set :",it_companies)

print('\n ')
it_companies.add('Twitter')
print("Tambahan : ", it_companies)

print('\n')
t_it = {'Tiktok','Adobe','Line'}
it_companies.update(t_it)
print("Nambah Data :", it_companies)

print('\n')
it_companies.remove('Twitter')
print(it_companies)

print('\n')
print('Perbedaan Remove dan Discard')
print('Remove')
print(it_companies.remove('Facebook'))
print(it_companies.clear())

print('\n')
print('Level 2')
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

join_1 = A.union(B)
print('gabungan dg union',join_1)
print("Intersection : ",A.intersection( B))
print("Subset : ", A.issubset(B))
print("Disjoint : ", A.isdisjoint(B))
print("Join A With B :", A.union(B))
print("Join B With A :", B.union(A))
print("Symetric Difference : ", A.symmetric_difference(B))
del A
del B

print('\n')
print('Level 3')
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(age)
ages = set(age)
print("Konversi Set : ", ages)
print("Panjang List : ", len(age))
print("Panjang Set : ", len(ages))

string = "Anton Febianto"
t_list = ['A','N','T','O','N']
t_tuple = ('A','N','T','O','N')
t_set = {'A','N','T','O','N'}

print(t_list," = ", type(t_list))
print(t_tuple," = ", type(t_tuple))
print(t_set," = ",type(t_set))
print('\n')
kal = 'Saya guru dan saya suka menginspirasi dan mengajar orang'
pecah = kal.split()
print(pecah)
pecahset = set(pecah)
print(pecahset)
print("Unique Word :",len(pecahset))
