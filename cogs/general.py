import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="bonjour", description="Le bot te dit bonjour")
    async def bonjour(self, ctx):
        await ctx.send(f"Bonjour {ctx.author.mention}!")

async def setup(bot):
    await bot.add_cog(General(bot))