import os
import discord
from discord.ext import commands
from main_logic import check_flights

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"🤖 Bot connecté : {bot.user}")

@bot.command()
async def deals(ctx):
    await ctx.send("🔍 Recherche des meilleurs vols...")
    alerts = check_flights()

    if not alerts:
        await ctx.send("😕 Aucun bon plan trouvé")
    else:
        for alert in alerts:
            await ctx.send(alert)

bot.run(os.getenv("DISCORD_TOKEN"))
