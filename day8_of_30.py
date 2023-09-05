print("Days 8")
print('Exercise')

anjing ={}
print(anjing)
anjing['nama'] ='Chiko'
anjing['warna']='pelangi'
anjing['ras'] ='Persia'
anjing['kaki']='Pendek'
anjing['usia']=3
print(anjing)

print('\n')
m_siswa = {
    'first_name':'Angelo',
    'last_name':'Calisto',
    'gender':'Male',
    'age':23,
    'is_married':False,
    'skills':['Fisika','Kimia','Computer Sains'],
    'city':'Madiun',
    'address':{
        'street':'Jl.Pangsud',
        'zipcode':'63157',
    }
}

print("banyak data dict :",len(m_siswa))
print(m_siswa.get('skills'))
print(type(m_siswa.get('skills')))
m_siswa['skills'].append('HTML')
m_siswa['skills'].append('Cook')
print(m_siswa)

kunci = m_siswa.keys()
print(kunci)
print('\n')

detil = m_siswa.values()
print(detil)

print('\n')
konversi = m_siswa.items()
print(konversi)

print('\n')
m_siswa.pop('last_name')
print(m_siswa)

del m_siswa
