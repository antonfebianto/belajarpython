
print("Level 1")
print("Soal Nomor 1,2,3,4")

daftar_brg = ['YGP','HGP','SGP','YLB','SGO']
print(daftar_brg)
print('Banyak Data :',len(daftar_brg))
print("Data pertama, tengan, akhir :",daftar_brg[::2])

print("_____________________")
print("Soal Nomor 5")
mixed_data_types=['Anton',26,180,False,{'Addres':'Indonesia'}]
print(mixed_data_types)

print("_____________________")
print("Soal Nomor 6,7,8,9")
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[::3])

print("_____________________")
print("Soal Nomor 6,7,8,9")
it_companies[2] = 'Cisco'
print(it_companies)

it_companies.append('Intel')
print(it_companies)

it_companies.insert(3, 'AMd')
print(it_companies)

up_it_comp = it_companies[0]
print(up_it_comp.upper())

gabung = '#'.join (it_companies)
print(gabung)

cari = 'Apple' in it_companies
print("Yt ada Apple :",cari)

it_companies.sort()
print(it_companies)

it_companies.sort(reverse=True)
print(it_companies)

print("________________")
print(it_companies[0:6])
print("________________")
print(it_companies[-6:])

print("___________________")
it_companies2 = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
p_data = len(it_companies2) / 2
print(p_data)
print(it_companies2[3])
it_companies2.remove('Apple')
print(it_companies2)

del it_companies2[0]
print(it_companies2)

del it_companies2[-1]
print(it_companies2)

del it_companies2[0::]
print(it_companies2)

it_companies2.clear()
print(it_companies2)

it_companies.clear()
print(it_companies)


front_end = ['HTML','CSS','JS','React','Redux']
back_end = ['Node','Express','MongDB']
r_gabung = front_end + back_end
rk_gabung = ",".join(r_gabung)
print(r_gabung)
print(rk_gabung)

full_stack = r_gabung.copy()
print(full_stack)
full_stack.append('Python')
full_stack.append('SQL')
print(full_stack)

print("\n")
print("___________________")
print("Level 2")
print("Soal nomor 1")

ages =[19,22,19,24,20,25,26,24,25,24]
print(ages)

ages.sort()
print("Data urut asc : ",ages)

minim = ages[0]
maxim = ages[-1]
print("Nilai Min: ", minim)
print("Nilai Max :", maxim)

j_data = len(ages)
print("jumlah Data : ", j_data)
n_median = j_data / 2
print("Urutan Nilai tengah Ke-:" , n_median)
h_median = (ages[5] + ages[6])/2
print('Median : ', int(h_median))

tot_data = sum(ages)
avg = tot_data / 10
print("Average :", avg)

rentang = max(ages) - min(ages)
print("Range :", rentang)

min_diff = minim - avg
max_diff = maxim - avg
print("Perbandingan Min - Avg :", min_diff)
print("Perbandingan Max - Avg : ",max_diff)

print("min - avg > :",min_diff > max_diff)
print("max - avg < :", min_diff < max_diff)







