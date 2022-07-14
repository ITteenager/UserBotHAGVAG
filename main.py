from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import config as cfg
import random
 
import time
from time import sleep
from keep_alive import keep_alive

keep_alive() 

api_id = 17899889
api_hash = "89da681d42f98b7ceb90b53ae458ca77"

app = Client("my_account", api_id = api_id, api_hash = api_hash)

@app.on_message(filters.command("help", prefixes=".") & filters.me)
def help(_, msg):
    msg.reply("<b>😈 <a href='https://t.me/Fsure123'>Hagi Vage USER BOT</a> 😈</b>\n\n<code>.type1</code> - send msg per 30 sec\n<code>.type2</code> - send msg per 1 min\n<code>.type3</code> - send msg per 5 mins\n<code>.type4</code> - send msg per 10 mins\n<code>.type5</code> - send msg per 20 mins\n<code>.type6</code> - send\n<code>.ghoul</code> - 1000-7 TbI Ghoul")

@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text[6:]
    cfg.tm = "1"
    msg.edit(orig_text)
    while cfg.tm == "1":
        time.sleep(1)
        msg.reply(orig_text)

@app.on_message(filters.command("stop", prefixes=".") & filters.me)
def stop(_, msg):
    cfg.tm = "0"
    msg.reply("STOPPED ⛔ || DEVELOPER: Fsure123")

@app.on_message(filters.command("type1", prefixes=".") & filters.me)
def type1(_, msg):
    orig_text = msg.text[7:]
    cfg.tm = "1"
    msg.edit(orig_text)
    while cfg.tm == "1":
        time.sleep(30)
        msg.reply(orig_text)

@app.on_message(filters.command("type2", prefixes=".") & filters.me)
def type2(_, msg):
    orig_text = msg.text[7:]
    cfg.tm = "1"
    msg.edit(orig_text)
    while cfg.tm == "1":
        time.sleep(60)
        msg.reply(orig_text)

@app.on_message(filters.command("type3", prefixes=".") & filters.me)
def type3(_, msg):
    orig_text = msg.text[7:]
    cfg.tm = "1"
    msg.edit(orig_text)
    while cfg.tm == "1":
        time.sleep(300)
        msg.reply(orig_text)

@app.on_message(filters.command("type4", prefixes=".") & filters.me)
def type4(_, msg):
    orig_text = msg.text[7:]
    cfg.tm = "1"
    msg.edit(orig_text)
    while cfg.tm == "1":
        time.sleep(600)
        msg.reply(orig_text)

@app.on_message(filters.command("type5", prefixes=".") & filters.me)
def type5(_, msg):
    orig_text = msg.text[7:]
    cfg.tm = "1"
    msg.edit(orig_text)
    while cfg.tm == "1":
        time.sleep(1200)
        msg.reply(orig_text)

@app.on_message(filters.command("type6", prefixes=".") & filters.me)
def type6(_, msg):
    orig_text = msg.text[7:]
    cfg.tm = "1"
    msg.edit(orig_text)
    while cfg.tm == "1":
        time.sleep(3600)
        msg.reply(orig_text)
        
# ГУЛИХА ХАГИ
@app.on_message(filters.command("ghoul", prefixes=".") & filters.me)
def hgoul(_, msg):
    i = 1000
    while i > 62:
        try:
            text = f'{i} - 7 = {i-7}'
            for j in range(1,10):
                text += f'\n{i-7*j} - 7 = {i-7*(j+1)}'
            msg.edit(f'`{text}`')
            time.sleep(0.2)
        except FloodWait as e:
            sleep(4)

        i -= 7

app.run()