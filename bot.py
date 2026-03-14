from highrise import BaseBot
from highrise.__main__ import main
import asyncio

class Bot(BaseBot):

    async def on_start(self, session_metadata):
        print("Bot connected!")

if __name__ == "__main__":
    asyncio.run(main([Bot()]))
