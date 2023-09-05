import re
teks = 'Aku Suka Phi Win'
cocok = re.match('Aku Suka',teks, re.I)
print(cocok)
span = cocok.span()
print(span)

awal,akhir = span
print(awal, akhir)
substring = teks[awal:akhir]
print(substring)

print('\n')
kata = 'i love you 3000 in every universe'
p_cocok = re.match('I love you 3000', kata, re.I)
print(p_cocok)

print("\nSearch")
q_cocok = re.search('love',kata, re.I)
print(q_cocok)

q_span = q_cocok.span()
print(q_span)

q_awal, q_akhir = q_span
print(q_awal, q_akhir)
q_substring = kata[q_awal: q_akhir]
print(q_substring)

print('\n')
kata_b = '''Getaran adalah gerak bolak balik
antara titik setimbang gerak getaran'''

r_cocok = re.findall('gerak', kata_b, re.I)
print(r_cocok)
r_cocok_b = re.findall('getaran', kata_b,re.I)
print(r_cocok_b)
r_cocok_c = re.findall('getaran|Getaran', kata_b)
print(r_cocok_c)
r_cocok_d = re.findall('[Gg]erak',kata_b)
print(r_cocok_d)

print('\nSubstring')
d_txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

d_ganti = re.sub('Python|python','Javascript', d_txt)
print(d_ganti)
d_ganti_b = re.sub('[Pp]ython','C++',d_txt)
print(d_ganti_b)
d_ganti_c =re.sub('python','SQL',d_txt,re.I)
print(d_ganti_c)

print("\n")
m_txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

m_gab = re.sub('%', '',m_txt)
print(m_gab)

print('\nSplit/Memisahkan')

m_split = re.split('\n',d_txt)
print(m_split)

print("Menulis Pola RegEx")

pola_regex = r'apple'
t_text = 'Apple and banana are fruits. An old clich says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
k_cocok = re.findall(pola_regex, t_text)
print(k_cocok)

pola_regex_b = f'banana'
k_cocok_b = re.findall(pola_regex_b,t_text, re.I)
print(k_cocok_b)

print("\nSquare Bracket")
sqr_brac = r'[Aa]pple'
sq_cocok = re.findall(sqr_brac,t_text)
print(sq_cocok)

sqr_brac_b =r'[Aa]pple|[Bb]anana'
sq_cocok_b = re.findall(sqr_brac_b,t_text)
print(sq_cocok_b)

print("\nEscape Character")
reg_pat = r'\d'
f_txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
reg_cocok = re.findall(reg_pat,f_txt)
print(reg_cocok)

reg_pat_b = r'\d+'
reg_cocok_b = re.findall(reg_pat_b,f_txt)
print(reg_cocok_b)


print("\nPeriode")
reg_pat_c = r'[a].'
reg_cocok_c = re.findall(reg_pat_c,f_txt)
print(reg_cocok_c)

reg_pat_d = r'[a].+'
reg_cocok_d = re.findall(reg_pat_d, f_txt)
print(reg_cocok_d)

print('\nZero Or More times(*)')

reg_zero = r'[a].*'
c_text = '''Apple and banana are fruits'''
pn_cocok = re.findall(reg_zero, c_text)
print(pn_cocok)

print('\nZero Or More times(?)')
n_txt = txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
reg_zero_intro = r'[eE]-?mail'
x_cocok = re.findall(reg_zero_intro,n_txt)
print(x_cocok)

print("\nQuantifier in RegEx")
g_txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
g_reg_ptt = r'\d{4}'
g_cocok = re.findall(g_reg_ptt,g_txt)
print(g_cocok)

print('\nCart^')
ca_text = 'Ini merupakan contoh regular expression yang dibuat pada 2 Agustus, 2023'
ca_regex = r'^Ini'
ca_cocok = re.findall(ca_regex, ca_text)
print(ca_cocok)

print('\nNegation/Penyangkalan')
neg_regex = r'[^A-Za-z ]+'
neg_text = 'Ini merupakan contoh dari regular expresion pada 2 Augustus, 2023 dan di update pada 17 Agustus, 2023'
neg_cocok = re.findall(neg_regex,neg_text)
neg_cocok_a = re.findall(neg_regex,g_txt)
print(neg_cocok)
print(neg_cocok_a)