print("Day 11 -  Function/fungsi")

print("Fungsi tanpa Parameter")

def detil_nama():
    first_nm = 'Anton'
    last_nm = 'Febianto'
    space = ' '
    full_nm = first_nm, space, last_nm
    full_nm2 = first_nm + space + last_nm
    print(full_nm)
    print(full_nm2)
detil_nama()

print('\n')
def p_angka ():
    angka1 = 2
    angka2 = 3
    total = angka1 + angka2
    print(angka1,"+",angka2," = ", total)
p_angka()

print("\n")
print("Fungsi return nilai - Bag.1")

def d_nama():
    nama_1 = 'Anton'
    nama_2 = 'febianto'
    spasi = " "
    all_nm = nama_1+spasi + nama_2
    return all_nm
print(d_nama())

def kali():
    nilai_a = 10
    nilai_b = 5
    kalikan = nilai_a * nilai_b
    return kalikan
print(kali())

print('\n')
print("Function dengan Parameter")
print("- Parameter tunggal (Single Parameter)")

def salam (nama):
    pesan ="Hai "+ nama + ' ,Selamat Datang!!'
    return pesan
print(salam('Anton Febianto'))
print('\n')
def h_kembali(jumlah):
    donasi = 1000
    return jumlah-donasi
print(h_kembali(20000))

print("\n")
def l_persegi(j_nilai):
    return j_nilai * j_nilai
print(l_persegi(10))

def total_angka(i_angka):
    total = 0
    for i in range(i_angka+1):
        total+=i
    print(total)
total_angka(100)

def segitiga(n_sisi):
    h_angk = 0
    for c in range(n_sisi+1):
        print("+"*c)
        c += c
        
        if h_angk > n_sisi:
            break
    print("selesai")
segitiga(7)

print('\n')
def l_ling(jr_ling):
    phi = 3.14
    ls_ling = phi * jr_ling**2
    return ls_ling
print(l_ling(7), "cm")

print('\n')
print("2 Parameter (Two Parameter)")

def nama_lengkap(nm_dpn, nm_akh):
    spasii = ' '
    n_lkp = nm_dpn + spasii + nm_akh
    return  n_lkp
print('Nama Lengkap Saya: ',nama_lengkap('Anton', 'Febianto'))

def umur (current_year, birth_year):
    h_umur = current_year - birth_year
    return h_umur
print('Umur Saya : ', umur(2023, 1997), 'tahun')

def berat_obj(massa, gravitasi):
    berat = str(massa * gravitasi)+ ' N'
    return berat
print("Massa Suatu Benda adalah :", berat_obj(120, 9.81))

print('\n')
print('Passing Argumen with Key & Value')
print(nama_lengkap(nm_dpn='Anton', nm_akh='Febianto'))
print(umur(current_year=2023, birth_year=1997))
print(berat_obj(massa=120,gravitasi=9.81))

print('\n')
print('Fungsi return nilai - Bag.2')

def genap(n_genap):
    if n_genap%2 ==0:
        return True
    return False
print("88 T/F Genap ? :",genap(88))
print("7 T/F Genap ? :",genap(7))

print('\n')

def f_angka(n_angka):
    genapin = []
    for i in range(n_angka+1):
        if i%2 == 0:
            genapin.append(i)
    return(genapin)
print("Nilai Genap :", f_angka(100))

print("\n")
print("Function dgn Param Default")

def ucapan(pengucap='Yesus'):
    notif = pengucap + ', Selamat Belajar'
    return notif
print(ucapan())
print(ucapan('Anton Febianto'))
print(ucapan(pengucap='Anton S.Kom'))

print("\n")
print("Arbitrary Number Of Arguments")

def penjlm_loop(*s_angka):
    total_s = 0
    for sembarang in s_angka:
        total_s += sembarang
    return total_s
print(penjlm_loop(1,2,3))
print(penjlm_loop(10,11,12))

print("Param Default dan Sembarang")

def prodi(kampus, *jur_kmps):
    print(kampus)
    for q in jur_kmps:
      print(q)
print(prodi('Unipma :','TIF','PTE','TSI','TIN'))

print("\nFunction menggunakan Function")

def akar(n_angka):
    return n_angka*n_angka
def fungsifx (f, x):
    return f(x)
print(fungsifx(akar, 6))