import discord
import re
import requests

client = discord.Client()


def ConvertShortLink2Regular(url):
    res = requests.get(url)
    matchRes = re.findall(
        r"(<meta data-vue-meta=\"true\" itemprop=\"url\" content=\"(.+?)\">)", res.text)
    return matchRes[0][1]


@client.event
async def on_ready():
    print("Fuck b23.tv bot starts as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(message.content)
    pattern = re.compile(r"((https:\/\/b23\.tv)\/(.+))")
    reRes = pattern.findall(message.content)

    if len(reRes) != 0:
        for url in reRes:
            # Replace b23tv with regular url.
            originalLink = ConvertShortLink2Regular(url[0])
            msg = f"发现b23.tv短链接，获取原始链接：{originalLink}\n请使用360安全浏览器打开。"

            await message.reply(msg)

with open("discord-bot/bot-token.txt", "r") as tokenFile:
    client.run(tokenFile.read())
