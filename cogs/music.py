import discord
from discord.ext import commands


class Music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(
        name="play",
        description="Play a song from YouTube."
    )
    async def play(self, interaction: discord.Interaction, query: str):
        await interaction.response.send_message(
            f"🔍 Searching for: **{query}**"
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(Music(bot))
