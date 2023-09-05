
print("While segitiga ganjil")
sisi = int(input("Masukan Jumlah : "))
count = 1
print("Menjadi Segitiga Genap")
while True:
    if count%2 == 1:
        count += 1
        continue

    print("*"*count ," -->",count)
    count += 1

    if count > sisi:
        break
print("mandek")


print("\n")
sisi_a = int(input("Masukan Jumlah :"))
count_a = 1
print("Menjadi Segitiga Ganjil")
while True:
    if count_a%2 == 0:
        count_a += 1
        continue

    print("*" * count_a, " -->", count_a)
    count_a += 1

    if count_a > sisi_a:
        break
print("Sudah!")


print("\n")
print("Menjadi Segitiga samasisi")

sisi_b = int(input("Masukan Jumlah :"))
count_b = 1
jarak = int(sisi_b/2)

while True:
    if (count_b%2):
        print(" "*jarak,"+"*count_b," --> Ke-", count_b)
        jarak -= 1
        count_b += 1
    else:
        count_b += 1
        continue
    if count_b > sisi_b:
        break
while True:
    if (count_b%2):
        print(" "*jarak,"+"*count_b, " --> Ke-", count_b)
        jarak += 1
        count_b -= 1
    else:
        count_b -= 1
        continue
    if count_b == 0:
        break
print("wes bar")