#day16
print("Day 16 - Date time")
#datetime module untuk menghandel tanggal dan waktu

import datetime
print(dir(datetime))
print("\n")

from datetime import datetime

current = datetime.now()
print(current)

hari = current.day
bulan = current.month
tahun = current.year
jam = current.hour
menit = current.minute
detik = current.second

d_waktu = current.timestamp()
print(hari,bulan,tahun,jam,menit,detik)
print("Detail Waktu :", d_waktu)
print(f"{hari}/{bulan}/{tahun}, {jam}:{menit}:{detik}")

print("\nstrftime")
from datetime import datetime as m_tgl
tahun_lahir = m_tgl(1997,3,20)
print(tahun_lahir)

l_hari = tahun_lahir.day
l_bulan = tahun_lahir.month
l_tahun = tahun_lahir.year
l_jam = tahun_lahir.hour
l_menit = tahun_lahir.minute
l_detik = tahun_lahir.second
print(l_hari, l_bulan, l_tahun, l_jam, l_menit, l_detik)
print(f"{l_hari}/{l_bulan}/{l_tahun}, {l_jam}:{l_menit}:{l_detik}")

print("\n")

skrg = m_tgl.now()
d_time = skrg.strftime("%H:%M:%S")
print(f"Jam : {d_time}")

d_time1 = skrg.strftime("%m/%d/%Y, %H:%M:%S")
print(f"Jam_2 : {d_time1}")

d_time2 = skrg.strftime("%d/%m/%Y, %H:%M:%S")
print(f"Jam_3 : {d_time2}")

print("\nstrptime")

tgl_str = "20 March 1997"
print("Tanggal String :", tgl_str)
tgl_obj = m_tgl.strptime(tgl_str,"%d %B %Y")
print(f"Tgl Lahirmu : {tgl_obj}")

print("\nMenggunakan Tanggl dari datetime")
p_wktu = m_tgl(1997,3,20)
print(p_wktu)
print("Current date:", p_wktu.today())

hr_ini = m_tgl.today()
print("Tahun Berjalan:", hr_ini.year)
print("Bulan Berjalan :", hr_ini.month)
print("Hari Berjalan :", hr_ini.day)

print("\nObjek Waktu to Represent time")

from datetime import time
a = time()
print(f"a= {a}")

b = time(10,30,50)
print(f"b = {b}")

c = time(hour=10, minute=30, second=43)
print(f"c = {c}")

d = time(10, 30, 50, 200000)
print(f"d= {d}")

print("\n")
t_curr = m_tgl(year=1997, month=3, day=5)
n_year = m_tgl(year=2024, month=1, day=1)
gap_th = n_year - t_curr

print(f"berapa tahun aku :", gap_th)

print("\nMenggunakan Timedelta")

from datetime import timedelta

w1 = timedelta(weeks=13, days=10, hours=5, seconds=30)
w2 = timedelta(days=14, hours=7, minutes=20, seconds=10)
diff = w1 - w2
print(diff)

from package import artmatika

artmatika.bagi(10,2)