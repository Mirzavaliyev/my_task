# def info():
#     """This function returns name and age"""
#     name = input("write your name")
#     age = int(input('when did you born'))
#     ages = 2024 - age
#     print(f"Hi {name} you are {ages} years old")
#
# info()
# def sq_3rd():
#     square = int(input("Write number that should be squared "))
#     rd = int(input('Write number that should be 3 times '))
#     square1 = square**2
#     rd1 = rd**3
#     print(f"sqaure is {square} 3 times is {rd1}")
# # sq_3rd()
# def greet(username):
#     print(f"Hello {username}")
# greet("Shavkat")
# def get_formatted_name(first_name,last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name
# while True:
#     print('write your full name')
#     f_name = input('Write your name')
#     l_name = input('Write your surname')
#     ff = get_formatted_name(f_name, l_name)
# print(ff)
# def info_about_person(name, surname, phone, email, age=" ", city=" "):
#     info = {'ism':name,
#             'familya':surname,
#             'phone':phone,
#             'email':email,
#             'age':age,
#             'city':city
#     }
#     return info
# print('Mijoz haqida malumot kiriting')
# mijozlar = []
# while True:
#     ism = input('Put your name ')
#     familya = input('Put your surname ')
#     phone = input('Put your phone ')
#     email = input('Put your email ')
#     age = input('Put your age (Optional) ')
#     city = input('Put your city (Optional) ')
#     mijozlar.append(info_about_person(ism,familya,phone,email,age,city))
#     quit = input('If you want to quit write Q ')
#     if quit == "Q":
#         break
#
# print('Mijozlar')
# for mijoz in mijozlar:
#     print(f"{mijoz['ism']} {mijoz['familya']} {mijoz['phone']}  {mijoz['email']} {mijoz['city']} {mijoz['age']}")
# def books(name,author,year,janr,cost=""):
#     book = {
#         'name':name,
#         'author':author,
#         'year':year,
#         'janr':janr,
#         'cost':cost
#     }
#     return book
# book_list = []
# while True:
#     name = input('Book name ')
#     author = input('Books author ')
#     year = input('Books year ')
#     janr = input('Books genre ')
#     cost = input('Books cost ')
#     book_list.append(books(name,author,year,janr,cost))
#     exit = input('Input Exit if you want to quit')
#     if exit == 'Exit':
#         break
# print('About book')
# for bookg in book_list:
#
#     print(f"Books name {bookg['name']} \n Books author {bookg['author']} \n Books year {bookg['year']} \n Books genre {bookg['janr']} \n Books cost{bookg['cost']}")
# def number():
#     number1 = int(input('Number 1 '))
#     number2 = int(input('Number 2 '))
#     number3 = int(input('Number 3 '))
#     if number1 > number2 and number1 > number3:
#         print(f"The biggest number is {number1}")
#     elif number2 > number1 and number2 > number3:
#         print(f"The biggest number is {number2}")
#     else:
#         print(f"The biggest number is {number3}")
#
# # number()
# import math
#
# def aylana_hisobla(radius):
#     """Aylananing radiusi, diametri, perimetri va yuzini lug'at ko'rinishida qaytaradi."""
#     aylana_info = {
#         'radius': radius,
#         'diametr': 2 * radius,
#         'perimetr': 2 * math.pi * radius,
#         'yuzasi': math.pi * (radius ** 2)
#     }
#     return aylana_info
#
# # Foydalanuvchidan radiusni kiritishni so'rash
# radius = float(input("Aylananing radiusini kiriting: "))
# natija = aylana_hisobla(radius)
#
# # Natijalarni chop etish
# print("\nAylana haqida ma'lumot:")
# for kalit, qiymat in natija.items():
#     print(f"{kalit.title()}: {qiymat:.2f}")
# def teskari_tartib(harflar):
#     for i in range(len(harflar)):
#         harflar[i] = harflar[i][::-1]
#     return harflar
# harf = ["hello", "world", "python"]
# harf1 = teskari_tartib(harf)
# print(harf1)











