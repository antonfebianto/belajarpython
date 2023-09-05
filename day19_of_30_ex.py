
a_data = open('./files/data_coba.txt')
print(a_data)

bc_data = a_data.read()
print(type(bc_data))
print(bc_data)
a_data.close()

print("\n")
b_data = open('./files/data_coba.txt')
ln_data = b_data.readline()
print(ln_data)
b_data.close()

print("\n")
c_data = open('./files/data_coba.txt')
lnes = c_data.readlines()
print(lnes)
c_data.close()

print('\n')
d_data = open('./files/data_coba.txt')
spl_data = d_data.read().splitlines()
print(spl_data)
d_data.close()

with open('./files/data_coba.txt') as e_data:
    splt_data = e_data.read().splitlines()
    print(type(splt_data))
    print(splt_data)

with open('./files/data_coba.txt','a') as f_data:
    f_data.write('Anton Febianto Bachelor Computer')

#with open('./files/data_coba.txt','w') as g_data:
#    g_data.write('Febianto Anton')

print("\n_______json___________")

import json
data_org = '''{
    "nama":"Anton Febianto",
    "umur":26,
    "negara":"Indonesia",
    "kota":"Madiun",
    "skil":["Excel","SQL","Python"]
}'''

p_dict = json.loads(data_org)
print(type(p_dict))
print(p_dict)
print(p_dict['nama'])


m_dtorg = {
    "nama":"Anton Febianto",
    "negara":"Indonesia",
    "kota":"Madiun",
    "skil":["Excel",'SQL','Python']
}

p_dtorg = json.dumps(m_dtorg, indent=8)
print(type(p_dtorg))
print(p_dtorg)

with open('./files/ex_json.json','w',encoding='utf-8') as sv:
    json.dump(m_dtorg,sv, ensure_ascii=False, indent=2)

print("\n_______CSV__________")
import csv
with open('./files/ex_csv.csv') as a_csv:
    r_csv =csv.reader(a_csv, delimiter=',')
    h_line = 0
    for baris in r_csv:
        if h_line == 0:
            print(f'Nama Kolom :{", ".join(baris)}')
            h_line += 1
        else:
            print(
                f'\t{baris[0]} adalah IT Profesional. Dia tinggal di {baris[1]}, {baris[2]}'
            )
            h_line += 1
    print(f"Jumlah Lines : {h_line}")

print("\n______Excel__________")
import xlrd
excel_dt = xlrd.open_workbook('./files/excel_data.xls')
baca_excel = excel_dt.sheet_by_index(0)
#dt_excel = baca_excel.cell_value(row_number, column_number)
print(baca_excel)
print(excel_dt.nsheets)
print(excel_dt.sheet_names)

print("\n_____XML_______")
import xml.etree.ElementTree as data_xml
t_xml = data_xml.parse('./files/data_xml.xml')
r_xml = t_xml.getroot()
print('Root Tag :', r_xml.tag)
print('Attribute :',r_xml.attrib)
for d_xml in r_xml:
    print('Field :', d_xml.tag)