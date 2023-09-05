print('Exercise day-19')
print("Level-1")
print("No 1")
#A


def jl_ln_kt(data):
    line = data.readlines()
    kata = ''.join(line).split()
    h_line = len(line)
    h_kata = len(kata)
    print('Jumlah Kata dalam Pidato : ', h_kata)
    print('Junmlah Line dalam Pidato :', h_line)
print("a) President Obama Speech")
with open('./data/obama_speech.txt') as obama:
    print(jl_ln_kt(obama))

print("\nb) First Lady Michell Obama Speech")
with open('./data/michelle_obama_speech.txt') as firs_lady:
    print(jl_ln_kt(firs_lady))

print("\nc) President Donald Trump Speech")
with open('./data/donald_speech.txt') as donald:
    print(jl_ln_kt(donald))

print("\nd) First Lady Melina Trump Speech")
with open('./data/melina_trump_speech.txt') as melina:
    print(jl_ln_kt(melina))

print("______No 2______")

import json
def topten_bhs(data):
    h_bahasa = {}
    for n in data:
        d_bhs = n.get('languages',[])
        for p_bhs in d_bhs:
            h_bahasa[p_bhs] = h_bahasa.get(p_bhs,0) + 1
    t_ten = sorted(h_bahasa.items(), key=lambda b:b[1],reverse=True)
    top_ten = t_ten[:10]
    return top_ten
def most_popular(data):
    t_pop = sorted(data, key=lambda p:p['population'], reverse=True)
    ten_pop = t_pop[:10]
    return ten_pop

with open('./data/countries_data.json','r', encoding='utf-8') as dt_neg:
    p_neg = json.load(dt_neg)

proses = topten_bhs(p_neg)
proses_b = most_popular(p_neg)
print("Most Languange Top 10")
for b,j in proses:
    print(f"{b}, {j}")
print('\nNo3. Most Population Top 10')
for c in proses_b:
    print(f"{c['name']}, {c['population']}")


print("\nNo 4")
import re
def ekstrak(filename):
    with open(filename,'r',encoding='utf-8') as data:
        email = data.read()

    reg_pat = f'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    inc_email = re.findall(reg_pat, email)
    return inc_email

filename = './data/email_exchanges_big.txt'
print(ekstrak(filename))


from collections import Counter

def most_kata(data,n):
    with open(data, 'r', encoding='utf-8') as txt:
        konten = txt.read()
    regex = r'\b\w+\b'
    kata = re.findall(regex, konten)
    f_kata = Counter(kata)
    most_kt = f_kata.most_common(n)
    return most_kt
print(most_kata('./data/obama_speech.txt',15))

