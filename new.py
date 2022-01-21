def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "- " + json_data[0]['a']
  return(quote)



swear_words = ["fuck", "shit"]
greetings = ["$hi", "$hello", "$yo", "$hey" ]
regreets = ["sup?", "yo dawg", "hiya", "heyaa"]







@bot.event
async def on_message(message):
  for s in swear_words:
    if str(s) in message.content.lower():
      await message.delete()
      await message.channel.send(f'Dont swear {message.author.mention}')

  for g in greetings:
    if message.content.startswith(g):
      r = random.choice(regreets)
      await message.channel.send(r)

  if message.content.startswith("$motivate"):
    quote = get_quote()
    await message.add_reaction("💪")
    await message.channel.send(quote)