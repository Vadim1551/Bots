from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from parser.classes import Person
from parser.methods import Methods
from keyboards.client_kb import Keyboards

bot = Bot('5308944947:AAFpoBXAgHjKfAZco4pVmb59KhCerXJ3qtY')
dp = Dispatcher(bot)
md = Methods()
hero = Person()
keyboards = Keyboards()