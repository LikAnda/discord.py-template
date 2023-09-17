import discord
from discord.ext import commands
import logging
import asyncio
import os
import json

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")

with open("config.json", "r") as f:
    data = json.load(f)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix=data["prefix"])
async def load_extensions(): # function from kkrypt0nn
    for i in os.listdir(f"{os.path.realpath(os.path.dirname(__file__))}/cogs"):
        if i.endswith(".py"):
            extension = i[:-3]
            try:
                await bot.load_extension(f"cogs.{extension}")
                print(f"Extension cogs.{extension} chargée")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Erreur lors du chargement de l'extension {extension}\n{exception}")

@bot.event
async def on_ready():
    print(f"Le bot est connecté sous le nom: {bot.user}"
          "\n============[BOT READY]============\n")

asyncio.run(load_extensions())
bot.run(data["token"], log_handler=handler)