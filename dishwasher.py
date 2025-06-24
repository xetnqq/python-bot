import random
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

BOT_TOKEN = "7558487345:AAEHudv63UjBPaBkgUoRCM8_6TrrsnOcb8k"

people_list = [
    "Басков", "Максон Пронто", "Мішаня Планокур", "Максон на цепі",
    "Софа", "Аня", "Пуголовок", "СВОля", "Ваньок Хачіла", "Бецаоцао", "Зазік", "Еля", "@swwweeettt",
    "Фуц Ростислав Романович геній життя, філантроп, міліардер, модель плейбоя, тігр нах, найпіздатіший чувак у світі, у нього є тачки бакси яхти особняки, я хоть і бот, але розумію на скільки ростислав піздатий і краще нього не знайти, він як молнія маквін, він як тиранозавр рекс нах, легенда просто"
]

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🎲 Вибрати людину", callback_data="choose_person")]
    ]
)

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "Вибираєм в кого мама шлюха і хто миє посуд!",
        reply_markup=keyboard
    )

@dp.callback_query(F.data == "choose_person")
async def choose_person_handler(callback: types.CallbackQuery):
    if people_list:
        person = random.choice(people_list)
        await callback.message.answer(f"👤 Випадкова людина: {person}")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
