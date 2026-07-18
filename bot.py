import os
import logging
import discord
from discord.ext import commands
from core.config import config

###########################################################
# KAYUMI MUSIC BOT
###########################################################


TOKEN = config.token
PREFIX = config.prefix

intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix=PREFIX,
    intents=intents,
    help_command=None
)


###########################################################
# EVENTS
###########################################################

@bot.event
async def on_ready():

    print("=" * 60)
    print("        KAYUMI PREMIUM MUSIC BOT")
    print("=" * 60)

    print(f"Logged in as : {bot.user}")
    print(f"Servers      : {len(bot.guilds)}")
    print(f"Prefix       : {PREFIX}")

    print("=" * 60)

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} Slash Commands")
    except Exception as e:
        print(e)

    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name="Premium Music 🎵"
        )
    )


###########################################################
# OWNER CHECK
###########################################################

def is_owner(user_id: int):
    return config.is_owner(user_id)


###########################################################
# PREFIX COMMAND
###########################################################

@bot.command()
async def ping(ctx):

    await ctx.send(
        f"🏓 Pong! `{round(bot.latency*1000)}ms`"
    )


###########################################################
# SLASH COMMAND
###########################################################

@bot.tree.command(
    name="ping",
    description="Shows bot latency."
)
async def ping_slash(interaction: discord.Interaction):

    await interaction.response.send_message(
        f"🏓 Pong! `{round(bot.latency*1000)}ms`"
    )


###########################################################
# START
###########################################################

bot.run(TOKEN)
