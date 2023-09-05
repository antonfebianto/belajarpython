import random
import string

def user_random():
    karakter = string.digits + string.ascii_lowercase
    karakter_b = '0123456789abcdef'
    acakan = ''.join(random.choices(karakter, k=6))
    acakan2 = ''.join(random.choices(karakter_b, k=6))
    return acakan, acakan2

print(user_random())


def user_id_gen_by_user(digit, jml):
    user_unique = []
    karak_a = string.ascii_letters + string.digits

    for _ in range(digit):
        id_user = ''.join(random.choices(karak_a, k=jml))
        user_unique.append(id_user)
    
    for i in user_unique:
        print(i)

print (user_id_gen_by_user(5,16))
print("\n")

def warna():
    red= random.randint(0,255)
    green= random.randint(0,255)
    blue=random.randint(0,255)

    return f"rgb({red},{green},{blue})"

print(warna())
print("\n")

def list_hexa_colors(digit,panjang):
    rand_id = []
    karak_b = string.hexdigits

    for _ in range(digit):
        id_warna ="#"+''.join(random.choices(karak_b, k=panjang))
        rand_id.append(id_warna)
    return rand_id

print(list_hexa_colors(5,6))

print('\n')

def list_rgb_colors(digit):
    rgb_rand = []

    for _ in range (digit):
        warna_a = random.randint(0,255)
        warna_b = random.randint(0,255)
        warna_c = random.randint(0,255)
        hasil = f"rgb({warna_a},{warna_b},{warna_c})"
        rgb_rand.append(hasil)
    return(rgb_rand)

print(list_rgb_colors(5))

print('\n')
def generate_color(digit,identity='hexa'):
    warna = []

    for _ in range (digit):
        if identity == 'hexa':
            warna_x = hex_color()
        elif identity == 'rgb':
            warna_x = rgb_color()
        else:
            raise ValueError(f"Invalid Format: {identity}. support formats are 'hexa' and 'rgb'.")
        warna.append(warna_x)

    return warna

def hex_color():
    karak_b = string.hexdigits
    id_user ="#" + ''.join(random.choices(karak_b, k=6))
    return id_user

def rgb_color():
    warna_a = random.randint(0,255)
    warna_b = random.randint(0,255)
    warna_c = random.randint(0,255)
    hasil = f"rgb({warna_a},{warna_b},{warna_c})"
    return hasil

print(generate_color(5,identity='hexa'))
print(generate_color(5,identity='rgb'))

print('\nLevel 3')

def shuffle_list(digit, n):
    rand_angk = []
    karakter_x = '1234567890'
    for _ in range(n):
        daft_acak= ''.join(random.choices(karakter_x, k=digit))
        rand_angk.append(daft_acak)
    
    for i in rand_angk:
        print("Angka acak:",i)

print(shuffle_list(5,7))
