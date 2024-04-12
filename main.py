import os
import discord
from discord.ext import commands
import requests
import json
import random
import asyncio
import datetime
import gemini

# from keep_alive import keep_alive


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return (quote)


forbidden = [
    "bao", "whale", "vtuber", "BAO", "Bao", "BAo", "b@o", "b40", "bAo", "bAO",
    "baO", "ba0", "3O", "3o", "b4o", "B40", "B@o", "B@O", "B4o", "B4O", "b4O"
]

token = os.environ["TOKEN"]

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='.',
                      case_insensitive=True,
                      intents=intents)
nguoihoi = 0


@client.event
async def on_ready():
  print("ready to play")


@client.event
async def on_message(msg):
  global nguoihoi
  #if msg.author.id == 990215817218129921:
  #await msg.channel.send("<@771739550606819391> Bao 🐳 tweeted a new tweet")

  if "." not in msg.content and msg.author.id != 990219099990794270:
    if "chan vai" in msg.content or "Chan vai" in msg.content:
      await msg.channel.send(
          "co tao o day roi khong sao dau <:joewaiting:987409375792627802>")
    elif ("choi " in msg.content or "Choi " in msg.content
          or "chơi " in msg.content or "Chơi " in msg.content
          or msg.content == "choi" or msg.content == "Choi"
          or msg.content == "chơi" or msg.content == "Chơi"):
      await msg.channel.send("choi me may a <:ftw:987408211890036776>")

    if (msg.content == "e" or msg.content == "E") and nguoihoi == 0:
      nguoihoi = msg.author.id
      await msg.channel.send("j cu <:joewaiting:987409375792627802>")

      def check_nguoihoi(m):
        return m.author.id == nguoihoi

      try:
        cauhoi = await client.wait_for('message',
                                       check=check_nguoihoi,
                                       timeout=60)
      except asyncio.TimeoutError:
        chui = random.randint(1, 3)
        if (chui == 1):
          await msg.channel.send(
              "suc vat goi xong de day <:joetridodai:1071285390071304223>")
        elif chui == 2 :
          await msg.channel.send(
            "goi xong deo noi j an cac a <:joetridodai:1071285390071304223>")
        else:
          await msg.channel.send(
            "dit me suc vat goi xong deo noi gi <:joetridodai:1071285390071304223>"
          )
        nguoihoi = 0

      else:
        input = str(cauhoi.content)
        tra_loi = gemini.generate_text(input)
        await msg.channel.send(tra_loi)
        nguoihoi = 0

    # elif dang_hoi == 1 and msg.author.id == nguoihoi:
    #   input = str(msg.content)
    #   tra_loi = gemini.generate_text(input)
    #   await msg.channel.send(tra_loi)
    #   nguoihoi = 0
    #   dang_hoi = 0

  # channel = client.get_channel(796362150276890627)
  # if msg.channel.id == 794193276122955781 and not msg.author.bot:
  #   embed = discord.Embed(title=f"{msg.content}")
  #   embed.set_author(name=msg.author, icon_url=msg.author.avatar_url)
  #   embed.timestamp = datetime.datetime.now()
  #   embed.set_footer(text=f"ID: {msg.id}")
  #   await channel.send(embed=embed)
  #   if len(msg.attachments) != 0:
  #     for i in range(len(msg.attachments)):
  #       await channel.send(msg.attachments[i])
  #       await asyncio.sleep(3)
  #   await asyncio.sleep(3)
  # await client.process_commands(msg)


@client.command()
async def quote(ctx):
  quote = get_quote()
  await ctx.channel.send(quote)


@client.command()
async def joke(ctx, *ten):
  self = " ".join(str(e) for e in ten) if len(ten) != 0 else ctx.author.mention
  if any(word in self for word in forbidden):
    await ctx.channel.send("khong co chuyen day dau")
    roll = -1
  else:
    roll = random.randint(0, 2)
  if roll == 0:
    await ctx.channel.send(f"me {self} beo <:ftw:987408211890036776>")
  elif roll == 1:
    await ctx.channel.send(
        f"nguoi khong lo duy nhat con ton tai la me {self} <:ftw:987408211890036776>"
    )
  elif roll == 2:
    await ctx.channel.send(f"me {self} khong beo <:ok:987574238833676298>")
    await asyncio.sleep(5)
    await ctx.channel.send(
        f"dua thoi, me {self} beo vl <:ftw:987408211890036776>")


@client.command()
async def coolcheck(ctx, *ten):
  if len(ten) != 0:
    self = " ".join(str(e) for e in ten)
  else:
    self = ctx.author.mention

  if any(word in self for word in forbidden) or "771739550606819391" in self:
    roll = 1
  else:
    roll = random.randint(0, 1)

  if roll == 0:
    await ctx.channel.send(f"No, {self} is not cool <:puke:987409216614576189>"
                           )
  elif roll == 1:
    await ctx.channel.send(f"Yes, {self} is very cool <:ok:987574238833676298>"
                           )


# keep_alive()
try:
  client.run(token)
except:
  os.system("kill 1")
