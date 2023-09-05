
bil_a = 0
print("Awal For")
for i in range(11):
    print(i)
    bil_a += 1

print("Akhir For")
print("\n")

print("Awal While")
bil_c = 0
while bil_c < 11:
    print(bil_c)
    bil_c = bil_c + 1

print("Akhir While")
print("\n")

bil_b = 10
for o in range(10,-1,-1):
    print(o)
    bil_b -= 1


print("\nAwal While")
bil_d = 10
while bil_d >= 0:
    print(bil_d)
    bil_d = bil_d - 1

print('\nMembuat Segitiga')

j_urut = 7
hitung = 1
while True:
    print("*"*hitung)
    hitung += 1

    if hitung > j_urut:
        break

print("\n")
j_urut_a = 7
hitung_a = 1
spasi = int(j_urut_a/2)
while True:
    print(" "*spasi,"*"*hitung_a,"--> Ke-",hitung_a)
    spasi -= 1
    hitung_a += 1

    if hitung_a > j_urut_a:
        break

print("\n")

for persegi in range(8):
    for bawah in range(8):
        print("#", end="")
    print()

print("\n")

for a in range (11):
    kali = a * a
    print(f"{a} * {a} = {kali}")

print("\n")

m_list = ['Python','Numpy','Pandas','Django','Flask']

for unpack in m_list:
    print(unpack)

print('\n')

for i in range(100):
    if i%2 == 0:
        print(i)

print('\n')
for j in range(100):
    if j%2 == 1:
        print(j)

print("\nLevel 2")

total = 0
for k in range (101):
    total += k
    
print("total",total)


print("\n")

total_g = 0
total_gj = 0
for genap in range(101):
    if genap%2 == 0 :
        total_g += genap
for ganjil in range(101):
    if ganjil%2 == 1:
        total_gj += ganjil
print("The Sum Of All Evens is", total_g, "and Total All Odds is ", total_gj)


print('\n')