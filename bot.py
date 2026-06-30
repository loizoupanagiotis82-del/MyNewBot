import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong! {round(bot.latency * 1000)}ms")

@bot.command()
async def botinfo(ctx):
    embed = discord.Embed(
        title="🤖 Bot Information",
        color=discord.Color.blurple()
    )

    embed.add_field(
        name="Latency",
        value=f"{round(bot.latency * 1000)}ms",
        inline=False
    )

    embed.add_field(
        name="Servers",
        value=str(len(bot.guilds)),
        inline=False
    )

    await ctx.send(embed=embed)

bot.run(TOKEN)
