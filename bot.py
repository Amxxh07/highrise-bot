from highrise import BaseBot, Highrise
import os

class Bot(BaseBot):

    async def on_start(self, session_metadata):
        print("Bot connected!")

bot = Bot()

if __name__ == "__main__":
    room_id = os.getenv("65d9f3af863dc01805999f2c")
    token = os.getenv("23db108357bc3d0ebe4bea1264d2636b37d1c969a77aabfe72c42a768a17fc02")

    highrise = Highrise(bot)
    highrise.run(room_id, token)
