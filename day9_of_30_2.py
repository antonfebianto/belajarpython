print('Exercise level 3')

dataku = {
    'nama_dpn':'Anton',
    'nama_blk':'Febianto',
    'umur':26,
    'is_married':False,
    'negara':'Indonesia',
    'skill':['JavaScript','React','Node','MongoDB','Python'],
    'addres':{
        'jalan':'Pangsud',
        'zipcode':'63157'
    }
}

#

 #* Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 #* Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 #* If the person is married and if he lives in Finland, print the information in the following format:

if 'skill' in dataku:
    terampil = dataku['skill']
    if len(terampil) > 0:
        idx_tgh = len(terampil)//2
        t_tgh = terampil[idx_tgh]
        print('Middle Skill :', t_tgh)
    else:
        print("data tidak ada")
else:
    print('data tidak ada')


print('\n')
if 'skill' in dataku:
    terampil2 = dataku['skill']
    if 'Python' in terampil2:
        print('Iya ada Dong')
    else:
        ('Tidak Ada')
else:
    print('tidak ada')


print('\n')
#* If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB,
# Print('He is a fullstack developer'), 
# else print('unknown title')
# for more accurate results more conditions can be nested!




if 'skill' in dataku:
    dftr = dataku['skill']
    if all(skill in dftr for skill in ['JavaScript','React']):
        print('Frond End developer')
    elif all(skill in dftr for skill in ['Node','MongoDB','Python']):
        print('Back End Developer')
    elif all(skill in dftr for skill in ['React','Node','MongoDB']):
        print('Full Stack Developer')
    else :
        print("Unkown title")
else:
    print('Uknown title')


print('\n')

if 'is_married' in dataku:
    if not dataku['is_married']:
        print(dataku['nama_dpn']," tingal di ",dataku['negara'], "Dia belum menikah")
    else:
        print('Belum nikah')
else:
    print('Raurus')
    