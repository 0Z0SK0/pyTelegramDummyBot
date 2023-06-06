import CTelegram
import CConfig
import CDatabase

import asyncio
from aiogram import *
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardMarkup, KeyboardButton

class CGeneral():
    def __init__(self, chat_id, message_id):
        self.chat_id = chat_id
        self.message_id = message_id

    async def createDialog(self, text, buttons):
        builder = None

        if len(buttons) > 0:
            builder = InlineKeyboardBuilder()
            adjust_param = ""
            for idx, i in enumerate(buttons):
                if idx == len(buttons):
                    adjust_param = adjust_param + "1"
                else:
                    adjust_param = adjust_param + "1,"

                builder.button(text=str(i[0]), callback_data=str(i[1]))
 
            if adjust_param != "":
                eval(f"builder.adjust({adjust_param})")

        try:
            await CTelegram.CTelegram().editMessage(self.chat_id, self.message_id, text, reply_markup=builder.as_markup())
        except Exception:
            await CTelegram.CTelegram().sendMessage(self.chat_id, text, reply_markup=builder.as_markup())

        

class CFunctions():
    async def _selectCategory(self, chat_id, message_id):
        await CTelegram.CTelegram().deleteMessage(chat_id, message_id)
        
        self.builder = InlineKeyboardBuilder()
        self.builder.button(text="WEB", callback_data=f"_selectCategory__web")
        self.builder.button(text="Desktop", callback_data=f"_selectCategory__desktop")
        self.builder.button(text="Mobile", callback_data=f"_selectCategory__mobile")

        # create user
        self.user = await CDatabase.CDatabase().query(f"SELECT * FROM `users` WHERE `chat_id` = '{chat_id}'")
        if not self.user:
            await CDatabase.CDatabase().query(f"INSERT INTO `users` (`chat_id`, `status`) VALUES ('{chat_id}', 1)")

        await CTelegram.CTelegram().sendMessage(chat_id, "Выберите категорию:", reply_markup=self.builder.as_markup())

    async def _startup(self, chat_id, message_id):
        await CTelegram.CTelegram().deleteMessage(chat_id, message_id)

        self.builder = InlineKeyboardBuilder()
        self.builder.button(text="Продолжить", callback_data=f"_selectCategory")
        self.builder.adjust(1,1)
        await CTelegram.CTelegram().sendPhoto(chat_id, CConfig.CConfig().getImagesDirectory() + "\\startup_1.png", "", reply_markup=self.builder.as_markup())
