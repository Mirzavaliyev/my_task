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
#





