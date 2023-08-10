import os

from dotenv import load_dotenv
from discord import Intents, utils
from discord.ext import commands
from Cogs import soulcup

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

INTENTS = Intents.all()

bot = commands.Bot(command_prefix="!", intents=INTENTS)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord !')
    await bot.add_cog(soulcup.SoulCup(bot))
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

bot.run(TOKEN)