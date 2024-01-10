import discord
import asyncio
import json
import sys
import time
import os
import colorful as cf
from discord.ext import commands
import random
import ctypes
import traceback
from time import sleep
import threading
import aiohttp

#shit whitelist
#counter = 0
#while counter <2:
   # print (cf.bold_red("Don't have a key? Get one from https://discord.gg/jQtFXDJ"))
   # print (cf.bold_brown("Made by ICE#5150"))
   # auth_token = input(cf.bold_green("Enter Your Key:")) 
   # print (cf.bold_yellow("Validating key please be patient....."))
   # time.sleep(1)
  #  if auth_token in {'Rosasacunt9980'}:
     #   print("Logged in Successfully")
      #  time.sleep(1)
      #  counter += 2
      #  clear = lambda: os.system('cls')
      #  clear()

   # else:
       # clear = lambda: os.system('cls')
        #clear()
        #print(cf.red("Incorrect key or Key is blacklisted"))
       # time.sleep(2)
       # clear()



ctypes.windll.kernel32.SetConsoleTitleW("AutismWare Recode V2.1")
client = discord.Client()
with open('token.json', 'r') as handle:
    token = json.load(handle)
    token = (token["token"])
with open('Autismware.json', 'r') as handle:
    Autismware = json.load(handle)
    if token == "Token_Here":
        print ("You Haven't set up the Token.json. Please set it up and then run the program again.")
        time.sleep(10)
        sys.exit()
    cleanphrase = (Autismware["cleanphrase"])
    monkey = (Autismware["monkey"])
    death = (Autismware["death"])
    spam = (Autismware["spam"])
    start = (Autismware["start"])
    game = (Autismware["game"])
    logout = (Autismware["logout"])
    watchstatus = (Autismware["watchstatus"])
    Listening = (Autismware["Listening"])
    slap = (Autismware["slap"])
    pat = (Autismware["pat"])
    help = (Autismware["help"])
    copy = (Autismware["copy"])
    cuddle = (Autismware["cuddle"])
    kiss = (Autismware["kiss"])
    hug = (Autismware["hug"])
    shoot = (Autismware["shoot"])
    stickbug = (Autismware["stickbug"])
    lewd = (Autismware["lewd"])
    fuck = (Autismware["fuck"])
    cry = (Autismware["cry"])
    clap = (Autismware["clap"])
    dice = (Autismware["dice"])
    holdhands = (Autismware["holdhands"])
    hack = (Autismware["hack"])
    dance = (Autismware["dance"])
    alienprobe = (Autismware["alienprobe"])
    nut = (Autismware["nut"])
    console = (Autismware["console"])
    consolecolors = (Autismware["consolecolors"])
    looplisten = (Autismware["looplisten"])
    guild = (Autismware["guild"])
    crash = (Autismware["crash"])
    ball = (Autismware["ball"])



cf.use_true_colors()
#print ("Whats new?")
#print ("NEW Changed Copy avatar to user Logger Now gives information about users ")
#input("Press Any key to continue")

@client.event
async def on_ready():
    cls = lambda: os.system('cls') 
    cls()
    await client.change_presence(status = discord.Status.dnd,
    activity = discord.Activity(type=discord.ActivityType.playing,
    name = "ΛЦƬIƧMЩΛЯΣ 2.3 BΣƬΛ",
    details = "Created by ICEY",))
    print (cf.bold_orange("ΛЦƬIƧMЩΛЯΣ 2.3 BΣƬΛ Created by ICEY"))

    print (cf.bold_orange("                                            ╭╮╱╱╭┳━━━╮╱╭╮"))
    print (cf.bold_orange(" ▄▀█ █░█ ▀█▀ █ █▀ █▀▄▀█ █░█░█ ▄▀█ █▀█ █▀▀   ┃╰╮╭╯┃╭━╮┃╭╯┃"))
    print (cf.bold_orange(" █▀█ █▄█ ░█░ █ ▄█ █░▀░█ ▀▄▀▄▀ █▀█ █▀▄ ██▄   ╰╮┃┃╭┻╯╭╯┃╰╮┃"))
    print (cf.bold_yellow("╔══╗────────────────╔╗╔╗───╔╗               ╱┃╰╯┃╭━╯╭╯╱┃┃"))
    print (cf.bold_yellow("╚╗╗╠═╦═╦═╦═╦╗╔═╦═╦═╦╝║║╚╦╦╗╠╬═╦═╗           ╱╰╮╭╯┃┃╰━┳┳╯╰╮"))
    print (cf.bold_yellow("╔╩╝║╩╬╗║╔╣╩╣╚╣╬║╬║╩╣╬║║╬║║║║║═╣╩╣           ╱╱╰╯╱╰━━━┻┻━━╯"))
    print (cf.bold_red("╚══╩═╝╚═╝╚═╩═╩═╣╔╩═╩═╝╚═╬╗║╚╩═╩═╝"))
    print (cf.bold_red("───────────────╚╝───────╚═╝"))
    sleep(0.1)
    lines = ["You're using AutismWare Recode By ICE#0420"]
    for line in lines:          # for each line of text (or each message)
        for c in line:          # for each character in each line
            print (c, end='')    # print a single character, and keep the cursor there.
            sys.stdout.flush()  # flush the buffer
            sleep(0.1)          # wait a little to make the effect look good.
    print (cf.bold_orange(''))               # line break (optional, could also be part of the message)
    print (cf.bold_purple('________________________________'))
    print (cf.bold_red(' Mention Commands:' ))
    print (cf.bold_red('Send Monkey BROKEN      ' + str(monkey)))
    print (cf.bold_red('Send Headpats BROKEN '+ str(pat)))
    print (cf.bold_red('Send Cuddles BROKEN '+ str(cuddle) ))
    print (cf.bold_red('Send kisses BROKEN '+ str(kiss)))
    print (cf.bold_red('Shoot Someone BROKEN      '+ str(shoot)))
    print (cf.bold_red('Send Huggies BROKEN      '+ str(hug)))
    print (cf.bold_red('Send Stickbug BROKEN     '+ str(stickbug)))
    print (cf.bold_red('Slap User BROKEN         '+ str(slap)))
    print (cf.bold_red('Clap at User BROKEN      '+ str(clap)))
    print (cf.bold_red('Log User Information   ' + str(copy)))
    print (cf.bold_red('Lewd Someone BROKEN       ' + str(lewd)))
    print (cf.bold_red('Fuck Someone BROKEN      '  + str(fuck)))
    print (cf.bold_red('Send Crying BROKEN        ' + str(cry)))
    print (cf.bold_red('Hold hands BROKEN          ' + str(holdhands)))
    print (cf.bold_red('Dance with user BROKEN    ' + str(dance)))
    print (cf.bold_red('send probe BROKEN         ' + str(alienprobe)))
    print (cf.bold_red("Nut On user BROKEN        " + str(nut)))
    print (cf.bold_purple('________________________________'))
    print (cf.bold_orange('Logged in as: '))
    print(client.user.name + "#" + client.user.discriminator)
    print (cf.bold_purple(''))
    print (cf.bold_orange('UserID: '))
    print(client.user.id)
    print (cf.bold_purple('________________________________'))
    print (cf.bold_red('Commands: '))
    print (cf.bold_green("Chat Purge          " + str(cleanphrase)))
    print (cf.bold_green("Send ur thoughts    " + str(death)))
    print (cf.bold_green("Roll the dice       " + str(dice)))
    print (cf.bold_green("Hack the User       " + str(hack)))
    print (cf.bold_green("Set Gaming      " + str(game)))
    print (cf.bold_green("Set Listening       " + str(Listening)))
    print (cf.bold_green("Set Watching      " + str(watchstatus)))
    print (cf.bold_green("Ask The 8Ball      " + str(ball)))
    print (cf.bold_red("Change Console window  " + str(console) + "  I:E .console 1f"))
    print (cf.bold_red("prints Console Color examples " + str(consolecolors)))
    print (cf.bold_green("Help Command Imbed  " + str(help)))
    print (cf.bold_red("Matching pfp list  " + str (guild)))
    print (cf.bold_green("Closes the bot      " + str(logout)))
    print (cf.bold_yellow("Discord Crasher // BROKEN" + str (crash)))
    print (cf.bold_purple('________________________________'))
    print (cf.bold_blue("Client is ready to be used"))








