
from highrise import BaseBot, Highrise
from highrise.models import *

class Bot(BaseBot):

    async def on_start(self, session_metadata):
        print("Bot is online!")

bot = Bot()

app = Highrise(
    bot,
    "<65d9f3af863dc01805999f2c>",
    "<23db108357bc3d0ebe4bea1264d2636b37d1c969a77aabfe72c42a768a17fc02>"
)

app.run()
