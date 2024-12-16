# print(' "Nexiya" , "Tiko" \' Damas \' Ko\'rganlar qilar havas')

# print(f'5 4 darajasini {5**4}')
# # print(f'22 ni 4ga bo\'lgandagi qoldiq {22 // 4}')
# print(f"Tomonlari 125 ga teng kvadratning yuzi {125 * 125} perimetri {125 * 4}")
# print(f" Diametri 12 ga teng bo'lgan doiraning yuzini {3.14 * 12**2} ")
# list_friends = ['Jasur', 'Bahodir', 'Olim']
# print(f"Salom {list_friends[0]}")
# print(f"Choyxonaga borasami {list_friends[1]}")
# # print(f"Sen meni do\'stim {list_friends[2]}")
# t_shaxslar = ['Bobur', 'Temur', 'Alisher']
# z_shaxslar = ['Imron', 'Javohir', 'Qizlarxon']
# print(f"Tarixiy odam {t_shaxslar.pop(0)}")
# print(f"Zamonaviy odam {z_shaxslar.pop(1)}")

# friends = []
# friends.append('Shaxzamon')
# friends.append(8)
# friends.remove('Shaxzamon')
# print(friends)
# friends = ['Bobur', 'Temur', 'Alisher']
# friends.insert(0,"Javohir")
# print(friends)
# mehmonlar = []
# friends = ['Bobur', 'Temur', 'Alisher']
# mehmonlar.append(friends.pop(1))
# print(mehmonlar)
# friends = ['Bobur', 'Temur', 'Alisher']
# # friends.sort()
# print(sorted(friends))
# fruits = ['pear','banana','apple','watermelon','lemon']
# fruits.reverse()
# print(fruits)
# numbers = list(range(1,10,3))
# print(numbers)
# sonlar = [2323, 2222, 34333,9999]
# arzon = min(sonlar)
# qimmat = max(sonlar)
# yigindi = sum(sonlar)
# print(f" Eng arzon {arzon} Eng qimmat {qimmat} Jami {yigindi}")
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# car = cars[0:5]
# print(car)
# royhat = ['Saida', 'Javohir', 'Ramzan', 'Qizlarhon', 'Kamoliddin']
# for i in royhat:
#     print(f"Salom {i} yaxshimisz?")
# bosh = []
# for i in list(range(10,15)):
#     bosh.append(i**3)
#     print(bosh)
# print(i)
# empty = []
# for i in range(5):
#     empty.append(input(f"{i+1} sevimli filimingizni kiriting"))
#     print(empty)
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for i in cars:
#     if i != 'gm':
#         print(i.title())
#     else:
# #         print(i.upper())
# foydalanuvchi = input('Ismingizni kiriting')
# if foydalanuvchi == 'Admin':
#     print(f"Salom Admin foydlanuvchilar ro\'yxatini ko\'rasizmi?")
# else:
#     print(f"Salom {foydalanuvchi}")
# lugat = {'int':'Butun son','float':'onlik son','input':'kirgazish','if':'Shart'}
# print(lugat)
# lugat = {'hello':'salom','morning':'ertalab','evening':'kechqurun','laptop':'notebuk','screen':'ekran'}
# royhat = input('So\'z kiriting ')
# if royhat in lugat:
#     print(f"{royhat} tarjimasi {lugat[royhat]}")
# else:
#     print(f"Bu so\'zni hali kiritmadik uzur")
# lugat = {'hello':'salom','morning':'ertalab','evening':'kechqurun','laptop':'notebuk','screen':'ekran'}
# for kalit, qiymat in lugat.items():
#     print(f"kalit {kalit} ")
#     print(f'qiymat {qiymat}')
#
# mahsulotlar = { # Do'kondagi mahsulotlar
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }
# # bozorlik = input('Kerakli mahsulotni yozing')
# # if bozorlik in mahsulotlar:
# #     print(f"Mahsulot bor ekan olindi")
# # else:
# #     print(f"Bu mahsulot yo\'q edi uzur")
# for mahsulot in sorted(mahsulotlar):
#     print(f"{mahsulot.title()}")
# shaxs0 = {'ism':'Alisher', 't_yil':'1936', 'ishi':'Shoir bo\'lgan'}
# shaxs1 = {'ism':'abror', 't_yil':'1970', 'ishi':'Diniy yetakchi'}
# shaxs2 = {'ism':'munisa', 't_yil':'1990', 'ishi':'Qo\'shiqchi'}
# shaxs3 = {'ism':'jahongir', 't_yil':'1992', 'ishi':'Biznesmen o\'quv markaz sohsida'}
# shaxslar = [shaxs0, shaxs1, shaxs2, shaxs3]
# for i in shaxslar:
#     print(f"{i['ism'].title()} {i['t_yil']} da tug\'ilgan va uning kasbi {i['ishi']} ")
#
# shaxs0 = {'ism':'Alisher', 't_yil':'1936', 'ishi':'Shoir bo\'lgan','asar':'hamza'}
# shaxs1 = {'ism':'abror', 't_yil':'1970', 'ishi':'Diniy yetakchi', 'asar':'hech narsa'}
# shaxs2 = {'ism':'munisa', 't_yil':'1990', 'ishi':'Qo\'shiqchi', 'asar':'yomg\'ir'}
# shaxs3 = {'ism':'jahongir', 't_yil':'1992', 'ishi':'Biznesmen o\'quv markaz sohsida', 'asar':'cambridge'}
# shaxslar = [shaxs0, shaxs1, shaxs2, shaxs3]
# for shaxs in shaxslar:
#     print(f"{shaxs['ism'].title()} {shaxs['asar'].upper()} ni yozgan")
# x = 0
# while x < 8:
#     print(x)
#     x += 1
# son = "Istalgan sonni kiriting"
# son += " men uning 3-darajasini qaytaraman "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(son)
#     if qiymat != 'exit':
#         print(f"{int(qiymat)} ning 3-darajasi {int(qiymat)**3}")
# son = 'Biror son kiriting '
# flag = True
# while flag:
#     qiymat = input(son)
#     if qiymat == 'exit':
#         flag = False
#     elif not qiymat.isdigit():
#         print("Faqat son kiriting")
#     else:
#         print(f'{int(qiymat)} ning kvadrati {int(qiymat)**2}')

