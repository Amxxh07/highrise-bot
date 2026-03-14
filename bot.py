from highrise import BaseBot
from highrise.models import *

class Bot(BaseBot):

    async def on_start(self, session_metadata):
        print("Bot is online!")

bot = Bot()
