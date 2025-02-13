import asyncio
from pyrogram import Client
import tgcrypto
import datetime
import time

api_id = 26350164
api_hash = "78142b6e4e89e0f0bdc93a7ebf01d6ec"

app = Client(name="my_account", api_hash=api_hash, api_id=api_id)

async def main():
    async with Client("my_account", api_id, api_hash) as app:
        prev_bio = ""
        while True:
                chat = await app.get_chat(7005378942) #her chat id is 7005378942
                bio = chat.bio or "None"
                if bio != prev_bio:
                     await app.send_message("me", f"{bio}\n{datetime.datetime.today().strftime('%H:%M %d.%m.%Y')}")
                     prev_bio = bio
                time.sleep(3)


asyncio.run(main())