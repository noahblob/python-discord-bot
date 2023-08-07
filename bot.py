import discord
import responses

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    username = str(message.author.name)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f'{username} said: {user_message} ({channel})')

    if user_message.startswith('?'):
        user_message = user_message[1:]
        await send_message(message, user_message, is_private=True)
    else:
        await send_message(message, user_message, is_private=False)

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTEzODA0NjM4OTgzODk1NDU5OQ.GUjqjI.AIv4jlniMq3hLuXyjHT498ZykzFVVk9ygSirFo'
    client.run(TOKEN)