from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.PersonalData import PersonlaData

@dp.message_handler(Command("form"), state=None)
async def enter_test(message: types.Message):
    await message.answer('Enter Full name >> ')
    await PersonlaData.fullname.set()

@dp.message_handler(state=PersonlaData.fullname)
async def answer_fullaname(message: types.Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {'name': fullname}
    )

    await message.answer("Enter Your Email")

    await PersonlaData.next()
@dp.message_handler(state=PersonlaData.email)
async def answer_email(message: types.Message, state: FSMContext):
    email = message.text

    await state.update_data(
        {"email" : email }
    )






    date = await state.get_data()
    name = date.get("name")
    email = date.get("email")
    phone = date.get("phone")

    msg = "Quydagi malumotlar qul qilindi: '\n"
    msg += f"Ism: {name}\n"
    msg += f"Email - {email}\n"
    msg += f"Phone: - {phone}"
    await message.answer(msg)

    await state.finish()
