#type data string
print("Type Data String")

huruf = 'A'
print(huruf)
print(len(huruf))

salam = 'Hallo, Aku Anton'
print(salam)
print(len(salam))

kalimat = "Saya Anton Febianto Belajar Python"
print(kalimat)
print(len(kalimat))

print("==Multiline===")
paragraf = """Anton Febianto adalah seorang lulusan Strata-1 Universitas PGRI Madiun,
dan bekerja di PT.Berlian Jaya Perkasa"""
print(paragraf)

print("Type Huruf")
print("Anton Febianto, \n and u ?")
print("Day 1\t3\t5")
print("Day 2\t3\t5")
print("Huruf dengan kutipan atau tanda petik")
print('\"Anton Febianto\"')


print("Format string gaya lama % operator")
nm_awal = 'Anton'
nm_blk = 'Febianto'
bahasa = 'Indonesia'
format_slama = 'namaku %s %s, dan berbahasa %s' %(nm_awal, nm_blk, bahasa)
print(format_slama)

#matematika
jari = 10
phi = 3.14
luas = phi * jari ** 2
format_aslama = "Luas Lingakaran dengan %d adalah %.2f" %(jari, luas)
print(format_aslama)


python_lib = ['Django','Numpy', 'Pandas', 'Sympy', 'Matplotlib']
format_sslama = "Ada beberapa library pada python: %s" %(python_lib)
print(format_sslama)

print("format string gaya baru str.format")

format_snew = "Namaku {} {}, dan berbahasa {}".format(nm_awal, nm_blk, bahasa)
print(format_snew)

ang1 = 4
ang2 = 3

print("{} + {} = {}".format(ang1,ang2, ang1 + ang2))
print("{} x {} = {}".format(ang1, ang2, ang1 * ang2))
print("{} / {} = {}".format(ang1, ang2, ang1 / ang2))

format_lnew = "Luas lingkaran dgn jari {} adlah {}".format(jari,luas)
print(format_lnew)

prog = "python"
a,b,c,d,e,f = prog
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

kata_1 = prog[0]
print(kata_1)

kata_2 = prog[1]
print(kata_2)

akhir_index = len(prog) - 1
h_akh = prog[akhir_index]
print(h_akh)

kata_1a = prog[-1]
kata_2a = prog[-2]
print(kata_1a)
print(kata_2a)

kata_n1 = prog[0:3]
print(kata_n1)
kata_n2 = prog[1:4]
print(kata_n2)

print(prog[::-1])
abbr = prog[0:6:2]
print(abbr)


n_kalimat = "presiden mandataris"
print(n_kalimat)
print(n_kalimat.capitalize())

print(n_kalimat.count('n'))
print(n_kalimat.count('e', 5, 10))

print(n_kalimat.endswith('is'))
print(n_kalimat.endswith('iden'))

n_kal2 = "presiden\tmandataris\tMPRS"
print(n_kal2.expandtabs())
print(n_kal2.expandtabs(4))

print(n_kal2.find('e'))
print(n_kal2.find('en'))
print(n_kal2.rfind('a'))

print(n_kal2.index('en'))
print(n_kal2.rindex('en'))

a_nm = 'ANTON'
b_nm = 'Febianto'
c_addr = 'Madiun'
gabung = 'Nama saya {} {} dan tinggal di {}'.format(a_nm,b_nm,c_addr)
print(gabung)


