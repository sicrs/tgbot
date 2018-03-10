from telegram import Message, Update, Bot, User
from telegram import MessageEntity
from telegram.ext import Filters, MessageHandler, run_async

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler, DisableAbleRegexHandler

@run_async
def nou(bot: Bot, update: Update):
    update.effective_mesage.reply_text("NoNoU")

__help__ = """
 - /nou: says NoU
"""

__mod_name__ = "NoU"

NOU_HANDLER = DisableAbleCommandHandler("nou", nou)
dispatcher.add_handler(NOU_HANDLER)