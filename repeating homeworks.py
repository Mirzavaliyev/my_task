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
