from dotenv import load_dotenv
load_dotenv()
import os
import discord
from scraper import MusinsaAPI
#---Discord 봇 기본설정----
intents = discord.Intents.default()
intents.messages_content=True #메시지 내용을 읽어오기 위한 권한설정
client = discord.client(intents=intents)
#Disscord 클라이언트 인스턴스 생성
#---메시지 생성 디스플레이 화면(개발자) 헬퍼함수---#
def build_message(item):
    embed=discord.Embed(type="rich",title=item["name"],url=item["linkurl"])
    embed.set_thumbnail(url=item["imageUrl"])    
    embed.description=item["brand"]
    embed.add_field(name="정가",value=item["normalPrice"],inline=True)
    embed.add_field("할인가",value=item["saleprice"],inline=True)
    return embed
