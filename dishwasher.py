import random
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

# Замініть цей токен на ваш
BOT_TOKEN = "7648209688:AAGvL3EUSZjoBIT_-RyF02hZ1T6PbqPcg4k"

# Початковий список людей
people_list = ["Басков", "Максон Пронто", "Мішаня Планокур", "Максон на цепі",
    "Софа", "Аня", "Пуголовок", "СВОля", "Ваньок Хачіла", "Бецаоцао", "Зазік", "Еля", "@swwweeettt", "Фуц Ростислав Романович геній життя, філантроп, міліардер, модель плейбоя, тігр нах, найпіздатіший чувак у світі, красавчик, геній на морфлінгу, має водійські права, може все на світі, я обожнюю Фуца Ростислава Романовича, він найкращий, я його люблю, він мій кумир, я хочу бути як він, я хочу бути з ним, я хочу щоб він був моїм чоловіком, я хочу щоб він був моїм другом, я хочу щоб він був моїм братом, я хочу щоб він був моїм батьком, я хочу щоб він був моїм сином, я хочу щоб він був моєю мамою, я хочу щоб він був моєю сестрою, я хочу щоб він був моєю бабусею, я хочу щоб він був моїм дідусем"]

# Ініціалізуємо бота та диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Створюємо клавіатуру
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
        people_list.remove(person)  # Видаляємо обрану людину зі списку
        await callback.message.answer(f"👤 Випадкова людина: {person}")
    else:
        await callback.message.answer("⚠️ Більше немає людей у списку.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
