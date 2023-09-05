print("Exercise Day 18 Regular Expression")
print("Level - 1")

import re
from collections import Counter
m_paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

def cari_jdata(paragrap,n=5):
    m_regex = r'\b\w+\b'
    m_cocok = re.findall(m_regex,paragrap.lower())
    m_hitung = Counter(m_cocok)
    m_modus = m_hitung.most_common(n)
    return [(f,w) for f,w in m_modus]

print(cari_jdata(m_paragraph,999))

print('\nNo 2')

points = ['-12', '-4', '-3', '-1', '0', '4', '8']
urut_point = sorted([int(re.search(r'-?\d+',p).group()) for p in points])
jarak =urut_point[-1] - urut_point[0]
print(urut_point)
print(jarak)


print("\nExercise level 2")
def is_valid_var(var):
    regex = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return re.match(regex,var) is not None

print(is_valid_var('firs_name'))
print(is_valid_var('first-name'))
print(is_valid_var('1first_name'))
print(is_valid_var('firstname'))

print('\nExercise Level 3')
def sub_kata(paragrap):
    cocok = re.sub(r'[^a-zA-Z ]','',paragrap)
    return cocok
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
print(sub_kata(sentence))

print(cari_jdata(sub_kata(sentence)))