@client.event
async def on_message(message):

        
        
        
        #LogInformation
        if message.content.startswith(str(copy)) and message.author == client.user:
            if message.author == client.user:
                await message.delete()
                try:
                    user = message.mentions[0]
                    log = "Username/Discriminator: " + str(user.name) + "#" + str(user.discriminator)
                    fog = "Discord ID: " + str(user.id)
                    await message.channel.send(log)
                    await asyncio.sleep(0.5)
                    await message.channel.send(fog)
                    await asyncio.sleep(0.5)

                    print (cf.bold_blue("Logged User: " + (user.name) + "#" + (user.discriminator)))
                except:
                    #user = message.mentions[0]
                    #log = "Username/Discriminator: " + str(user.name) + "#" + str(user.discriminator)
                    #fog = "Creation Date" + str(user.created_at)
                    #await message.channel.send(log)
                    #await message.channel.send(fog)
                    #await asyncio.sleep(0.5)
                    print (cf.bold_red("ERROR"))
                    #print (cf.bold_blue("Logged User: " + (user.name) + "#" + (user.discriminator)))
        
        
        
        
        #Breaking my brain one line at a time
        #FuckingWithShit
        if message.content.startswith(str(guild)) and message.author == client.user:
            if message.author == client.user:
                    await message.delete()
                    match = "https://cdn.discordapp.com/attachments/674359483987787794/951735138771935242/DC85E5E6-5E4F-44F1-BA8C-32B5CF28E1DD.png https://cdn.discordapp.com/attachments/674359483987787794/951735138188943420/42107BDE-3C93-4CF1-B8C0-A0CBB25ECC47.png "
                    match2 = "https://cdn.discordapp.com/attachments/674359483987787794/946008932806189106/IMG_3181.png https://cdn.discordapp.com/attachments/674359483987787794/946008932562903040/IMG_3182.png"
                    match3 = "https://cdn.discordapp.com/attachments/674359483987787794/944146047872167936/cfaefe586dbce81fca869b2b6bc32e7b.png https://cdn.discordapp.com/attachments/674359483987787794/944146047440146472/33fc00fbaacd1abd7d500043a23a4e95.png"
                    match4 = "https://cdn.discordapp.com/attachments/674359483987787794/943596867093155940/unknown.png https://cdn.discordapp.com/attachments/674359483987787794/943596866858287154/unknown.png"
                    match5 = "https://cdn.discordapp.com/attachments/674359483987787794/940781528152162304/pfp2.jpg https://cdn.discordapp.com/attachments/674359483987787794/940781527808217168/pfp.jpg"
                    match6 = "https://cdn.discordapp.com/attachments/674359483987787794/939629099314462840/IMG_6054.jpg https://cdn.discordapp.com/attachments/674359483987787794/939629099574521896/IMG_6055.jpg"
                    match7 = "https://cdn.discordapp.com/attachments/674359483987787794/939629098773385266/IMG_6056.jpg https://cdn.discordapp.com/attachments/674359483987787794/939629099008274522/IMG_6057.jpg"
                    match8 = "https://cdn.discordapp.com/attachments/745262990697431150/894193645148848158/1.jpg https://cdn.discordapp.com/attachments/745262990697431150/894193625007808542/fa17c5f12b43f1ee.jpg"
                    match9 = "https://cdn.discordapp.com/attachments/745262990697431150/876654576261013544/image0.jpg https://cdn.discordapp.com/attachments/745262990697431150/876654576445567039/image1.jpg"
                    match1 = "https://cdn.discordapp.com/attachments/745262990697431150/876156906387951636/image2.jpg https://cdn.discordapp.com/attachments/745262990697431150/876156906568298536/image3.jpg"
                    await message.channel.send(match)
                    await asyncio.sleep(0.3)
                    await message.channel.send(match2)
                    await asyncio.sleep(0.3)
                    await message.channel.send(match3)
                    await asyncio.sleep(0.3)
                    await message.channel.send(match4)
                    await asyncio.sleep(0.3)
                    await message.channel.send(match5)
                    await asyncio.sleep(0.3)
                    await message.channel.send(match6)
                    await asyncio.sleep(0.3)
                    await message.channel.send(match7)
                    await asyncio.sleep(0.3)
                    await message.channel.send(match8)
                    await asyncio.sleep(0.3)
                    await message.channel.send(match9)
                    await asyncio.sleep(0.3)
                    await message.channel.send(match1)
                    await asyncio.sleep(0.3)
                    print (cf.bold_blue("Matching?"))
                    
        #crasher
        if message.content.startswith(str(crash)) and message.author == client.user:
                if message.author == client.user:
                    await message.delete()
                    message = await message.channel.send("https://cdn.discordapp.com/attachments/949355891759669338/963137827074347038/choco_milk.webm?size=4096")
                    print (cf.bold_blue("Crasher Sent"))
                    
                    

                #dice
        if message.content.startswith(str(dice)) and message.author == client.user:
                if message.author == client.user:
                    await message.delete()
                    message = await message.channel.send("Rolling Dice")
                    await asyncio.sleep(1)
                    await message.edit (content= random.randrange(0, 7, 1))
                    await asyncio.sleep(0.5)
                    msg = "Finished rolling dice"
                    await message.channel.send(msg)
                    print (cf.bold_blue("dice rolled"))
                    await asyncio.sleep(0.5)



                    #hack
        if message.content.startswith(str(hack)) and message.author == client.user:
                if message.author == client.user:
                    await message.delete()
                    message = await message.channel.send("Hacking this retards account..")
                    await asyncio.sleep(1)
                    await message.edit (content= "Hacking this retards account..." )
                    await asyncio.sleep(0.5)
                    await message.edit (content= "Hacking this retards account...." )
                    await asyncio.sleep(0.5)
                    await message.edit (content= "Hacking this retards account....." )
                    await asyncio.sleep(0.5)
                    await message.edit (content= "Uploading Dox.." )
                    await asyncio.sleep(0.5)
                    await message.edit (content= "Uploading Dox..." )
                    await asyncio.sleep(0.5)
                    await message.edit (content= "Uploading Dox...." )
                    await asyncio.sleep(1)
                    await message.edit (content= "Finished hacking" )
                    await asyncio.sleep(0.5)
                    await message.edit (content= "This :monkey: lives in his mums basement" )
                    await asyncio.sleep(0.5)
                    print (cf.bold_blue("Retard Trolled"))



        #alienprobe
        if message.content.startswith(str(alienprobe)) and message.author == client.user:
             if message.author == client.user:
                 await message.delete()
                 try:
                    user = message.mentions[0]
                    probe1 = "https://cdn.discordapp.com/attachments/668397606954860546/750890319007973537/tenor.gif"
                    probe2 = "https://cdn.discordapp.com/attachments/668397606954860546/750890461471834152/tenor.gif"
                    probe3 = "https://cdn.discordapp.com/attachments/668397606954860546/750890554510016632/tenor.gif"
                    await message.channel.send(embed=embed)
                    print (cf.bold_blue("probing sent to user: " + (user.name) + "#" + (user.discriminator)))
                    await asyncio.sleep(0.5)
                 except IndexError:
                    print("Error User not Found have you tried mentioning them? ")    


        #Dance
        if message.content.startswith(str(dance)) and message.author == client.user:
             if message.author == client.user:
                 await message.delete()
                 try:    
                    user = message.mentions[0]
                    dance1 = "https://cdn.discordapp.com/attachments/668397606954860546/750885182436802610/tenor.gif"
                    dance2 = "https://cdn.discordapp.com/attachments/668397606954860546/750885563971665941/tenor.gif"
                    dance3 = "https://cdn.discordapp.com/attachments/668397606954860546/750885626391429221/tenor.gif"
                    embed = discord.Embed()
                    embed = discord.Embed(title="", description=(message.author.name) + "  Dances with  " + (user.mention), color=0x00ff00)
                    embed.set_footer(text="Command invoked by ICE's Private Selfbot")
                    embed.set_image(url = random.choice([dance1,dance2,dance3]))
                    await message.channel.send(embed=embed)
                    print (cf.bold_blue("Dance sent to user: " + (user.name) + "#" + (user.discriminator)))
                    await asyncio.sleep(2)
                 except IndexError:
                    print("Error User not Found have you tried mentioning them? ")    

        #Cuddle
        if message.content.startswith(str(cuddle)) and message.author == client.user:
            if message.author == client.user:
                await message.delete()
                try:   
                    user = message.mentions[0]
                    Cuddle1 = "https://cdn.discordapp.com/attachments/668397606954860546/749832428360695838/tenor.gif"
                    GuzVaB = "https://cdn.discordapp.com/attachments/668397606954860546/749832718602469467/tenor.gif"
                    vjuNNc = "https://cdn.discordapp.com/attachments/668397606954860546/749832881815420998/tenor.gif"
                    cuddle2 = "https://cdn.discordapp.com/attachments/668397606954860546/750483954611650661/tenor.gif"
                    cuddle3 = "https://cdn.discordapp.com/attachments/668397606954860546/750484123700953218/tenor.gif"
                    cuddle4 = "https://cdn.discordapp.com/attachments/668397606954860546/750484313421774868/tenor.gif"
                    embed = discord.Embed()
                    embed = discord.Embed(title="", description=(message.author.name) + "  Cuddles  " + (user.mention), color=0x00ff00)
                    embed.set_footer(text="Command invoked by ICE's Private Selfbot")
                    embed.set_image(url = random.choice([Cuddle1,GuzVaB,vjuNNc,cuddle2,cuddle3,cuddle4]))
                    await message.channel.send(embed=embed)
                    print (cf.bold_blue("Cuddles sent to user: " + (user.name) + "#" + (user.discriminator)))
                    await asyncio.sleep(2)
                except IndexError:
                    print("Error User not Found have you tried mentioning them? ")

                #Lewd
        if message.content.startswith(str(lewd)) and message.author == client.user:
            if message.author == client.user:
                await message.delete()
                try:    
                    user = message.mentions[0]
                    lewd1 = "https://cdn.discordapp.com/attachments/668397606954860546/750167753847210054/tenor.gif"
                    QoKKla = "https://cdn.discordapp.com/attachments/668397606954860546/750167834524385352/tenor.gif"
                    QBqyFG = "https://cdn.discordapp.com/attachments/668397606954860546/750167934701273158/tenor.gif"
                    lewd2 = "https://cdn.discordapp.com/attachments/668397606954860546/750483132201042060/tenor_1.gif"
                    lewd3 = "https://cdn.discordapp.com/attachments/686666931394314294/750483021613891674/tenor.gif"
                    embed = discord.Embed()
                    embed = discord.Embed(title="", description=(message.author.name) + "  Lewds  " + (user.mention), color=0x00ff00)
                    embed.set_footer(text="Command invoked by ICE's Private Selfbot")
                    embed.set_image(url = random.choice([lewd1,QoKKla,QBqyFG,lewd2,lewd3]))
                    await message.channel.send(embed=embed)
                    print (cf.bold_blue("Lewd sent to user: " + (user.name) + "#" + (user.discriminator)))
                    await asyncio.sleep(2)
                except IndexError:
                    print("Error User not Found have you tried mentioning them? ")    

                #fuck
        if message.content.startswith(str(fuck)) and message.author == client.user:
            if message.author == client.user:
                await message.delete()
                try:   
                    user = message.mentions[0]
                    fuck1 = "https://cdn.discordapp.com/attachments/668397606954860546/750168478736187462/5apr5A.gif"
                    gIoZQd = "https://cdn.discordapp.com/attachments/668397606954860546/750168596126236672/1.gif"
                    aYOGaH = "https://cdn.discordapp.com/attachments/668397606954860546/750168770605219900/3834664966496909gifshentaiporn2406.gif"
                    fuck2 = "https://cdn.discordapp.com/attachments/668397606954860546/750481126442795039/325_1000.gif"
                    fuck3 = "https://cdn.discordapp.com/attachments/668397606954860546/750481465434833069/Animated_GIFs_Angelium_hentai_anime_GIFs_4378532-16.gif"
                    fuck4 = "https://cdn.discordapp.com/attachments/668397606954860546/750481911079632936/5e2df38ca39ce372d03d84e7966eea6a.gif"
                    embed = discord.Embed()
                    embed = discord.Embed(title="", description=(message.author.name) + "  Fucked " + (user.mention), color=0x00ff00)
                    embed.set_footer(text="Command invoked by ICE's Private Selfbot")
                    embed.set_image(url = random.choice([fuck1,gIoZQd,aYOGaH,fuck2,fuck3,fuck4]))
                    await message.channel.send(embed=embed)
                    print (cf.bold_blue("Fuck sent to user: " + (user.name) + "#" + (user.discriminator)))
                    await asyncio.sleep(2)
                except IndexError:
                    print("Error User not Found have you tried mentioning them? ")


                #clap
        if message.content.startswith(str(clap)) and message.author == client.user:
            if message.author == client.user:
                await message.delete()
                try:   
                    user = message.mentions[0]
                    clap1 = "https://cdn.discordapp.com/attachments/668397606954860546/750425898511237180/tenor.gif"
                    clap2 = "https://cdn.discordapp.com/attachments/668397606954860546/750426052479680535/tenor.gif"
                    clap3 = "https://cdn.discordapp.com/attachments/668397606954860546/750426148454006884/tenor.gif"
                    embed = discord.Embed()
                    embed = discord.Embed(title="", description=(message.author.name) + "  clapped " + (user.mention), color=0x00ff00)
                    embed.set_footer(text="Command invoked by ICE's Private Selfbot")
                    embed.set_image(url = random.choice([clap1,clap2,clap3]))
                    await message.channel.send(embed=embed)
                    print (cf.bold_blue("clapped user: " + (user.name) + "#" + (user.discriminator)))
                    await asyncio.sleep(2)
                except IndexError:
                    print("Error User not Found have you tried mentioning them? ")
                    
                         
                
        if message.content.startswith(str(cry)) and message.author == client.user:
            if message.author == client.user:
                await message.delete()
                try:
                    user = message.mentions[0]
                    cry1 = "https://cdn.discordapp.com/attachments/668397606954860546/750169161254305792/tenor.gif"
                    sleep = "https://cdn.discordapp.com/attachments/668397606954860546/750169351822245928/tenor.gif"
                    eat = "https://cdn.discordapp.com/attachments/668397606954860546/750169466582728774/tenor_1.gif"
                    embed = discord.Embed()
                    embed = discord.Embed(title="", description=(message.author.name) + "  Cried too " + (user.mention), color=0x00ff00)
                    embed.set_footer(text="Command invoked by ICE's Private Selfbot")
                    embed.set_image(url = random.choice([cry1,sleep,eat]))
                    await message.channel.send(embed=embed)
                    print (cf.bold_blue("Cry sent to user: " + (user.name) + "#" + (user.discriminator)))
                    await asyncio.sleep(2)
                except IndexError:
                    print("Error User not Found have you tried mentioning them? ")

                #stickbug
        if message.content.startswith(str(stickbug)) and message.author == client.user:
            if message.author == client.user:
                await message.delete()
                try: 
                    user = message.mentions[0]
                    stick1 = "https://cdn.discordapp.com/attachments/668397606954860546/749850987237343312/tenor.gif"
                    yzDJui = "https://cdn.discordapp.com/attachments/668397606954860546/749851517225271406/tenor_1.gif"
                    stick2 = "https://cdn.discordapp.com/attachments/668397606954860546/750488039117160558/tenor.gif"
                    stick3 = "https://cdn.discordapp.com/attachments/668397606954860546/750488212824391781/tenor.gif"
                    embed = discord.Embed()
                    embed = discord.Embed(title="", description=(message.author.name) + "  Stickbugged  " + (user.mention), color=0x00ff00)
                    embed.set_footer(text="Command invoked by ICE's Private Selfbot")
                    embed.set_image(url = random.choice([stick1,yzDJui,stick2,stick3]))
                    await message.channel.send(embed=embed)
                    print (cf.bold_blue("Stickbug sent to user: " + (user.name) + "#" + (user.discriminator)))
                    await asyncio.sleep(2)
                except IndexError:
                    print("Error User not Found have you tried mentioning them? ")



        #Kiss
        if message.content.startswith(str(kiss)) and message.author == client.user:
            if message.author == client.user:
                await message.delete()
                try:   
                    user = message.mentions[0]
                    kiss1 = "https://cdn.discordapp.com/attachments/668397606954860546/749835921704091808/tenor.gif"
                    JgJziV = "https://cdn.discordapp.com/attachments/668397606954860546/749835972299980800/tenor.gif"
                    ceVLlP = "https://cdn.discordapp.com/attachments/668397606954860546/749836007121354792/tenor.gif"
                    WeLodp = "https://cdn.discordapp.com/attachments/668397606954860546/749836031489998918/tenor.gif"
                    kiss2 = "https://cdn.discordapp.com/attachments/668397606954860546/750487481832702092/tenor.gif"
                    kiss3 = "https://cdn.discordapp.com/attachments/668397606954860546/750487569858560030/tenor.gif"
                    kiss4 = "https://cdn.discordapp.com/attachments/668397606954860546/750487666122031214/tenor.gif"
                    embed = discord.Embed()
                    embed = discord.Embed(title="", description=(message.author.name) + "  Kisses  " + (user.mention), color=0x00ff00)
                    embed.set_footer(text="Command invoked by ICE's Private Selfbot")
                    embed.set_image(url = random.choice([kiss1,JgJziV,ceVLlP,WeLodp,kiss2,kiss3,kiss4]))
                    await message.channel.send(embed=embed)
                    print (cf.bold_blue("Kiss sent to user: " + (user.name) + "#" + (user.discriminator)))
                    await asyncio.sleep(2)
                except IndexError:
                    print("Error User not Found have you tried mentioning them? ")

        #Slap
        if message.content.startswith(str(slap)) and message.author == client.user:
            if message.author == client.user:
                await message.delete()
                try:
                    user = message.mentions[0]
                    slap1 = "https://cdn.discordapp.com/attachments/668397606954860546/749892979329859634/tenor.gif"
                    eZeUJO = "https://cdn.discordapp.com/attachments/668397606954860546/749893115673837598/tenor.gif"
                    slap2 = "https://cdn.discordapp.com/attachments/668397606954860546/750487019469275219/tenor.gif"
                    slap3 = "https://cdn.discordapp.com/attachments/668397606954860546/750487165527654422/tenor_1.gif"
                    slap4 = "https://cdn.discordapp.com/attachments/668397606954860546/750487261438803988/tenor.gif"
                    embed = discord.Embed()
                    embed = discord.Embed(title="", description=(message.author.name) + "  slapped  " + (user.mention), color=0x00ff00)
                    embed.set_footer(text="Command invoked by ICE's Private Selfbot")
                    embed.set_image(url = random.choice([slap1,eZeUJO,slap2,slap3,slap4]))
                    await message.channel.send(embed=embed)
                    print (cf.bold_blue("slap sent to user: " + (user.name) + "#" + (user.discriminator)))
                    await asyncio.sleep(2)
                except IndexError:
                    print("Error User not Found have you tried mentioning them? ")
                    

        #Shoot
        if message.content.startswith(str(shoot)) and message.author == client.user:
            if message.author == client.user:
                await message.delete()
                try:
                    user = message.mentions[0]
                    shoot1 = "https://cdn.discordapp.com/attachments/668397606954860546/749841454569881620/tenor.gif"
                    fBeYRU  = "https://cdn.discordapp.com/attachments/668397606954860546/749841487872655445/tenor.gif"
                    GWPmRv = "https://cdn.discordapp.com/attachments/668397606954860546/749841654810148874/tenor.gif"
                    shoot2 = "https://cdn.discordapp.com/attachments/668397606954860546/750486569462530088/tenor_1.gif"
                    shoot3 = "https://cdn.discordapp.com/attachments/668397606954860546/750486607382970498/tenor.gif"
                    shoot4 = "https://cdn.discordapp.com/attachments/668397606954860546/750486734810120252/tenor.gif"
                    embed = discord.Embed()
                    embed = discord.Embed(title="", description=(message.author.name) + "  Shoots  " + (user.mention), color=0x00ff00)
                    embed.set_footer(text="Command invoked by ICE's Private Selfbot")
                    embed.set_image(url = random.choice([shoot1,fBeYRU,GWPmRv,shoot2,shoot3,shoot4]))
                    await message.channel.send(embed=embed)
                    print (cf.bold_blue("Shoot sent to user: " + (user.name) + "#" + (user.discriminator)))
                    await asyncio.sleep(2)
                except IndexError:
                    print("Error User not Found have you tried mentioning them? ")
                    
        #Hug
        if message.content.startswith(str(hug)) and message.author == client.user:
            if message.author == client.user:
                await message.delete()
                try:
                    user = message.mentions[0]
                    hug1 = "https://cdn.discordapp.com/attachments/668397606954860546/749842321608278078/tenor.gif"
                    LAOWfI  = "https://cdn.discordapp.com/attachments/668397606954860546/749842387202736278/tenor.gif"
                    RuQPRg = "https://cdn.discordapp.com/attachments/668397606954860546/749842921209069668/tenor.gif"
                    hug2 = "https://cdn.discordapp.com/attachments/668397606954860546/750484488634761256/tenor.gif"
                    hug3 = "https://cdn.discordapp.com/attachments/668397606954860546/750484733527457812/tenor.gif"
                    hug4 = "https://cdn.discordapp.com/attachments/668397606954860546/750484955175452683/tenor.gif"
                    hug5 = "https://cdn.discordapp.com/attachments/668397606954860546/750485098440294470/tenor.gif"
                    embed = discord.Embed()
                    embed = discord.Embed(title="", description=(message.author.name) + "  hugged " + (user.mention), color=0x00ff00)
                    embed.set_footer(text="Command invoked by ICE's Private Selfbot")
                    embed.set_image(url = random.choice([hug1,LAOWfI,RuQPRg,hug2,hug3,hug4,hug5]))
                    await message.channel.send(embed=embed)
                    print (cf.bold_blue("Hug sent to user: " + (user.name) + "#" + (user.discriminator)))
                    await asyncio.sleep(2)
                except IndexError:
                    print("Error User not Found have you tried mentioning them? ")

        #HoldHands
        if message.content.startswith(str(holdhands)) and message.author == client.user:
            if message.author == client.user:
                await message.delete()
                try:    
                    user = message.mentions[0]
                    hand1 = "https://cdn.discordapp.com/attachments/668397606954860546/750477794215067698/tenor.gif"
                    hand2  = "https://cdn.discordapp.com/attachments/668397606954860546/750477843569311774/tenor.gif"
                    hand3 = "https://cdn.discordapp.com/attachments/668397606954860546/750477894790152222/tenor.gif"
                    hand4 = "https://cdn.discordapp.com/attachments/668397606954860546/750486332702326804/tenor.gif"
                    hand5 = "https://cdn.discordapp.com/attachments/668397606954860546/750486427585871882/tenor.gif"
                    embed = discord.Embed()
                    embed = discord.Embed(title="", description=(message.author.name) + "  Held hands with  " + (user.mention), color=0x00ff00)
                    embed.set_footer(text="Command invoked by ICE's Private Selfbot")
                    embed.set_image(url = random.choice([hand1,hand2,hand3,hand4,hand5]))
                    await message.channel.send(embed=embed)
                    print (cf.bold_blue("held hands with user: " + (user.name) + "#" + (user.discriminator)))
                except IndexError:
                    print("Error User not Found have you tried mentioning them? ")
                
                
                #nut
        if message.content.startswith(str(nut)) and message.author == client.user:
            if message.author == client.user:
                await message.delete()
                try:
                    user = message.mentions[0]
                    nut1 = "https://media3.giphy.com/media/nEZ822P20D1NeEv0lU/giphy.gif?cid=ecf05e47is6sxa5u7fc5sajlag2km7nkg6kdb7is097f8e3z&rid=giphy.gif"
                    nut2  = "https://media4.giphy.com/media/SseqwEB8RUOBcNDVTL/giphy.gif?cid=ecf05e47is6sxa5u7fc5sajlag2km7nkg6kdb7is097f8e3z&rid=giphy.gif"
                    nut3 = "https://media2.giphy.com/media/H4s7qjFZk486I/giphy.gif?cid=ecf05e47de1c250079fd53a67c57343ce32fcbbd2bcce62f&rid=giphy.gif"
                    nut4 = "https://media4.giphy.com/media/88hQmqhcQ7Gmj2cXX3/giphy.gif?cid=ecf05e47is6sxa5u7fc5sajlag2km7nkg6kdb7is097f8e3z&rid=giphy.gif"
                    embed = discord.Embed()
                    embed = discord.Embed(title="", description=(message.author.name) + "  Nutted on   " + (user.mention), color=0x00ff00)
                    embed.set_footer(text="Command invoked by ICE's Private Selfbot")
                    embed.set_image(url = random.choice([nut1,nut2,nut3,nut4]))
                    await message.channel.send(embed=embed)
                    print (cf.bold_blue("Nutted on user: " + (user.name) + "#" + (user.discriminator)))
                    await asyncio.sleep(2)
                except IndexError:
                    print("Error User not Found have you tried mentioning them? ")
                

        #Monkey
        if message.content.startswith(str(monkey)) and message.author == client.user:
            if message.author == client.user:
                await message.delete()
                try:
                    user = message.mentions[0]
                    kek1 = "https://cdn.discordapp.com/attachments/571211528376680448/749782099623673866/tenor.gif"
                    lel2 = "https://cdn.discordapp.com/attachments/571211528376680448/749782217726754866/tenor.gif"
                    monk3 = "https://cdn.discordapp.com/attachments/668397606954860546/749828786845122610/giphy.gif"
                    pasta4 = "https://cdn.discordapp.com/attachments/668397606954860546/749829370218151976/giphy_1.gif"
                    monk4 = "https://cdn.discordapp.com/attachments/668397606954860546/750485262496432159/tenor.gif"
                    monk5 = "https://cdn.discordapp.com/attachments/668397606954860546/750485395980156979/tenor.gif"
                    monk6 = "https://cdn.discordapp.com/attachments/668397606954860546/750485530831093930/tenor.gif"
                    embed = discord.Embed()
                    embed = discord.Embed(title="", description=(message.author.name) + "   Monkeys  " + (user.mention), color=0x00ff00)
                    embed.set_footer(text="Command invoked by ICE's Private Selfbot")
                    embed.set_image(url = random.choice([kek1,lel2,monk3,pasta4,monk4,monk5,monk6]))
                    await message.channel.send(embed=embed)
                    print (cf.bold_blue("Monkey sent to user: " + (user.name) + "#" + (user.discriminator)))
                    await asyncio.sleep(2)
                except IndexError:
                    print("Error User not Found have you tried mentioning them? ")

                #Help
        if message.content.startswith(str(help)) and message.author == client.user:
            if message.author == client.user:
                await message.delete()
                embed = discord.Embed()
                embed = discord.Embed(title="Help Commands: " + str(help) , description="" , color=0x00ff00)
                embed.add_field(name="Send Monkey mentionable", value=str(monkey) , inline=True)
                embed.add_field(name="Send headpats mentionable", value=str(pat) , inline=True)
                embed.add_field(name="Send Cuddles mentionable", value=str(cuddle) , inline=True)
                embed.add_field(name="Send Kiss mentionable", value=str(kiss) , inline=True)
                embed.add_field(name="Send Shoot mentionable", value=str(shoot) , inline=True)
                embed.add_field(name="Send hug mentionable", value=str(hug) , inline=True)
                embed.add_field(name="Send stickbug mentionable", value=str(stickbug) , inline=True)
                embed.add_field(name="Send slap mentionable", value=str(slap) , inline=True)
                embed.add_field(name="Log User Information ", value=str(copy) , inline=True)
                embed.add_field(name="Send lewd mentionable", value=str(lewd) , inline=True)
                embed.add_field(name="Send fuck mentionable", value=str(fuck) , inline=True)
                embed.add_field(name="Send cry mentionable", value=str(cry) , inline=True)
                embed.add_field(name="Send clap mentionable", value=str(clap) , inline=True)
                embed.add_field(name="Send HoldHands mentionable", value=str(holdhands) , inline=True)
                embed.add_field(name="Send Dance Mentionable", value=str(dance) , inline=True)
                embed.add_field(name="Send Probe Mentionable", value=str(alienprobe) , inline=True)
                embed.add_field(name="Chat Purge", value=str(cleanphrase) , inline=True)
                embed.add_field(name="Send Nut Mentionable", value=str(nut) , inline=True)
                embed.add_field(name="Sends life regards", value=str(death) , inline=True)
                embed.add_field(name="Change Console window", value=str(console), inline=True)
                embed.add_field(name="prints Console Color examples", value= str(consolecolors), inline=True)
                await message.channel.send(embed=embed)
                await asyncio.sleep(2)
                embed = discord.Embed()
                embed = discord.Embed(title="Help Commands Page 2: " + str(help) , description="" , color=0x00ff00)
                embed.add_field(name="Roll Dice", value=str(dice) , inline=True)
                embed.add_field(name="Hack user", value=str(hack) , inline=True)
                embed.add_field(name="Set Gaming", value=str(game) , inline=True)
                embed.add_field(name="Set Listening", value=str(Listening) , inline=True)
                embed.add_field(name="Set Watching", value=str(watchstatus) , inline=True)
                embed.add_field(name="Logs the bot out", value=str(logout) , inline=False)
                embed.set_footer(text="Command invoked by ICE's Private Selfbot")
                await asyncio.sleep(2)
                await message.channel.send(embed=embed)
                print (cf.bold_blue("Help recieved"))


                #pat
        if message.content.startswith(str(pat)) and message.author == client.user:
            if message.author == client.user:
                await message.delete()
                try:
                    user = message.mentions[0]
                    USGGwR = "https://cdn.discordapp.com/attachments/571211528376680448/749800840587640933/tenor.gif"
                    WRYwhx = "https://cdn.discordapp.com/attachments/571211528376680448/749800944358785135/tenor.gif"
                    YYREiL = "https://cdn.discordapp.com/attachments/571211528376680448/749801004295389275/tenor.gif"
                    qSsiFC = "https://cdn.discordapp.com/attachments/668397606954860546/749830562159525918/tenor.gif"
                    VZrrtb = "https://cdn.discordapp.com/attachments/668397606954860546/749831463272448121/tenor.gif"
                    pat2 = "https://cdn.discordapp.com/attachments/668397606954860546/750485774360641546/tenor.gif"
                    pat3 = "https://cdn.discordapp.com/attachments/668397606954860546/750485863401521242/tenor_1.gif"
                    pat4 = "https://cdn.discordapp.com/attachments/668397606954860546/750485959656603808/tenor.gif"
                    pat5 =  "https://cdn.discordapp.com/attachments/668397606954860546/750486078573772901/tenor.gif"
                    embed = discord.Embed()
                    embed = discord.Embed(title="", description=(message.author.name) + "   Headpats  " + (user.mention), color=0x00ff00)
                    embed.set_footer(text="Command invoked by ICE's Private Selfbot")
                    embed.set_image(url = random.choice([USGGwR,WRYwhx,YYREiL,qSsiFC,VZrrtb,pat2,pat3,pat4,pat5]))
                    await message.channel.send(embed=embed)
                    print (cf.bold_blue("Headpats sent to user: " + (user.name) + "#" + (user.discriminator)))
                    await asyncio.sleep(1.0)
                except IndexError:
                    print("Error User not Found have you tried mentioning them? ")

        #Logout
        if message.content.startswith(str(logout)) and message.author == client.user:
            if message.author == client.user:
                await message.delete()
                try:
                    print (cf.bold_blue("SelfBot Logging Out"))
                    await asyncio.sleep(1)
                    await client.change_presence(status=discord.Status.do_not_disturb)
                    print (cf.bold_blue("Cleared Status"))
                    print (cf.bold_red("you a gay ass nigga"))
                    await asyncio.sleep(1)
                    print("You've Been Logged out Goodbye")  # This is optional, but it is there to tell you.
                    await asyncio.sleep(1)
                    await client.logout()
                except IndexError:
                    print("you a gay ass nigga")
                


        #death
        if message.content.startswith(str(death)) and message.author == client.user:
                if message.author == client.user:
                    await message.delete()
                    msg = " Have i "
                    await message.channel.send(msg)
                    await asyncio.sleep(1)
                    msg = " ever told you "
                    await message.channel.send(msg)
                    await asyncio.sleep(1)
                    msg = " that i "
                    await message.channel.send(msg)
                    await asyncio.sleep(1)
                    msg = " want to "
                    await message.channel.send(msg)
                    await asyncio.sleep(0.5)
                    msg = " commit die "
                    await message.channel.send(msg)
                    await asyncio.sleep(1)
                    msg = " :clap: "
                    await message.channel.send(msg)
                    await asyncio.sleep(1)
                    print (cf.bold_blue("death Sent"))

        #ClearChat
        counter = 0
        if message.content.startswith(str(cleanphrase)) and message.author == client.user:
            async for message in message.channel.history(limit=999999):
                if message.author == client.user:
                    try: 
                        await message.delete()
                        await asyncio.sleep(2)
                        counter += 1
                        print (cf.bold_blue("Cleaned " + str(counter) + " messages."))
                    except discord.errors.Forbidden:
                        print("Skipping Error Message ( Continue: ) ")
                

        #Game Status
        if message.content.startswith(str(game)) and message.author == client.user:
                if message.author == client.user:
                 await message.delete()
                 Game = message.content.lstrip('.setgame')
                 await client.change_presence(activity=discord.Game(name=(Game)))
                 print (cf.bold_blue("Set Game activity to :" + (Game)))
                 await asyncio.sleep(1)

        #Watch Status
        if message.content.startswith(str(watchstatus)) and message.author == client.user:
                if message.author == client.user:
                 await message.delete()
                 Watch = message.content.lstrip('.setwatch')
                 await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=(Watch)))
                 print (cf.bold_blue("Set Watching activity to :" + (Watch)))
                 await asyncio.sleep(1)


        #Listening Status
        if message.content.startswith(str(Listening)) and message.author == client.user:
              if message.author == client.user:
                await message.delete()
                listen = message.content.lstrip('.setlisten')
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=(listen)))
                print (cf.bold_blue("Listening Status Changed To:" + (listen)))
                await asyncio.sleep(1)
                
        #Change Console Color
        if message.content.startswith(str(console)) and message.author == client.user:
              if message.author == client.user:
                    await message.delete()
                    color = "color " + message.content.lstrip('.console color')
                    os.system(color)
                    print (cf.bold_blue("Console Color Changed"))
                    await asyncio.sleep(1)
                
        #List Console colors  
        if message.content.startswith(str(consolecolors)) and message.author == client.user:
              if message.author == client.user:
                await message.delete()
                print (cf.bold_blue("0f = Black"))
                print (cf.bold_blue("8f = Gray"))
                print (cf.bold_blue("1f = Blue"))
                print (cf.bold_blue("9f = Light Blue"))
                print (cf.bold_blue("2f = Green"))
                print (cf.bold_blue("Af = Light Green"))
                print (cf.bold_blue("3f = Aqua"))
                print (cf.bold_blue("Bf = Light Aqua"))
                print (cf.bold_blue("4f = Red"))
                print (cf.bold_blue("5f = Purple"))     
                print (cf.bold_blue("Df = Light Purple"))
                print (cf.bold_blue("6f = Yellow"))
                print (cf.bold_blue("Ef = Light Yellow"))
                print (cf.bold_blue("7f = White"))
                print (cf.bold_blue("Ff = Bright White"))
                
                
                #8Ball
        if message.content.startswith(str(ball)) and message.author == client.user:
              if message.author == client.user:
                message = await message.channel.send("The8Ball Is Thinking")
                await asyncio.sleep(2)
                ist = ["Unsure    //8ball Response", "Yes    //8ball Response", "Maybe    //8ball Response ", "No    //8ball Response" , "Fuck Yeah    //8ball Response" , "Fuck No    //8ball Response" , "Stop asking    //8ball Response", "Im Certain    //8ball Response" , "No because your life is worthless    //8ball Response", "shut up you sped    //8ball Response", "Just stop   //8ball Response", "Go away   //8ball Response" ]
                await message.edit(content= random.choice(ist))
                print("8Ball command sent")

    

client.run(token, bot=False)
print ("Closing Bot Wait 5 seconds")
time.sleep(5)