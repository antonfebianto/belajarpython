from datetime import datetime
#Get the current day, month, year, hour, minute and timestamp from datetime module
#Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
#Today is 5 December, 2019. Change this time string to time.
#Calculate the time difference between now and new year.
#Calculate the time difference between 1 January 1970 and now.
#Think, what can you use the datetime module for? Examples:
#Time series analysis
#To get a timestamp of any activities in an application
#Adding posts on a blog

tgl_now = datetime.now()
print(tgl_now)

hari = tgl_now.day
bulan = tgl_now.month
tahun = tgl_now.year
jam = tgl_now.hour
menit = tgl_now.minute
detik = tgl_now.second

stem_w = tgl_now.timestamp()
print(hari,bulan,tahun,jam,menit)
print("Current time :", stem_w)
print(f"{hari}/{bulan}/{tahun}, {jam}:{menit}:{detik}")

print("\nNo 2")
f_waktu = tgl_now.strftime("%m/%d/%Y, %H:%M:%S")
print(f_waktu)

print("\nNo 3")
tgl_string = "5 December 2023"
pecah_string = datetime.strptime(tgl_string, "%d %B %Y")
print(tgl_string)
print(pecah_string)

print("\nNo 4")

h_cur = datetime(year=2023, month=7, day=25, hour=18, minute=30, second=10)
h_new = datetime(year=2024, month=10, day=24, hour=10, minute=10, second=30)
t_diff = h_new - h_cur
print(f"Masa Jabatan Presiden dan Wapres tinggal : {t_diff}")

print("\nNo 5")
h_date = datetime(year=1970, month=1, day=1)
h_now = datetime(year=2023, month=7, day=25)
t3 = h_now - h_date
print(f"{t3}")
