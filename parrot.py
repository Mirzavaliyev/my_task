# # # While loop
# # message = input("Enter your message and I will repeat ")
# # print(message)
# prompt = "Say something and I will return your sentence"
# message = ""
# while message != "quit":
#     message = input(prompt)
# #     print(message)
# prompt = "Hi give me sentence and I will give you that again"
# prompt += "\n Write here"
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
# #         print(message)
# numbers = 0
# while numbers < 10:
#     numbers += 1
#     if numbers % 2 == 0:
#         continue
# print(numbers)
# prompt = "You can choose any type of pizza and I send them to chef"
# prompt += "\nWrite name of pizza "
# message = True
# while message:
#     messsage = input(prompt)
#     if message == 'quit':
#         break
#     print(messsage)
# while True:
#     number = int(input("Enter a number: "))
#     if number <= 3:
#         print(f"The ticket free for you")
#     elif number > 3 and number <= 12:
#         print(f"The ticket 10$ for you")
#     else:
#         print(f"The ticket 20$ for you")
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)
# responses = {}
# polling_active = True
# while polling_active:
#     name = input("What is your name? ")
#     mountin = input("What is your favorite mountin? ")
#     responses[name] = mountin
#     repeat = input('Do you want to poll another person? Yes/No')
#     if repeat == 'No':
#         polling_active = False
# for name, response in responses.items():
#     print(f"Hi {name} your favorite mountin: {mountin}")
# senediwiches = ['tuna','salom','alik','qahramon','ishtiyoq','pastrami','pastrami','pastrami']
# # fineshed_sendiwiches = []
# # while senediwiches:
# #     current_senediwiches = senediwiches.pop(0)
# #     print(f"I made your {current_senediwiches}")
# #     fineshed_sendiwiches.append(current_senediwiches)
# # for sendwich in fineshed_sendiwiches:
# #         print(sendwich)
# while 'pastrami' in senediwiches:
#     senediwiches.remove('pastrami')
# print(senediwiches)


