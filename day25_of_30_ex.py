import pandas as pd
import numpy as np

print(3*"=","Pandas",3*"=")
angka = [1,2,3,4,5]
series_a = pd.Series(angka)
print(series_a)

print("\n")
series_b = pd.Series(angka, index=[1,2,3,4,5])
print(series_b)

print("\n")
buah = ['Jeruk','Pisang','Mangga']
buah = pd.Series(buah, index=[1,2,3])
print(buah)

print("\nPandas from Dict")
kamus = {
    'nama':'Anton',
    'negara':'Indonesia',
    'kota':'Madiun'
}

pd_unpack = pd.Series(kamus)
print(pd_unpack)

print("\nMembuat Nilai Konstan")
konst = pd.Series(10, index=[1,2,3])
print(konst)

print("\nMembuat Series dengan Linspace")
dt_line = pd.Series(np.linspace(5,20,10))
print(dt_line)

print(3*"=","DataFrame",3*"=")

data_mentah = [
    ['Anton','Indonesia','Madiun'],
    ['Le Wang','Tiongkok','Wouzu'],
    ['Stephen','America','Boston']
]

df = pd.DataFrame(data_mentah, columns=['Nama','Negara','Kota'])
print(df)

print("\n Data Frame dengan Dict")

data_kms = {
    'Nama':['Anton','Xu Pat','Reymond','Vachirawit','Choi Min Hoo'],
    'Country':['Indonesia','Tiongkok','Amerika','Thailand','Korea Selatan'],
    'Kota': ['Madiun','Wouzu','Boston','Chiangmai','Gangnam']
}

df_a = pd.DataFrame(data_kms)
print(df_a)

print("\nMenggunakan CSV")

df_b = pd.read_csv('data\weight-height.csv')
print(df_b)


print("\n",3*"=","Explorasi Data",3*"=")
print("\n",df_b.head())
print("\n",df_b.tail())

print("\n",df_b.shape)
print("\n",df_b.columns)

height = df_b['Height']
print(height)

print("\nWeight")
weight = df_b['Weight']
print(weight)

print(len(height) == len(weight))
print("\n")
print(weight.describe())

print("\nDescribe dataFrame Csv")
print(df_b.describe())


print("\n",3*"=","Modifying a DataFrame",3*"=")
print("\n",3*"+","Creating a DataFrame",3*"+")
print(df)

print("\n",3*"+","Adding a New Column",3*"+")

bb = [77,67,80]
df['Berat Bdn'] = bb
print(df)

tb = [184,181,186]
df['Tinggi Bdn'] = tb
print(df)

print("\n",3*"+","Modify Column Value",3*"+")
df['Tinggi Bdn'] = df['Tinggi Bdn'] * 0.01
print(df)

def hitung_bm():
    bb = df['Berat Bdn']
    tb = df['Tinggi Bdn']
    bmi = []
    for a,s in zip(bb, tb):
        u = a/(s*s)
        bmi.append(u)
    return bmi

bmi = hitung_bm()
df['BMI'] = bmi
print(df)

print("\n",3*"+","Formating DF Columns",3*"+")

df['BMI'] = round(df['BMI'], 1)
print(df)

print("\n")
th_lhr = ['1997','1996','1997']
th_skg = pd.Series(2023, index=[0,1,2])
df['Tahun Lahir'] = th_lhr
df['Tahun Sekarang'] = th_skg
print(df)

print(df['BMI'].dtype)

df['Tahun Sekarang'] = df['Tahun Sekarang'].astype('int')
df['Tahun Lahir'] = df['Tahun Lahir'].astype('int')
print(df['Tahun Sekarang'].dtype)
print(df['Tahun Lahir'].dtype)
print("\n")
umur = df['Tahun Sekarang'] - df['Tahun Lahir']
df['Umur'] = umur
print(df)


print("\n",3*"+","Pengindex Boolean",3*"+")
print(df[df['Umur'] > 26])
print(df[df['Umur'] < 27])