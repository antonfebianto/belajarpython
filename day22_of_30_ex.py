import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/datasets'

p_proses = requests.get(url)
p_status = p_proses.status_code
p_konten = p_proses.content
soup = BeautifulSoup(p_konten,'html.parser')
print(soup.title)
print(soup.title.get_text())
print(soup.body)
print(p_proses.status_code)

tabel = soup.find_all('table',{'cellpadding':'3'})
table = tabel[0]
for td in table.find('tr').find_all('td'):
    print(td.text)