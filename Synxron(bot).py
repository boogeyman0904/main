from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command

from asyncio import run

class MyBot:
    def __init__(self) -> None:
        self.Token = ""
        self.bot = Bot(token=self.Token)
        self.yonaltiruvchi = Dispatcher()

    async def boshlash_buyrugi(self, habar:Message, bot:Bot):
        sms = "Assalomu Aleykum"
        await habar.reply(text=sms)

    async def eng_boshi(self):
        self.yonaltiruvchi.message.register(self.boshlash_buyrugi, Command(commands=["boshlash", "start"],ignore_case=True))  
        try:
            await self.yonaltiruvchi.start_polling(self.bot)
        except Exception as e:
            await self.bot.session.close()          

if __name__ == "__main__":
    mn = MyBot()
    run(mn.boshlash_buyrugi())            