from countries_data import data

total_bhs = 0
for bahasa in data:
    total_bhs += len(bahasa["languages"])
print("Total Bahasa Yang digunakan :", total_bhs)

print("\n")


t_bhs = {}
for i in data:
    for d_bhs in i["languages"]:
        t_bhs[d_bhs] = t_bhs.get(d_bhs, 0) +1

bhs_10 = sorted(t_bhs.items(), key=lambda x: x[1], reverse=True)[:10]
print("10 bahasa yang sering dipakai :")
for d_bhs, hitung in bhs_10:
    print(d_bhs)
 
print('\n')

top_10p = sorted(data, key=lambda x: x["population"], reverse=True)[:10]

print("10 Negara Populasi terbesar : ")
for n in top_10p:
    print(n["name"])
