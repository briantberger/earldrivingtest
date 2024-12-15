import discord
import os
from dotenv import load_dotenv

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user: 
            return
    
        if message.author.name == 'waeha' and message.id % 10 == 1:
            await message.channel.send('Earl do your driving test')
            await message.channel.send('https://media.npr.org/assets/img/2011/09/14/Ryan%20Gosling%20in%20Drive_wide-d34d9ba593650d1a2bc51d3714257a31feceb9d2.jpg?s=1400&c=100&f=jpeg')

load_dotenv()

api_key = os.getenv("DISCORD_BOT_KEY")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(api_key)