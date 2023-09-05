#import webbrowser

#url_list = [
#    'https://www.python.org',
#    'https://www.mtr-cc.com']

#for url in url_list:
#    webbrowser.open_new_tab(url)


import numpy as np

matric_a = np.array([1,2,3,4])
print(matric_a)
zeros_a = np.zeros([1,3,2])
print(zeros_a)
ones_a = np.ones((5,2))
print(ones_a)

import requests

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'

respon = requests.get(url)
print(respon)
print(respon.status_code)
print(respon.headers)
print(respon.text)

#url_c = 'https://github.com/mdn/dom-examples/blob/main/fetch/fetch-json/products.json'

#respon_c = requests.get(url_c)
#print(respon_c)
#print(respon_c.status_code)
#negara = respon_c.json()
#print(negara)


print("\n")
from package import artmatika
print(artmatika.bagi(10,2))

from package import greet

print(greet.salam('Anton','Febianto'))
