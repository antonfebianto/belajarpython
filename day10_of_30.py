print('exercise day 10')
print("level 1")

for urut in range(11):
    print(urut)

print("___while_______")

ngurut = 0
while ngurut < 11:
    print(ngurut)
    ngurut = ngurut + 1

print('\n______no 2____')

for mundur in range(10,-1,-1):
        print(mundur)
        
print('___While______')

mundur_a = 10
while mundur_a >= 0:
    print(mundur_a)
    mundur_a = mundur_a - 1

print('\n_______no 3__________')
for i in range (-1,8):
    print('#' * i)


print("\nNomor 4")

for a in range(8):
    for k in range(8):
        print("#", end=" ")
    print()


print("\n")

for c in range(11):
    hasil =c * c
    print(f"{c} x {c} = {hasil}")

print("\n")

prog = ['Python','Numpy','Pandas','Django','Flask']
for p in prog:
    print(p)

print("\n")
for genap in range(101):
    if genap%2==0:
        print(genap)


print("\nganjil")
for ganjil in range(100):
    if ganjil%2 == 1:
        print(ganjil)

print("\n Level 2")

total = 0
for ctk in range(101):
    total += ctk
print("Penjumlaha total :", total)