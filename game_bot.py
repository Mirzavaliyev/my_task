from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram import F

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import random
import asyncio

# Bot tokenini kiriting
API_TOKEN = "7840981516:AAEqJNWYSMGXQT1sSgOaZHYCOgCyRkKBVG4"

# Bot va dispatcher ob'ektlari
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


# Foydalanuvchi o'yini uchun davlatlar
class GameStates(StatesGroup):
    waiting_for_guess = State()

# Har bir foydalanuvchi uchun o'yin ma'lumotlari
user_data = {}

# /start komandasi uchun handler
@router.message(F.text == "/start")
async def send_welcome(message: Message):
    await message.answer(
        "Salom! Son topish o'yiniga xush kelibsiz! \n"
        "1. Agar men o'ylagan sondan kichikroq desangiz, - ni yuboring.\n"
        "2. Agar men o'ylagan sondan kattaroq desangiz, + ni yuboring.\n"
        "3. To'g'ri topsangiz, t ni yuboring.\n"
        "O'yinni boshlash uchun /play yozing."
    )

# /play komandasi uchun handler
@router.message(F.text == "/play")
async def start_game(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_data[user_id] = {
        "number": random.randint(1, 10),  # O'ylangan son
        "attempts": 0                    # Urinishlar soni
    }
    await message.answer("1 dan 10 gacha bo'lgan son o'yladim. Topishga harakat qiling!")
    await state.set_state(GameStates.waiting_for_guess)

# Foydalanuvchi javoblarini qayta ishlash
@router.message(GameStates.waiting_for_guess)
async def handle_guess(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_input = message.text

    if user_id not in user_data:
        await message.answer("Iltimos, /play yozib o'yinni qayta boshlang.")
        return

    try:
        guess = int(user_input)
    except ValueError:
        await message.answer("Iltimos, raqam kiriting.")
        return

    user_data[user_id]["attempts"] += 1
    number = user_data[user_id]["number"]

    if guess < number:
        await message.answer("Men bundan kattaroq son o'yladim.")
    elif guess > number:
        await message.answer("Men bundan kichikroq son o'yladim.")
    else:
        attempts = user_data[user_id]["attempts"]
        await message.answer(f"Tabriklayman! Siz {attempts} urinishda to'g'ri topdingiz!")
        del user_data[user_id]
        await state.clear()

# Botni ishga tushirish
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
