class Person:
    def __init__(self,name):
        self.name = name


p = Person('Anton')
print(p.name)
print(p)

print("\n")

class Orang:
    def __init__(self, nama_awl,nama_akh,umur,negara,kota):
        self.nama_awl = nama_awl
        self.nama_akh = nama_akh
        self.umur = umur
        self.negara = negara
        self.kota = kota

p_fg = Orang('Anton','Febianto',26,'Indonesia','Madiun')
print(p_fg.nama_awl)
print(p_fg.nama_akh)
print(p_fg.umur)
print(p_fg.negara)
print(p_fg.kota)

print('\n')
class Norang:
    def __init__(self,nama_awl,nama_akh,umur,negara,kota):
        self.nama_awl = nama_awl
        self.nama_akh = nama_akh
        self.umur = umur
        self.negara = negara
        self.kota = kota
    def ninfo(self):
        return f"{self.nama_awl} {self.nama_akh} is {self.umur} year old. He lives in {self.kota},{self.negara}"
    
p_fg1 = Norang('Anton','Febianto',26,'Indonesia','Madiun')
print(p_fg1.ninfo())
print('\n')

class Nperson:
    def __init__(selfa, nama_a='Anton',nama_b='Febianto',age=26,negara='Indonesia',kota='Madiun'):
        selfa.nama_a = nama_a
        selfa.nama_b = nama_b
        selfa.age = age
        selfa.negara = negara
        selfa.kota = kota
    
    def info_dong(selfa):
        return f"{selfa.nama_a} {selfa.nama_b} is {selfa.age} year old. He lives in {selfa.kota},{selfa.negara}"
    
p1 = Nperson()
print(p1.info_dong())
p2 = Nperson('Aswin','Rifai',27,'Indonesia','Madiun')
print(p2.info_dong())
print('\n')

class Skill:
    def __init__(selfa, nama_a='Anton',nama_b='Febianto',age=26,negara='Indonesia',kota='Madiun'):
        selfa.nama_a = nama_a
        selfa.nama_b = nama_b
        selfa.age = age
        selfa.negara = negara
        selfa.kota = kota
        selfa.skills = []
    
    def p_info(selfa):
        return f"{selfa.nama_a} {selfa.nama_b} is {selfa.age} year old. He lives in {selfa.kota},{selfa.negara}"
    def add_skl(selfa, skill):
        selfa.skills.append(skill)

p_class = Skill()
print(p_class.p_info())
p_class.add_skl('SQL')
p_class.add_skl('Hack')
p_class.add_skl('Makan')
p_class2 = Skill('Aswin','Rifai',27,'Indonesia','Madiun')
print(p_class2.p_info())
print(p_class.skills)
print(p_class2.skills)


print('\Metode Inheritance')

class Murid(Skill):
    pass

s1 = Murid('Elphin','Putra',26,'Indonesia','Tulungagung')
s2 = Murid('Aswin','Rifai',27,'Indonesia','Madiun')
print(s1.p_info())
s1.add_skl('Modeling')
s1.add_skl('Volley')
s1.add_skl('Gym')
print(s1.skills)

print(s2.p_info())
s2.add_skl('Tidorr')
s2.add_skl('Tidorr')
s2.add_skl('Tidorr')
print(s2.skills)

print('\n')
class Murid2(Skill):
    def __init__(selfa, nama_a='Anton',nama_b='Febianto',age=26,negara='Indonesia',kota='Madiun',kelamin='lanang'):
        selfa.kelamin = kelamin
        super().__init__(nama_a,nama_b,age,negara,kota)
    def p_infolg(selfa):
        kelamin = 'He' if selfa.kelamin == 'lanang' else 'She'
        return f"{selfa.nama_a} {selfa.nama_b} is {selfa.age} year old. {kelamin} lives in {selfa.kota},{selfa.negara}"
    

k1 = Murid2('Erlita','Trepes',26,'Indonesia','Madiun','wedok')
k2 = Murid2('Aswin','Rifai',27,'Indonesia','Madiun','lanang')
print(k1.p_infolg())
k1.add_skl('Paok')
k1.add_skl('Paok')
k1.add_skl('Paok')
print(k1.skills)

print(k2.p_infolg())
k2.add_skl('Tidor')
k2.add_skl('Tidor')
k2.add_skl('TIdor')
print(k2.skills)
