print("Loops")
print("While Loops")
print("1.")
print("_____________________")

ulang_a = 0
while ulang_a < 5 :
    print(ulang_a)
    ulang_a = ulang_a + 1


print("\n")
print('2.')
print("____________________")

ulang_b = 0
while ulang_b < 5:
    print(ulang_b)
    ulang_b = ulang_b + 1
else:
    print(ulang_b)

print("\n")
print('3.')
print("_______Break dan Continue_____________")

ulang_c = 0
while ulang_c < 5:
    print(ulang_c)
    ulang_c = ulang_c + 1
    if ulang_c == 3:
        break

print("\n")
print("Continue")
ulang_d = 1
while ulang_d < 20:
    if ulang_d == 16:
        continue
    print(ulang_d)
    ulang_d = ulang_d + 1


print("\n")
print("Continue")