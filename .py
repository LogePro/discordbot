pip install discord.py

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

bot.user.name = 'L'

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author.bot:
        return  # Ignore messages from other bots

    if message.content.lower() == 'hi':
        await message.channel.send('Hello!')

    await bot.process_commands(message)

@bot.command(name='play')
async def play_tic_tac_toe(ctx):
    pass
    
TOKEN = 

bot.run('TOKEN')  
