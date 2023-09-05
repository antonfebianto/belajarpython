#Day2 : 30 Days of python programming

first_name = 'Anton'
last_name = 'Febianto'
full_name  = 'Anton Febianto'
country = 'Indonesia'
city    = 'Madiun'
age = 26
year = 1997
is_married = False
is_true = False
is_light_on = True
sd, smp, smk = 'Purwo1', 'mtscrb','smkpink'

print(first_name)
print(last_name)
print(full_name)
print(country)
print(city)
print(age)
print(year)
print(is_married)
print(is_true)
print(is_light_on)
print(sd, smp, smk)

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))


print('______________________')
print(first_name, len(first_name))
print(first_name, "Jlm karakter :", len(first_name))
print(last_name, "Jlm karakter :", len(last_name))

#Soal nomor 4

num_one = 5
num_two = 4

total = (num_one + num_two)
diff = (num_two - num_one)
product = (num_two * num_one)
division = (num_one / num_two)
remainder = (num_two % num_one)
exp = (num_one ** num_two)
floor_division = (num_one // num_two)

print(num_one," + ", num_two,' = ', total)
print(num_two,"-", num_one,' = ', diff)
print(num_two,' x ', num_one,' = ', product)
print(num_one,'/', num_two,' = ', division)
print(num_two, 'Mod', num_one,' = ', remainder)
print(num_one,'Pangkat',  num_two,' = ', exp)
print(num_one, '//', num_two,' = ', floor_division)

#Lingkaran
r = 30
phi = 3.14

#Luas lingkaran
area_of_circle = phi * r * r
circum_of_circle = phi * r * 2

print('Luas Lingkaran =', area_of_circle)
print('Keliling Lingkaran =', circum_of_circle)

jari = int(input('Jari-Jari ='))

l_ling = phi * jari * jari
kel_ling = phi * jari * 2

print('L.Lingkarang = ', l_ling)
print('Kel.Lingkaran = ', kel_ling)

print("__________________________________")
#Nomer 6
nm_1 = input('First Name = ')
nm_2 = input('Last Name = ')
negara = input('Country = ')
age = input('Age = ')

print(nm_1)
print(nm_2)
print(negara)
print(age)

help('keywords')
