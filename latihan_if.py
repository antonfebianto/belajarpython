bilangan = int(input("Masukan Bilangan: "))

if bilangan % 3:
    print(bilangan,"Ada Sisa Hasil Bagi 3")
else:
    print(bilangan, "Habis Dibagi 3")


print('\n')
print('\n')
print("___________________")

nama = str(input("Nama mu : "))
j_kel = str(input("Pria/Wanita ? : "))

if j_kel.lower() in ['pria']:
    print("Hai Bro",nama)
elif j_kel.lower() in ['wanita']:
    print("Hai Sis",nama)
else:
    print('kliru kan')


print('\n')
print('\n')
print("___________________")

#Baby boomer, kelahiran 1944 s.d 1964
#Generasi X, kelahiran 1965 s.d 1979
#Generasi Y (Millenials), kelahiran 1980 s.d 1994
#Generasi Z, kelahiran 1995 s.d 2015

jeneng = str(input("Masukan Nama Anda : "))
th_lahir = int(input("Tahun Berapa Anda Lahir : "))

if th_lahir in [1944,1945,1946,1947,1948,1949,1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,19560,1961,1962,1963,1964]:
    print(jeneng, " Kamu lahir ",th_lahir," Bayi Boomer")
elif th_lahir in [1965,1966,1967,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979]:
    print(jeneng, " Kamu lahir ",th_lahir," Generasi X")
elif th_lahir in [1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994]:
    print(jeneng, " Kamu lahir ",th_lahir," Generasi Y (Millenials)")
elif th_lahir in [1995,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]:
    print(jeneng, " Kamu lahir ",th_lahir," Generasi Z")
else:
    print("Belum ternamai generasi apa")


print('\n')
print("versi Lain")

j_nama = str(input('Masukan Nama Anda : '))
tahun_lhr = int(input("Masukan Tahun Lahir : "))

if tahun_lhr >=1994 and tahun_lhr <=1964:
    print(j_nama," Kamu Lahir di tahun ",tahun_lhr," Generasi Bayi Boomer")
elif th_lahir >=1965 and tahun_lhr <=1979:
    print(j_nama," Kamu Lahir di tahun ",tahun_lhr," Generasi X")
elif th_lahir >=1980 and tahun_lhr <=1994:
    print(j_nama," Kamu Lahir di tahun ",tahun_lhr," Generasi Y (Milenials)")
elif th_lahir >=1995 and tahun_lhr <=2015:
    print(j_nama," Kamu Lahir di tahun ",tahun_lhr," Generasi Z")
else:
    print("Alah mboh")


print('\n')
print('\n')
print('______________________')

bb_bdan = float(input("Berat Badan Anda (Kg): "))
tb_badan = float(input("Tinggi Badan Anda (cm): "))

tb_meter = tb_badan / 100
bmi = bb_bdan/(tb_meter ** 2)

print(bmi)

if bmi > 25:
    print("Gemuk")
elif bmi >= 18.5 and bmi <= 25:
    print("Ideal/langsih dan sehat")
elif bmi < 18.5:
    print("Anda Terlalu Kurus")
else:
    print("tidak teridentifikasi")