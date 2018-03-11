from telegram import Message, Update, Bot, User
from telegram import MessageEntity
from telegram.ext import Filters, MessageHandler, run_async

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler, DisableAbleRegexHandler

@run_async
def nou(bot: Bot, update: Update):
    msg = update.effective_message
    reply_text = msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    reply_text("NoNoU")

@run_async
def vincent(bot: Bot, update: Update):
    update.effective_message.reply_text("Fuck u, Vincent")

__help__ = """
 - /nou: says NoU
"""

__mod_name__ = "NoU"

NOU_HANDLER = DisableAbleCommandHandler("nou", nou)
VINCENT_HANDLER = DisableAbleCommandHandler("vincent", vincent)

dispatcher.add_handler(NOU_HANDLER)
dispatcher.add_handler(VINCENT_HANDLER)