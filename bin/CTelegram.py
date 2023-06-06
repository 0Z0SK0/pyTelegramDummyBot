import CConfig
import CCommands
import CFunctions
import CDatabase

from aiogram import *
from aiogram.types import FSInputFile

class CTelegram():
    handle = Bot(CConfig.CConfig().getAPIKey(), parse_mode="HTML")

    async def start(self):
        self.router = Router()
        self.dp = Dispatcher()
        self.dp.include_router(self.router)
        
        @self.router.message()
        async def _handleMessage(message):
            await self.handleMessage(message)

        @self.router.callback_query()
        async def _handleCallback(callback_query: types.CallbackQuery):
            await self.handleCallback(callback_query)

        await self.dp.start_polling(self.handle)

    async def handleCallback(self, query: types.CallbackQuery):
        chat_id = query.message.chat.id
        message_id = query.message.message_id
        user = await CDatabase.CDatabase().query(f"SELECT * FROM `users` WHERE `chat_id` = '{chat_id}'")
        callback = query.data
        if user and callback == "start":
            await eval(f"CFunctions.CFunctions()._profile({chat_id}, {message_id})")
        else:
            print(callback)
            await eval(f"CFunctions.CFunctions().{callback}({chat_id}, {message_id})")

    async def handleMessage(self, message):
        user = await CDatabase.CDatabase().query(f"SELECT * FROM `users` WHERE `chat_id` = '{message.chat.id}'")
        if user and message.text == "/start":
            await CCommands.CCommands().interpret("/profile", message.chat.id, message.message_id)
        else:
            await CCommands.CCommands().interpret(message.text, message.chat.id, message.message_id)

    async def sendMessage(self, chat_id, text, reply_markup=None):
        await self.handle.send_message(chat_id, text, reply_markup=reply_markup)

    async def editMessage(self, chat_id, message_id, text, reply_markup=None):
        await self.handle.edit_message_text(text, chat_id, message_id, reply_markup=reply_markup)

    async def sendPhoto(self, chat_id, filepath, caption, reply_markup=None):
        media = FSInputFile(filepath)
        await self.handle.send_photo(chat_id, photo=media, caption=caption, reply_markup=reply_markup)

    async def deleteMessage(self, chat_id, message_id):
        await self.handle.delete_message(chat_id, message_id)