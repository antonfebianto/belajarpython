import requests
import re
from collections import Counter
def romeo_juliet (url,n):
    p_resp = requests.get(url)
    konten = p_resp.text

    regex = r'\b\w+\b'
    kata = re.findall(regex, konten)
    f_kata = Counter(kata)
    s_kata = f_kata.most_common(n)
    return s_kata

url = 'http://www.gutenberg.org/files/1112/1112.txt'

print(romeo_juliet(url, 10))


print("\n")

import json
import statistics

def get_data_kucing(url):
    c_resp = requests.get(url)
    konten = c_resp.json()
    return konten


def berat_kucing(dt_kucing):
    berat = [cat['weight']['metric'].split()[0] for cat in dt_kucing]
    berats = [float(b_berat) for b_berat in berat]

    kc_min = min(berats)
    kc_max = max(berats)
    kc_mean= sum(berats) /  len(berats)
    kc_median = statistics.median(berats)
    kc_stdev = statistics.stdev(berats)

    return kc_min,kc_max,kc_mean,kc_median,kc_stdev


def data_lifespan(dt_lifespan):
    lifespan = [cat['life_span'].split()[0] for cat in dt_lifespan if cat['life_span'] != 'Unknown']
    lifespans = [int(kc_life) for kc_life in lifespan]

    life_min = min(lifespans)
    life_max = max(lifespans)
    life_mean = sum(lifespans)/ len(lifespans)
    life_median = statistics.median(lifespans)
    life_stddev = statistics.stdev(lifespans)

    return life_min,life_max,life_mean,life_median,life_stddev

def freq_table(tb_kucing):
    negara = [cat['origin'] for cat in tb_kucing if 'origin' in tb_kucing]
    breeds = [cat['name'] for cat in tb_kucing if 'name' in cat]

    freq_negara = Counter(negara)
    freq_breed = Counter(breeds)

    return freq_negara, freq_breed


kc_api = 'https://api.thecatapi.com/v1/breeds'
kc_data = get_data_kucing(kc_api)

kc_min,kc_max,kc_mean,kc_median,kc_stdev = berat_kucing(kc_data)

print('Nilai Minimum : {}'.format(kc_min))
print('Nilai Maximal : {}'.format(kc_max))
print('Nilai Rata2 : {}'.format(kc_mean))
print('Nilai Tengah : {}'.format(kc_median))
print('Nilai Std Deviasi : {}'.format(kc_stdev))

print("\n")

life_min,life_max,life_mean,life_median,life_stddev = data_lifespan(kc_data)
print('Nilai Minimum : {}'.format(life_min))
print('Nilai Maximal : {}'.format(life_max))
print('Nilai Rata2 : {}'.format(life_mean))
print('Nilai Tengah : {}'.format(life_median))
print('Nilai Std Deviasi : {}'.format(life_stddev))

print('\n')

freq_negara, freq_breed = freq_table(kc_data)
for negara, freq in freq_negara.items():
    print(f"{negara} : {freq}")

for breed, freq in freq_breed.items():
    print(f"{breed} : {freq}")