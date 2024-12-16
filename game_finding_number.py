import random
def user_play(x=10):
    print("Keling son o'yinini o'ynaymiz men bir son o'ylayman siz topasiz")
    print(f"1 dan {x} gacha bo'lgan son oyladim toping ")
    taxminiy_son = random.randint(1,x)
    taxminlar_soni = 0
    while True:
        taxminlar_soni += 1
        kiritilgan_son = int(input('Son kiriting '))
        if kiritilgan_son < taxminiy_son:
            print('Men bundan kattaroq son o\'yladim')
        elif kiritilgan_son > taxminiy_son:
            print('Men bundan kichikroq son o\'yladim ')
        else:
            print('Topdingiz')
            print(f"Siz {taxminlar_soni} martada topdingiz")
            break
    return taxminlar_soni
def komp_play(x=10):
    import random
    print('Endi sizni son o\'ylash navbatingiz ')
    print('1 dan 10 gacha son o\'ylang ')
    input("O'yinni boshlash uchun hohlagan tugmangizni bosing")
    taxminlar_soni2 = 0
    quyi = 1
    yuqori = 10
    while True:
        taxminiy_son2 = random.randint(quyi, yuqori)
        taxminlar_soni2 += 1
        print(f"Men {taxminiy_son2} ni o'yladim")
        taxminiy_son_user = input("Agar topgan b'lsam t kichik bolsa - katta b'olsa + kiriting ")
        if taxminiy_son_user == '-':
            yuqori = taxminiy_son2 - 1
        elif taxminiy_son_user == '+':
            quyi = taxminiy_son2 + 1
        elif taxminiy_son_user == 't':
            print("Topdim")
            print(f"Men {taxminlar_soni2} martada topdim ")
            break
        else:
            print('Siz notogri malumot kiritdingiz')
    return taxminlar_soni2
def play(x=10):
    yana = True
    while yana:
        sontop_u = user_play(x)
        sontop_k = komp_play(x)
        if sontop_k > sontop_u:
            print("Siz yutdingiz")
        elif sontop_u > sontop_k:
            print('Men yutdim')
        else:
            print('Durrang')
        yana = int(input("Yana o'ynaysizmi ha(1) yo'q(0)"))

play()













