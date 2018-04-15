import re

from telegram import Message, Update, Bot, User
from telegram import MessageEntity
from telegram.ext import Filters, run_async

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

@run_async
def tidy(bot: Bot, update: Update):
    message = updater.effective_message
    reply_text = re.sub(r'Pls', "Please", message.reply_to_message.text)
    message.reply_to_message_.reply_text(reply_text)

TIDY_HANDLER = DisableAbleCommandHandler("tidy", tidy)

dispatcher.add_handler(TIDY_HANDLER)