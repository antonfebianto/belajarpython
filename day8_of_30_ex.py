#day 8
#dictionary
print("Dictionary")
print("""Dictionary
merupakan kumpulan type data yg tdk diurutkan,
dapat di modifikasi dan di pair/hubungkan""")
print('\n')

empty_dict = {}

idn_org = {
    'first_nm':'Anton',
    'last_nm': 'Febianto',
    'age':26,
    'country':'Indonesia',
    'is_married': False,
    'skills':['Cliper','Foxpro','SQL','HTML'],
    'address':{
        'village':'Purwosari',
        'zipcode' : '63157'
    }
}

print(idn_org)
print("Panjang Dict : ",len(idn_org))
print('\n')
print("Mengakses item Dict")
print("Nama : ",idn_org['first_nm'])
print("Negara :",idn_org['country'])
print("Alamat :",idn_org['address']['village'])
#print(idn_org['city'])

print('\n')
print('dengan metode get()')
print("Nama :",idn_org.get('first_nm'))
print("Umur ; ", idn_org.get('age'))
print("Negara :",idn_org.get('country'))
print("Kota Asal :",idn_org.get('city'))

print('\n')
print('Menambah key pada dict')

idn_org['Campus']='Unipma'
idn_org['Company']='PT.Berlian Jaya Perkasa'
print(idn_org)
print('\n')
idn_org['skills'].append('C++')
print(idn_org)

print('\n')
print("Memodifikasi item dalam dict")
idn_org['age']=27
print(idn_org)
print('\n')
print('first_nm' in idn_org)
print('city' in idn_org)

idn_org.pop('Campus')
print(idn_org)

idn_org.popitem()
print(idn_org.popitem())
del idn_org['is_married']
print(idn_org)
print(idn_org.items())

idn_org2 = idn_org.copy()
print(idn_org2)

kunci = idn_org.keys()
print(kunci)
#print(idn_org.clear())

for gembok in kunci:
    print(gembok)

item = idn_org.values()
print(item)

for detil in item:
    print(detil)