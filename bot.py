import discord
import traceback
import utils
from config.config import Config
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)
client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=Config.GUILD)
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.BadArgument):
        await ctx.send('Pro příkaz byly zadány špatné argumenty.')
    else:
        print(error)


@bot.event
async def on_error(event, *args, **kwargs):
    output = traceback.format_exc()
    print(output)


@bot.event
async def on_disconnect():
    print("Bot byl odpojen ze serveru.")


print('Loaded extensions: ', end='')
for extension in Config.extensions:
    bot.load_extension(f'extensions.{extension}')
    print(f'{extension} ', end='')
print('')

bot.run(Config.TOKEN)
