import discord
from discord.ext import commands
from googletrans import Translator, LANGUAGES
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
translator = Translator()

@bot.event
async def on_ready():
    print(f"Bot hazır: {bot.user}")

@bot.command()
async def cevir(ctx, dil: str, *, text: str):
    dil = dil.lower()
    if dil not in LANGUAGES:
        await ctx.send("Geçersiz dil kodu")
        return
    result = translator.translate(text, dest=dil)
    await ctx.send(result.text)

bot.run(os.getenv("DISCORD_TOKEN"))
