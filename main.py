import discord
from discord.ext import commands
import os
import webserver

TOKEN = os.environ['discordkey']

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# IDs
AUTO_ROLE_ID = 1402933083484721242
USER_COUNT_CHANNEL_ID = 1402937963800957089

@bot.event
async def on_ready():
    print(f'Online: {bot.user}')

@bot.event
async def on_member_join(member):
    guild = member.guild

    role = guild.get_role(AUTO_ROLE_ID)
    if role:
        try:
            await member.add_roles(role)
            print(f"Erfolgreich")
        except Exception as e:
            print(f"Error {e}")
    else:
        print("Error.")

    channel = guild.get_channel(USER_COUNT_CHANNEL_ID)
    if channel:
        try:
            new_name = f"📱・𝑼𝑺𝑬𝑹: {guild.member_count}"
            await channel.edit(name=new_name)
            print(f"Erfolgreich: {new_name}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Error.")

webserver.keep_alive()

bot.run(TOKEN)
