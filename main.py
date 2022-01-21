import discord
from discord.ext import commands
import random
import os
import requests
import json
from replit import db
from keep_alive import keep_alive
my_secret = os.environ['token']


bot = commands.Bot(command_prefix = ">")


swear_words = []
greetings = ["$hi", "$hello", "$yo", "$hey", "$friday", "$friday you there?" ]
regreets = ["sup?", "yo dawg", "hiya", "heyaa"]
ynn = ["Yep", "Yes", "Oh yeah","Totally", "Maybe", "Not at all", "Nope", "Nah", "No", "I'm not sure", "I'm afraid I dont know"]
chance = [1, 2, 3]





def get_apod():

  apod = requests.get("https://api.nasa.gov/planetary/apod?api_key=wbN80x81gRtITPNpzkdluXmycNbeFejZRBGSlcH6")

  data = apod.json()
  exp = data["explanation"]
  image = data["hdurl"]
  stuff = [image, exp]
  return(stuff)


def get_insult():
  fact = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")

  insult = fact.json()

  ins = insult["insult"]
  return(ins)



def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "- " + json_data[0]['a']
  return(quote)



def dog_img():
  img = requests.get("http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true")
  photo = img.json()
  return(photo[0])



def cat_img():
  img = requests.get("http://shibe.online/api/cats?count=1&urls=true&httpsUrls=true")
  photo = img.json()
  return(photo[0])



def bird_img():
  img = requests.get("http://shibe.online/api/birds?count=1&urls=true&httpsUrls=true")
  photo = img.json()
  return(photo[0])




@bot.command()
async def hlp(ctx):
  await ctx.send(msg)





@bot.command()
async def dogpic(ctx):
  photo = dog_img()
  await ctx.send(photo)



@bot.command()
async def catpic(ctx):
  photo = cat_img()
  await ctx.send(photo)



@bot.command()
async def birdpic(ctx):
  photo = bird_img()
  await ctx.send(photo)


@bot.command()
async def apod(ctx):
  stuff = get_apod()
  await ctx.send(stuff[0])
  await ctx.send(stuff[1])






@bot.command()
async def poll(ctx,*,msg):
  channel = ctx.channel
  try:
    op1 , op2 = msg.split("/")
    text = f'''
    🅰 {op1}

    🅱 {op2}
    '''
   
  except:
    await channel.send("Please type in the format - >poll [Option A]/[Option B]")
    return

  em = discord.Embed(title = "Poll", description = text, colour = discord.Colour.purple())
  message = await channel.send(embed = em)
  await message.add_reaction("🅰")
  await message.add_reaction("🅱")
  await ctx.message.delete()

  



@bot.event
async def on_ready():
  print("status - online")
  await bot.change_presence(status=discord.Status.dnd, activity = discord.Activity(type = discord.ActivityType.watching, name = "over the server"))
  





@bot.event
async def on_message(message):
  await bot.process_commands(message)
  for s in swear_words:
    if str(s) in message.content.lower():
      await message.delete()
      await message.channel.send(f'Dont swear {message.author.mention}')


  for g in greetings:
    if message.content.startswith(g):
      if message.author.id == 750747055030403132:
        await message.channel.send("Yes, boss")
      else:
        r = random.choice(regreets)
        await message.channel.send(f'{r} {message.author.mention}')

  if message.content.startswith("$motivate"):
    quote = get_quote()
    await message.add_reaction("💪")
    await message.channel.send(quote)
        
  if message.content.startswith("$yn"):
    ans = random.choice(ynn)
    await message.channel.send(ans)
  
  if message.content.startswith("$welcome"):
    if message.author.id == 750747055030403132:
      await message.channel.send("Thanks, boss!")
    else:
      await message.channel.send("Thanks!")
  
  if message.content.startswith("$go"):
    if message.author.id == 750747055030403132:
      await message.channel.send("Powering down...")


  if message.content.startswith("$mai"):
    await message.channel.send("Beta, focus kar")






    







msg = "Hi! I'm Friday! I was made by uc. I can't do much yet. You can check if I'm working correctly by typing hi / hello / yo with a $ in front. For eg $hi. Also, if you type $motivate, I'll give you a random quote. New feature - type $yn and a yes or no question after that and i'll answer!! Eg - $yn do you like donuts. Have a good day!! "
















keep_alive()
bot.run(my_secret)