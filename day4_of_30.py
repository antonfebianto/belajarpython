#exercise
#day4 of python

print("Soal Nomor 1")
kt1 = 'Tiga Puluh'
kt2 = 'Hari'
kt3 = 'Python'
gabung = kt1 + " " + kt2 + " " + kt3
print(gabung)

print("________________")
print("Soal Nomor 2")

kt_a = 'Coding'
kt_b = 'For'
kt_c = 'All'
gabungan = kt_a + " " + kt_b+ " " + kt_c
print(gabungan)

print("________________")
print("Soal Nomor 3,4,5,6,7,8")

company = "Coding For All"
print(company)
print("jml karakter:", len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

print("________________")
print("Soal Nomor 9")

potong = company[0:7]
print(potong)

print("________________")
print("Soal Nomor 10")
print(company.find('Coding'))
print(company.index('Coding'))
print(company.rfind('Coding'))
print(company.rindex('Coding'))

print("________________")
print("Soal Nomor 11")
print(company.replace("Coding","Python"))

print("________________")
print("Soal Nomor 12")
nw_kt = "Python For Everyone"
print(nw_kt.replace("Everyone","All"))

print("________________")
print("Soal Nomor 13")
print(company.split())

print("________________")
print("Soal Nomor 14")
merk = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(merk.split())

print("________________")
print("Soal Nomor 15")
print(company[0])

print("________________")
print("Soal Nomor 16")
print(company.index('l')+ 1)

print("________________")
print("Soal Nomor 17")
print(company[10])

print("________________")
print("Soal Nomor 18")
word1 = "Python For Everyone"
print(word1[0:18:7])

print("________________")
print("Soal Nomor 19")
word2 = "Coding For All"
print(word2[0:13:3])

print("________________")
print("Soal Nomor 20")
print(word2.index('C'))

print("________________")
print("Soal Nomor 21")
print(company.index('F'))

print("________________")
print("Soal Nomor 22")
word3 ="Coding For All People"
print(word3.rfind('l'))

print("________________")
print("Soal Nomor 23")
paraf1= "You cannot end a sentence with because because because is a conjunction"

print(paraf1.find('because'))
print(paraf1.index('because'))

print("________________")
print("Soal Nomor 24")
print(paraf1.rindex('because'))

print("________________")
print("Soal Nomor 25")
word3= "You cannot end a sentence with because because because is a conjunction"
print(word3.replace("because because because", "because"))

print("________________")
print("Soal Nomor 26")
print(word3.index('because'))

print("________________")
print("Soal Nomor 27")
word4 = "You cannot end a sentence with because because because is a conjunction"
print(word4.replace("because because because", "because"))

print("________________")
print("Soal Nomor 28")
print(word2.startswith('Coding'))
print("________________")
print("Soal Nomor 29")
print(word2.endswith('Coding'))

print("________________")
print("Soal Nomor 30")
word5 = " Coding For All "
print(word5)
print(word5.strip(' '))

print("________________")
print("Soal Nomor 31")
print("30 DaysPython".isidentifier())
print("tiga puluh hari_dari_python".isidentifier())

print("________________")
print("Soal Nomor 31")
py_lib = ['Django','Flask', 'Bottle','Pyramid','Falcon']
print(' # '.join(py_lib))

print("________________")
print("Soal Nomor 32")
print("I am enjoying this challenge \nI just wonder what is next")

print("________________")
print("Soal Nomor 33")
print("Name\tAge\tCountry\tCity")
print("Anton\t100\tIndonesia\tMadiun")

print("________________")
print("Soal Nomor 35")
jari2 = 10
luas = 3.14 * jari2 ** 2
keluaran = "The are of a circle radiun {} is {}".format(jari2,luas)
keluaran2 = "The are of a circle radiun %d is %d" %(jari2,luas)
print(keluaran)
print(keluaran2)

print("________________")
print("Soal Nomor 36")
ongk1 = 8
ongk2 = 6
print("{} + {} = {}".format(ongk1, ongk2, ongk1 + ongk2))
print("{} - {} = {}".format(ongk1, ongk2, ongk1 - ongk2))
print("{} * {} = {}".format(ongk1, ongk2, ongk1 * ongk2))
print("{} / {} = {}".format(ongk1, ongk2, ongk1 / ongk2))
print("{} Mod {} = {}".format(ongk1, ongk2, ongk1 % ongk2))
print("{} // {} = {}".format(ongk1, ongk2, ongk1 // ongk2))
print("{} ^ {} = {}".format(ongk1, ongk2, ongk1 ** ongk2))