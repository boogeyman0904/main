from aiogram import Router, Dispatcher, Bot
from aiogram.types import Message, User
from aiogram.filters.text import Text
from aiogram.filters.command import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from asyncio import run
from aiogram import F
from aiogram.types.dice import Dice, DiceEmoji
from asyncio import sleep

API = "6274173954:AAEy427uAHh5dUnihZQmSm45GCBRU_OwKS0"
class Main:
    def __init__(self) -> None:
        self.dp = Dispatcher()
        self.bot = Bot(token=API)

    async def start_hend(self, msg:Message, bot:Bot):
        ans = f"""Assalomu Aleykum hurmatli <b>{msg.from_user.full_name}</b>"""

        btn = [
            [KeyboardButton(text="Main Menu 👁‍🗨"), KeyboardButton(text="Settings ⚙️")],
            [KeyboardButton(text="Language 🌐"), KeyboardButton(text="All Users ⭕️")],
        ]

        rp = ReplyKeyboardMarkup(keyboard=btn,resize_keyboard=True,
                                 input_field_placeholder="Iltimos menuni tanlang ")
        await msg.reply(text=ans, parse_mode="HTML",reply_markup=rp)

    async def language(self, msg:Message, bot:Bot):
        lang = [
            [InlineKeyboardButton(text="UZB",callback_data="uzb"), InlineKeyboardButton(text="RU",callback_data="ru")],
            [InlineKeyboardButton(text="ARABIC",callback_data="arabic")]
        ]    

        rp = InlineKeyboardMarkup(inline_keyboard=lang)
        await msg.answer(text="Iltimos tilni tanlang nimadir nimadir",reply_markup=rp)

    async def Menu(self, msg:Message, bot:Bot):
        men = [
            [InlineKeyboardButton(text="Sevgi",callback_data="sevgi"), InlineKeyboardButton(text="Bizness",callback_data="bizness")],
            [InlineKeyboardButton(text="Hayotiy",callback_data="hayotiy"), InlineKeyboardButton(text="Boshqa",callback_data="boshqa")]
        ]
        rp = InlineKeyboardMarkup(inline_keyboard=men)
        await msg.answer(text="Yonalishni tanlang",reply_markup=rp)
        
    async def help_hend(self, msg:Message, bot:Bot):
        ans = f"""Hurmatli <b>{msg.from_user.full_name}</b>
        Bu bot hozircha hech narsa qilmaydi."""
        await msg.reply(text=ans, parse_mode="HTML")    

    async def echo(self, msg:Message, bot:Bot):
        print(msg.dict())

    async def bot_call(self, msg:Message, bot:Bot):
        await bot.send_message(chat_id=msg.from_user.id, text="Assalomu Aleykum men shu yerdaman",
                               reply_to_message_id=msg.message_id)

    #Photo yuborishda
    async def get_mag_fl(self,msg:Message, bot:Bot):
        await msg.answer(text="Siz magic filterga tushtiz")

    #Audio yuborishda
    async def get_audio(self, msg:Message, bot:Bot):
        nw_msg = await msg.reply_dice(emoji=msg.dice.emoji)
        await sleep(6)
        qiy_foy = msg.dice.value
        bot_qiy = nw_msg.dice.value
        if qiy_foy > bot_qiy:
            await msg.answer(text="Siz yutdiz")
        else:   
            await msg.answer(text="""Siz yutqazdiz""") 

    async def start(self):
        self.dp.message.register(self.start_hend, Command(commands=["start"],ignore_case=True))
        self.dp.message.register(self.help_hend, Command(commands=["help"], ignore_case=True))
        self.dp.message.register(self.language, Text(text="Language 🌐"))
        self.dp.message.register(self.Menu, Text(text="Main Menu 👁‍🗨"))
        self.dp.message.register(self.bot_call, Text(contains="bot ?",ignore_case=True))
        self.dp.message.register(self.get_mag_fl,F.text == "allo")
        self.dp.message.register(self.get_audio,F.dice)
        self.dp.message.register(self.echo)
        try:
            await self.dp.start_polling(self.bot)
        except Exception as e:
            await self.bot.session.close()

if __name__ == "__main__":
    mn = Main()
    run(mn.start())            