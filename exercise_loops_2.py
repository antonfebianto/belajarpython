from countries import countries

ngr_land = []
for negara in countries:
    if 'land' in negara:
        ngr_land.append(negara)
print(ngr_land)


print('\n')
buah = ['banana','orange','mango','lemon']

#buah.reverse()
#for bwah in buah:
#        print(bwah)

mundur_buah = []

for bwah in range(len(buah)-1,-1,-1):
    mundur_buah.append(buah[bwah])
print(mundur_buah)

print('\n')

