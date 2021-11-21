import discord
import requests
import json
import random

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "sadd", "ugh", "bad", "godd", "F",
             "tiring", "leave me alone", "so bad", "bad",
             "brokenhearted", "cast down", "crestfallen", "dejected", "despondent", "disconsolate",
             "doleful", "downcast", "downhearted", "down in the mouth", "droopy", "forlorn", "gloomy", "glum",
             "hangdog", "heartbroken", "heartsick", "heartsore", "heavyhearted", "inconsolable", "joyless",
             "low-spirited",
             "melancholic", "melancholy", "mourn", "mournful", "saddened", "sorrowful", "sorry", "unhappy", "woebegone",
             "woeful", "wretched"]

starter_encouragements = [
    "Cheer up!",
    "Hang in there.",
    "You are a great person / bot!",
    "Don't worry, you got this!",
    "There's nothing you can't handle!",
    "Trust me, you've got this.",
    "Don't give up, you're almost there!",
    "Give it a try. You got this!",
    "Go for it.",
    "Why not? Give it a try.",
    "It’s worth a shot.",
    "What are you waiting for? Lets give it a try!!",
    "What do you have to lose? Give it a try!",
    "You might as well give it a shot.",
    "Just do it. You got this.",
    "There you go!",
    "Keep up the good work.",
    "Keep it up.",
    "Good job.",
    "Hang in there, it gets worse.",
    "I’m so proud of you!",
    "Keep pushing.",
    "Stay strong.",
    "Never give up.",
    "Come on! You can do it!.",
    "I’ll support you either way.",
    "Follow your dreams.",
    "Reach for the stars.",
    "Do the impossible.",
    "Believe in yourself.",
    "The sky is the limit."
]

bot_commands = "**Welcome to ManaBOT help.** \n\nThe following bot commands are available as of now:\n" \
               "```1.\\bitcoin: Displays the most recently updated bitcoing rates in USD.\n" \
               "2.\\bored: Suggests ideas/tasks to perform when you're bored.\n" \
               "3.\cat: Keep trying, you might end up getting a cat picture.\n" \
               "4.\dog: Doggo is lob. Get yourself a good tsunami of dogoo pictures.\n" \
               "5.\hello: ManaBOT says hello when you use this command.\n"\
               "6.\help: Bot commands help menu.\n"\
               "7.\ip: Displays your public IP Address\n" \
               "8:\iss: Displays the current location of the ISS (In terms of latitude and longitude)\n" \
               "9.\meme: Get yourself a good dose of memes.\n"\
               "10.\ping: Checks if the bot is online.\n"\
               "11.\quote: Displays inspirational quotes on every use.```"

count = 0


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_member_join(member):
    await member.send("Welcome to the server {}! Make sure you have fun !! For roles, contact @BossMan".format(member))


@client.event
async def on_message(message):

    global count
    if message.author == client.user:
        return

    msg = message.content

    if msg == '\hello':
        await message.channel.send('Hello @{}, Hope you are keeping well !!'.format(message.author))

    if msg == '\quote':
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " -" + json_data[0]['a']
        await message.channel.send(quote)

    if msg == '\help':
        await message.channel.send(bot_commands)

    if msg == '\meme':
        content = requests.get("https://meme-api.herokuapp.com/gimme").text
        data = json.loads(content, )
        meme = discord.Embed(title=f"{data['title']}", Color=discord.Color.random()).set_image(url=f"{data['url']}")
        await message.channel.send(embed=meme)

    if msg.startswith('\cat'):
        await message.channel.send("Sorry. **We don't do that here.**")

    if msg == '\ping':
        count += 1
        if count > 2:
            await message.channel.send("ENOUGH OF YOUR PINGS !!")
        else:
            await message.channel.send("{} pong!".format(message.author))

    if msg.startswith('\dog'):
        content = requests.get("https://dog.ceo/api/breeds/image/random").text
        data = json.loads(content, )
        dog_pic = discord.Embed(Color=discord.Color.random()).set_image(url=f"{data['message']}")
        await message.channel.send(embed=dog_pic)

    if msg == '\iss':
        response = requests.get("http://api.open-notify.org/iss-now.json")
        json_data = json.loads(response.text)
        iss_locn = "Latitude: **" + json_data['iss_position']['latitude'] + "**   Longitude: **" + json_data['iss_position']['longitude'] + "**"
        await message.channel.send(iss_locn)

    if msg == '\\bitcoin':
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        json_data = json.loads(response.text)
        bitcoin_prc = "Current Price: **" + json_data['bpi']['USD']['rate'] + " USD**   Last Updated: **" + json_data['time']['updated'] + "**"
        await message.channel.send(bitcoin_prc)

    if msg == '\\bored':
        response = requests.get("https://www.boredapi.com/api/activity")
        json_data = json.loads(response.text)
        bored_activity = "Hmm, lemme think. I'd say **" + json_data['activity'] + "**"
        await message.channel.send(bored_activity)

    if msg == '\ip':
        response = requests.get("https://api.ipify.org/?format=json")
        json_data = json.loads(response.text)
        ip_addrs = "Your Public IP Address: **" + json_data['ip'] + "**"
        await message.channel.send(ip_addrs)

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

client.run("BOT ID")
