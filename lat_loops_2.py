for i in range(1,11):
    print(i)

print("\n")
n = 1
while n <=10:
    print(n)
    n += 1

print("\n")
sisi = 5
hitung = 1

for aw in range(1, sisi + 1,1):
    for k in range(1, aw +1):
        print(k, end=" ")
    print(" ")


sisi_a = 5
hitung_b = 0
while True:
    print("+ "* hitung_b)
    hitung_b += 1

    if hitung_b > sisi_a:
        break

print('\n_______________________')

banyak = int(input("masukan Nomor : "))
total_h = 0
for n in range(1, banyak+1):
    total_h += n
print(total_h)

print("\n")

#Nomer 4
for genap in range(1,21):
    if genap%2 == 0:
        print(genap)