# flag = True
# while flag:
#     kitob = input("Yaxshi korgan kitoblaringizni kiriting ")
#     if flag == 'stop':
#         break
#     print(f"Sizning yaxshi korgan kitobingiz {kitob}")

# flag = True
# while flag:
#     gap = "Yoshingizni kiriting "
#     yosh = input(gap)
#     if yosh == 'exit' or yosh == 'quit':
#         break
#     yosh = int(yosh)
#     if yosh <= 7:
#         print('Siz uchun bilet 2000')
#     elif yosh > 7 and yosh <= 18:
#         print('Siz uchun bilet 5000')
#     elif yosh > 18 and yosh <= 65:
#         print('Siz uchun bilet narxi 10000')
#     else:
#         print('Siz uchun bilet bepul')
# gap = "Mahsulot nomini yozing "
# while True:
#     bosh = []
#     stop = 'stop'
#     buyurtma = input(gap)
#     if stop == buyurtma:
#         print("Siz jarayonni to'xtatdingiz")
#         break
#     else:
#         bosh.append(buyurtma)
#     for i in bosh:
#         print(f"{i}")
# gap = "Maxsulot nomi "
# while True:
#     stop = "stop"
#     bosh = {}
#     maxsulot = input(gap)
#     narx = input('Narx yozing ')
#     if stop == maxsulot:
#         print('siz jarayonni toxtatdingiz')
#         break
#     else:
#         bosh[maxsulot] = 'narx'
#     print(bosh)
# def t_yil(ism, yosh):
#     """Bu tug'ilgan yilni hisoblovchi dastur"""
#     print(f"Salom {ism} {2024-yosh}")
# t_yil('Shavkatjon', 1336)
# def kv_kub(son):
#     '''Bu funksiya sonni 2 va 3 - darajalarini qaytaradi'''
#
#     print(f"{son} ning kvadrat {son**2} kubi {son**3}")
# son1 = int(input('Son kiriting '))
# # kv_kub(son1)
# def toq_juft(son):
#     if son % 2 == 0:
#         print('Bu son juft')
#     else:
#         print('Bu son toq')
# son1 = int(input('Son kiriting '))
# toq_juft(son1)
# def lugat_yasa(ism, familya, t_yil, phone=''):
#     lugat = {
#         'ism':ism,
#         'familya':familya,
#         't_yil':t_yil,
#         'phone':phone
#     }
#     print(lugat)
# lugat_yasa('Shavkatjon', 'Mirzavaliyev', '19980', '945034500')
# lugat_yasa('Shavkatjon', 'Mirzavaliyev', '19980')
# from datetime import datetime
#
#
# def get_user_info(name, surname, birth_year, birth_place, email=None, phone=None):
#     """
#     Foydalanuvchidan ma'lumotlarni qabul qilib, lug'at qaytaradi.
#     """
#     current_year = datetime.now().year
#     age = current_year - birth_year
#
#     return {
#         "name": name,
#         "surname": surname,
#         "birth_year": birth_year,
#         "birth_place": birth_place,
#         "email": email,
#         "phone": phone,
#         "age": age
#     }
#
#
# clients = []  # Mijozlar ro'yxati
#
# while True:
#     print("\nYangi foydalanuvchi ma'lumotlarini kiriting (to'xtash uchun 'exit' deb yozing):")
#     name = input("Ismi: ")
#     if name.lower() == 'exit':
#         break
#
#     surname = input("Familiyasi: ")
#     birth_year = int(input("Tug'ilgan yili (masalan, 1990): "))
#     birth_place = input("Tug'ilgan joyi: ")
#     email = input("Email manzili (ixtiyoriy): ") or None
#     phone = input("Telefon raqami (ixtiyoriy): ") or None
#
#     user_info = get_user_info(name, surname, birth_year, birth_place, email, phone)
#     clients.append(user_info)
#
# print("\nMijozlar ro'yxati:")
# for idx, client in enumerate(clients, start=1):
#     print(f"\nMijoz {idx}:")
#     for key, value in client.items():
#         print(f"{key.capitalize()}: {value}")
#
# def pul_ber(ismlar):
#     lugat = {}
#     while ismlar:
#         ism = ismlar.pop()
#         pul = input(f'{ism}ga qancha pul berasiz ')
#         lugat['ism'] = pul
#     return lugat
# talabalar = ['Ali', 'Vali', 'Shaxnoz', 'Hasan']
# lugat = pul_ber(talabalar)
# print(lugat)
#
# def make_title(words):
#     empty_list = []
#     while True:
#         empty_list.append(words)
#     return empty_list
# words = input('Soz kiriting ')
# print(words)
# import math as m
# x = 36
# sqrt = m.sqrt(x)
# print(f"{x} ning kvadrat ildizi {int(sqrt)}")
# import math
# angle = math.radians(180)
# sin_angle = math.sin(angle)
# cos_angle = math.cos(angle)
# tan_angle = math.tan(angle)
# print(f"Sinus 30 gradusda {sin_angle} \n Cosinus 30 gradusda {cos_angle} \n Tangens 30 gradusda {tan_angle}")
# import math
# x = 3
# uzunlik = math.pi*2*x
# yuzi = 2*math.pi*x**2
# print(uzunlik, yuzi)
# from datetime import datetime
#
# # Hozirgi vaqtni formatlash
# current_time = datetime.now()
# formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
# print(f"Formatlangan vaqt: {formatted_time}")
# import calculyator
# x = int(input('1-son '))
# y = int(input('2-son '))
# calculyator.qoshish(x, y)
# import calculyator
# x = int(input('1-son '))
# y = int(input('2-son'))
# calculyator.multiply(x, y)








