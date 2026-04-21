import discord
import ddddocr
import requests
import asyncio
import time
import re
import os
import winsound
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
TARGET_GUILD_ID = int(os.getenv("GUILD_ID"))
TARGET_CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
BOT_AUTHOR_ID = int(os.getenv("BOT_ID"))

ocr = ddddocr.DdddOcr(show_ad=False)

class MCTiersUltimate(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.already_joined = False 

    def play_ring(self):
        try:
            for _ in range(4):
                winsound.Beep(2000, 150)
                winsound.Beep(2500, 150)
        except:
            print("\a")

    async def on_ready(self):
        print("\n" + "═"*40)
        print("        MCTIERS AUTO-JOINER ACTIVE      ")
        print("═"*40)
        print(f"User:         {self.user.name}")
        
        guild = self.get_guild(TARGET_GUILD_ID)
        channel = self.get_channel(TARGET_CHANNEL_ID)
        
        print(f"Server:       {guild.name if guild else 'Not Found'}")
        print(f"Channel:      {channel.name if channel else 'Not Found'}")
        print("═"*40)
        print("[-] STATUS: NO TESTER AVAILABLE")
        print("═"*40 + "\n")

    def get_queue_position(self, embeds):
        for embed in embeds:
            desc = embed.description or ""
            match = re.search(rf"(\d+)\.\s*<@!?{self.user.id}>", desc)
            if match:
                return match.group(1)
        return "Position pending..."

    async def attempt_join(self, message):
        if self.already_joined:
            return False

        if not message.components:
            return False

        for row in message.components:
            for child in row.children:
                if child.type == discord.ComponentType.button and "join" in (child.label or "").lower():
                    try:
                        self.already_joined = True 
                        await child.click()
                        
                        
                        self.play_ring()
                        
                        print("\n[!] JOIN SUCCESS - ALARM RINGING")
                        
                  
                        await asyncio.sleep(0.7) 
                        updated_msg = await message.channel.fetch_message(message.id)
                        pos = self.get_queue_position(updated_msg.embeds)
                        
                        print("\n" + "⭐"*20)
                        print(f"Tester Name:    {updated_msg.author.name}")
                        print(f"Timestamp:      {time.strftime('%H:%M:%S')}")
                        print(f"My Queue Pos:   {pos}")
                        print("⭐"*20 + "\n")
                        return True
                    except Exception as e:
                        self.already_joined = False 
                        print(f"[X] Click Error: {e}")
        return False

    async def on_message(self, message):
        if message.channel.id != TARGET_CHANNEL_ID or message.author.id != BOT_AUTHOR_ID:
            return
        if not self.already_joined:
            await self.attempt_join(message)
        
       
        if message.attachments:
            asyncio.create_task(self.solve_captcha(message))

    async def on_message_edit(self, before, after):
      
        if after.channel.id == TARGET_CHANNEL_ID and after.author.id == BOT_AUTHOR_ID:
            if not self.already_joined:
                await self.attempt_join(after)

    async def solve_captcha(self, message):
        try:
            img = requests.get(message.attachments[0].url).content
            solution = ocr.classification(img)
            if solution:
                await asyncio.sleep(0.5)
                await message.channel.send(solution)
                print(f"[@] Captcha Solved: {solution}")
        except:
            pass

client = MCTiersUltimate()
client.run(TOKEN)
