import re
import os
import discord
from discord.ext import commands
import random
from discord.ext import tasks

client = discord.Client()
bot = commands.Bot(command_prefix='%')

taco_pics = ["https://tokyo-kitchen.icook.network/uploads/recipe/cover/60551/ce442fcb4b6f35ba.jpg",
"https://tokyo-kitchen.icook.network/uploads/recipe/cover/267919/7aa4779ce5040c2a.jpg",
"https://ciao.kitchen/wp-content/uploads/2018/04/%E5%A1%94%E5%85%8B%E9%A4%85-3711x2660.jpg",
"https://www.ilovespices.tw/wp-content/uploads/2019/12/Zz03NDRhYTBmZGM3OWEyMGQxOGJkOTMzNmRiNGZlOWM1ZA.jpg",
"https://cteecors.azureedge.net/wp-content/uploads/2021/10/04/05-09603-001.jpg",
"https://tokyo-kitchen.icook.network/uploads/recipe/cover/267919/7aa4779ce5040c2a.jpg",
"https://tokyo-kitchen.icook.network/uploads/recipe/cover/404282/74ebd67e6b391fe7.jpg",
"https://s3-eu-central-1.amazonaws.com/glossika-blog/2021/10/mexican-food-taco.jpg",
"https://www.thespruceeats.com/thmb/C0Rx3q8cglHwayLa3d7lnS7SuMg=/3000x2000/filters:fill(auto,1)/chicken-tinga-tinga-de-pollo-4773239-Hero_01-1bd1d960c02a4fdb812323b8c60fd55b.jpg",
"https://media-cdn.tripadvisor.com/media/photo-s/1a/f0/bf/25/slanted-taco.jpg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/001_Tacos_de_carnitas%2C_carne_asada_y_al_pastor.jpg/800px-001_Tacos_de_carnitas%2C_carne_asada_y_al_pastor.jpg",
"http://cn.flavours101.net/wp-content/uploads/sites/2/2021/04/1602583932_131020181012120000005f857d7c58644.jpg",
"https://img.taste.com.au/w_-0kcUJ/taste/2016/11/aussie-style-beef-and-salad-tacos-86525-1.jpeg",
"https://shoplineimg.com/5756526be37ec6ab5e000158/5d3acddf00d1e6001428b434/750x.jpg?",
"https://images-gmi-pmc.edge-generalmills.com/dc04f79c-cfd3-4132-8a0f-49b7a30c547e.jpg",
"https://media-cdn.tripadvisor.com/media/photo-p/15/a5/d9/f9/tacos.jpg",
"https://assets.tmecosys.com/image/upload/t_web767x639/img/recipe/ras/Assets/CF894406-192E-4166-A5A6-83C7EC8DEDC3/Derivates/74faf775-04e4-47f4-83a8-fb58456d8628.jpg",
"https://i0.wp.com/beyondyourtaste.com/wp-content/uploads/2022/02/269792003_475638157255009_9087436863738449513_n.jpg?resize=1080%2C1080&ssl=1",
"https://pic.pimg.tw/anny2949/1650170913-1313539207-g_l.jpg",
"https://media-cdn.tripadvisor.com/media/photo-s/19/60/90/99/2-tacos.jpg",
"https://d1ralsognjng37.cloudfront.net/b05d0e55-936d-4971-b7b3-fd450e942c62.jpeg",
"https://c.ndtvimg.com/2021-09/10cgsus8_tacos_625x300_09_September_21.jpg"]

@client.event
async def on_ready():
    print('開解',client.user)
    game = discord.Game('解你的牌')
    #discord.Status.<狀態>，online,offline,idle,dnd,invisible
    await client.change_presence(status=discord.Status.online, activity=game)
    
@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('嗨我是塔可巫師AKA解牌巫師，輸入「關於塔可巫師」查看我ㄉ功能')
        break

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if '解牌巫師' in message.content.lower():
        await message.channel.send('幹嘛🧿🔮')
    
    if '塔可巫師' in message.content.lower():
        await message.channel.send('🌮🤤')
#其他

    if message.content == '每日塔可':
        await message.channel.send(random.choice(taco_pics))

    if message.content =='關於塔可巫師':
        embed0=discord.Embed(title="塔可巫師ㄉ介紹", color=0x9a7a9f)
        embed0.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed0.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/867/867882.png"),
        embed0.add_field(name="每日塔牌🔮", value="你ㄉ隨機塔羅牌and解釋", inline=False)
        embed0.add_field(name="每日塔可🌮", value= "隨機塔可好吃圖片", inline=False)        
        embed0.add_field(name="每日其他功能", value= "我還在想oO", inline=False)  
        await message.channel.send(embed=embed0)

    if message.content.startswith('改改狀態'):
        tmp = message.content.split(" ",2)
        if len(tmp) == 1:
            await message.channel.send("你要改成什麼啦？")
        else:
            game = discord.Game(tmp[1])
            #online,offline,idle,dnd,invisible
            await client.change_presence(status=discord.Status.online, activity=game)
    
#塔羅
    if message.content == '每日塔牌':
        #大牌
        #21
        embed1=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed1.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed1.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/10/06/23/00/the-world-6686820_960_720.jpg"),
        embed1.add_field(name="你今天ㄉ牌是", value="【世界 正位】", inline=False)
        embed1.add_field(name="牌義", value= "世界正位代表你畢生追求的夢想得以實現。或辛勤付出之後得到了報酬。人際關係非常的穩定、備受他人信賴。", inline=True)

        embed2=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed2.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed2.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/10/06/23/00/the-world-6686820_960_720.jpg")
        embed2.add_field(name="你今天ㄉ牌是", value="【世界 逆位】", inline=False)
        embed2.add_field(name="牌義", value= "世界逆位代表你無法完成想完成的事情。凡事不太順利、不安於現狀、情緒特別低迷、思維頗顯幼稚。", inline=True)
        #20
        embed3=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed3.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed3.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-judgement.jpg")
        embed3.add_field(name="你今天ㄉ牌是", value="【審判 正位】", inline=False)
        embed3.add_field(name="牌義", value= "審判正位代表你知道了自己的錯誤並且開始悔改。或已經毫無希望的事情出現了轉機。與舊友言歸於好、與他人建立彼此信賴的關係。", inline=True)

        embed4=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed4.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed4.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-judgement.jpg")
        embed4.add_field(name="你今天ㄉ牌是", value="【審判 逆位】", inline=False)
        embed4.add_field(name="牌義", value= "審判逆位代表你生活特別散漫、因良心發現而內心有種罪惡感。朋友感到特別的失望、過去被好友背叛致使心裡留下陰影、時常會認錯人。", inline=True)
        #19
        embed5=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed5.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed5.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/05/13/06/39/tarot-6249979_960_720.jpg")
        embed5.add_field(name="你今天ㄉ牌是", value="【太陽 正位】", inline=False)
        embed5.add_field(name="牌義", value= "太陽正位代表你的實力得以充分發揮、竭盡全力最終獲得成功、面對課業積極上進、成績快速進步、考試順利。並且與朋友的關係日亦親密、好友越來越多。", inline=True)

        embed6=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed6.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed6.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/05/13/06/39/tarot-6249979_960_720.jpg")
        embed6.add_field(name="你今天ㄉ牌是", value="【太陽 逆位】", inline=False)
        embed6.add_field(name="牌義", value= "太陽逆位代表你對很多事情都無法持久、性格不開朗、感到無助、生活不穩定。或因衝動而使感情破裂、有分手的危險。", inline=True)
        #18
        embed7=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed7.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed7.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/05/13/06/39/tarot-6249977_960_720.jpg")
        embed7.add_field(name="你今天ㄉ牌是", value="【月亮 正位】", inline=False)
        embed7.add_field(name="牌義", value= "月亮正位代表你總是想著一件令你難受的還沒辦完的事情。事業有成卻又無法滿足、成績非常的差、因考試時心神不寧而導致失敗。", inline=True)

        embed8=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed8.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed8.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/05/13/06/39/tarot-6249977_960_720.jpg")
        embed8.add_field(name="你今天ㄉ牌是", value="【月亮 逆位】", inline=False)
        embed8.add_field(name="牌義", value= "月亮逆位代表你的狀況已經逐漸開始好轉、時間可以沖淡一切、疑慮漸消、倖免遇害。或檢討以往的過失、遭遇瓶頸苦研良策、默默付出終將獲得收益。", inline=True)
        #17
        embed9=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed9.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed9.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/05/13/06/39/tarot-6249976_960_720.jpg")
        embed9.add_field(name="你今天ㄉ牌是", value="【星星 正位】", inline=False)
        embed9.add_field(name="牌義", value= "星星正位代表你的願望得以實現、充滿無窮的創造力、萌發靈感、理想主義者、前景光明。", inline=True)

        embed10=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed10.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed10.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/05/13/06/39/tarot-6249976_960_720.jpg")
        embed10.add_field(name="你今天ㄉ牌是", value="【星星 逆位】", inline=False)
        embed10.add_field(name="牌義", value= "星星逆位代表你缺乏想像力、幻想破滅、好高騖遠、錯失良機、固執己見、理想與現實兩者無法兼顧。", inline=True)
        #16
        embed11=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed11.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed11.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/05/13/06/39/tarot-6249975_960_720.jpg")
        embed11.add_field(name="你今天ㄉ牌是", value="【高塔 正位】", inline=False)
        embed11.add_field(name="牌義", value= "高塔正位代表你不斷地遭遇麻煩、遭遇逆境、遭受打擊、原有的信念崩潰、遭遇突發事件、多管閒事、與人發生紛爭。", inline=True)

        embed12=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed12.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed12.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/05/13/06/39/tarot-6249975_960_720.jpg")
        embed12.add_field(name="你今天ㄉ牌是", value="【高塔 逆位】", inline=False)
        embed12.add_field(name="牌義", value= "高塔逆位代表遭遇到口舌之災、發生內部糾紛、風暴前的寂靜。或受困於不快樂或者失敗的境地，無法通過有力的導向令自己走出困境。", inline=True)
        #15
        embed13=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed13.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed13.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/05/13/06/39/tarot-6249974_960_720.jpg")
        embed13.add_field(name="你今天ㄉ牌是", value="【惡魔 正位】", inline=False)
        embed13.add_field(name="牌義", value= "惡魔正位代表你因受到拘束而特別的不自在、卑躬屈膝、淪為俘虜、十分頹廢的生活、隱瞞事實真相、會遭遇誘惑的陷阱、固執己見、已經貪婪成性。", inline=True)

        embed14=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed14.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed14.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/05/13/06/39/tarot-6249974_960_720.jpg")
        embed14.add_field(name="你今天ㄉ牌是", value="【惡魔 逆位】", inline=False)
        embed14.add_field(name="牌義", value= "惡魔逆位代表你擺脫了不良誘惑、與酒肉朋友斷交、拋棄了慾望、擁有了走出困境的機會、重新獲得自由、能夠表達出自己的意志。", inline=True)
        #14
        embed15=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed15.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed15.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/05/13/06/39/tarot-6249973_960_720.jpg")
        embed15.add_field(name="你今天ㄉ牌是", value="【節制 正位】", inline=False)
        embed15.add_field(name="牌義", value= "節制正位代表你會為他人排解爭端、整理出思路與情緒、淨化心靈、反复鑽研尋找關鍵所在、關注自我需求的同時還兼顧他人的意願、特別勤於節儉、相互協助。", inline=True)

        embed16=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed16.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed16.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/05/13/06/39/tarot-6249973_960_720.jpg")
        embed16.add_field(name="你今天ㄉ牌是", value="【節制 逆位】", inline=False)
        embed16.add_field(name="牌義", value= "節制逆位代表你乏自我調節的能力、開銷過大、遺忘初衷。你面對繁瑣的工作太過於情緒化、精神比較鬆懈、事情進展的十分不順利、成績在不斷地下滑。", inline=True)
        #13
        embed17=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed17.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed17.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/05/13/06/38/tarot-6249972_960_720.jpg")
        embed17.add_field(name="你今天ㄉ牌是", value="【死神 正位】", inline=False)
        embed17.add_field(name="牌義", value= "死神正位代表你與朋友的關係曰益惡化、友情方面出現了裂痕，對周邊的事物沒有任何興趣、厭世、遭遇窘境、一切即將成為泡影。", inline=True)

        embed18=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed18.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed18.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/05/13/06/38/tarot-6249972_960_720.jpg")
        embed18.add_field(name="你今天ㄉ牌是", value="【死神 逆位】", inline=False)
        embed18.add_field(name="牌義", value= "死神逆位代表你黑暗時期的終結，良好的開端，僵持的局面出現了轉機。另外你將會心情好轉、勇於開拓創新。", inline=True)
        #12
        embed19=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed19.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed19.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/05/13/06/38/tarot-6249969_960_720.jpg")
        embed19.add_field(name="你今天ㄉ牌是", value="【吊人 正位】", inline=False)
        embed19.add_field(name="牌義", value= "吊人正位代表你為了心中的理想做出犧牲，明知道辛苦卻依然付出努力。而且你在做的事情有償的犧牲。暗示著得到之前的失去，或是在選擇後的平靜。安靜地等待時機的轉變。", inline=True)

        embed20=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed20.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed20.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/05/13/06/38/tarot-6249969_960_720.jpg")
        embed20.add_field(name="你今天ㄉ牌是", value="【吊人 逆位】", inline=False)
        embed20.add_field(name="牌義", value= "吊人逆位代表你做了無謂的犧牲和努力。辛苦而且沒有回報。而且無法改變想法，鑽進了思想的死胡同。而在愛情中，付出得不到回應，沒有結果的愛。", inline=True)
        #11
        embed21=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed21.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed21.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/05/13/06/38/tarot-6249968_960_720.jpg")
        embed21.add_field(name="你今天ㄉ牌是", value="【正義 正位】", inline=False)
        embed21.add_field(name="牌義", value= "正義正位代表你在陷入的事情中最終得到了公平的對待。或是你在事物之間尋找平衡點，調和。並且誠實，光明正大，尊重自己的信譽，有嚴格標準的人。", inline=True)

        embed22=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed22.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed22.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/05/13/06/38/tarot-6249968_960_720.jpg")
        embed22.add_field(name="你今天ㄉ牌是", value="【正義 逆位】", inline=False)
        embed22.add_field(name="牌義", value= "正義逆位代表你放棄道德，做出讓人無法容忍的事情。像對別人做了不公平的事情或懷著偏心甚至偏見。或是你在事務中得到了不公平的對待。", inline=True)
        #10
        embed23=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed23.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed23.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/05/13/06/38/tarot-6249967_960_720.jpg")
        embed23.add_field(name="你今天ㄉ牌是", value="【命運之輪 正位】", inline=False)
        embed23.add_field(name="牌義", value= "命運之輪代表你會有積極向上的生活狀態，出現了好事情。事業到達了一種巔峰的狀態，最高最強大的時刻馬上來臨。而且運氣不錯，好的機會展開。", inline=True)

        embed24=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed24.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed24.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/05/13/06/38/tarot-6249967_960_720.jpg")
        embed24.add_field(name="你今天ㄉ牌是", value="【命運之輪 逆位】", inline=False)
        embed24.add_field(name="牌義", value= "命運之輪正義逆位代表你放棄道德，做出讓人無法容忍的事情。像對別人做了不公平的事情或懷著偏心甚至偏見。或是你在事務中得到了不公平的對待。", inline=True)
        #9
        embed25=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed25.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed25.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/04/05/22/43/the-hermit-6154777_960_720.jpg")
        embed25.add_field(name="你今天ㄉ牌是", value="【隱者 正位】", inline=False)
        embed25.add_field(name="牌義", value= "隱者正位代表你是有獨立思考的能力，可以為別人提供有用的建議的人。而且需要更多的私人空間，所以對周圍的情況保持著警惕心。但是很沉著，冷靜，思維周密。", inline=True)

        embed26=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed26.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed26.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/04/05/22/43/the-hermit-6154777_960_720.jpg")
        embed26.add_field(name="你今天ㄉ牌是", value="【隱者 逆位】", inline=False)
        embed26.add_field(name="牌義", value= "隱者逆位代表你是鑽牛角尖，無法聽從別人的建議。失去了謹慎，操之過急。因此孤僻，不願意和人來往，內心焦躁不安，人際關係有欠溝通。", inline=True)
        #8
        embed27=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed27.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed27.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/04/05/22/43/strength-6154776_960_720.jpg")
        embed27.add_field(name="你今天ㄉ牌是", value="【力量 正位】", inline=False)
        embed27.add_field(name="牌義", value= "力量正位代表你是個有勇氣，堅定不移的信念，強大的意志力和忍耐力。而且是善於把尖銳的問題處理好的人，或者把話說的很周全的人。", inline=True)

        embed28=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed28.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed28.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/04/05/22/43/strength-6154776_960_720.jpg")
        embed28.add_field(name="你今天ㄉ牌是", value="【力量 逆位】", inline=False)
        embed28.add_field(name="牌義", value= "力量逆位代表你內心空虛，缺乏熱情和愛，沒有憐憫之心。而且沒有頭腦，做事不經過大腦而顯得愚蠢令人討厭。還有無能。無法正確駕馭自己的慾望。", inline=True)
        #7
        embed29=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed29.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed29.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/04/05/22/43/the-chariot-6154775_960_720.jpg")
        embed29.add_field(name="你今天ㄉ牌是", value="【戰車 正位】", inline=False)
        embed29.add_field(name="牌義", value= "戰車正位代表你是具有強烈意志力的人，或者對別人能夠指揮的人。而且自我意識的提升，發現自己的能量，讓你向著某件計劃出發。", inline=True)

        embed30=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed30.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed30.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/04/05/22/43/the-chariot-6154775_960_720.jpg")
        embed30.add_field(name="你今天ㄉ牌是", value="【戰車 逆位】", inline=False)
        embed30.add_field(name="牌義", value= "戰車逆位代表你缺乏意志力，失去了信念，消極，缺乏鬥志，對自己不肯定。可能因為被對手打敗，或者遭遇到強勁有力的對手。而且感情上過於地嚴於要求對方，可能會有爭吵。", inline=True)
        #6
        embed31=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed31.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed31.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/04/05/22/43/the-lovers-6154774_960_720.jpg")
        embed31.add_field(name="你今天ㄉ牌是", value="【戀人 正位】", inline=False)
        embed31.add_field(name="牌義", value= "戀人正位代表會面臨著重大的選擇，這是個很重要的選擇。一旦出錯那麼後果會很嚴重。但或許會出現合作夥伴，結盟，如果合作，會有一番很不錯的合作。", inline=True)

        embed32=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed32.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed32.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/04/05/22/43/the-lovers-6154774_960_720.jpg")
        embed32.add_field(name="你今天ㄉ牌是", value="【戀人 逆位】", inline=False)
        embed32.add_field(name="牌義", value= "戀人逆位代表選擇了錯誤的合作夥伴，導致關係惡化，最終無法繼續實施計劃。或是你不穩定，不安穩，內心得不到休息，無法持續下去。", inline=True)
        #5
        embed33=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed33.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed33.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/04/05/22/42/the-hierophant-6154772_960_720.jpg")
        embed33.add_field(name="你今天ㄉ牌是", value="【教皇 正位】", inline=False)
        embed33.add_field(name="牌義", value= "教皇正位代表你值得信賴或你會遇到良師，同時也代表會出現引導你的人，或是你是一個值得信賴的人，並且你要多聽建議。然後參加團體活力，並且得到承認。", inline=True)

        embed34=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed34.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed34.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/04/05/22/42/the-hierophant-6154772_960_720.jpg")
        embed34.add_field(name="你今天ㄉ牌是", value="【教皇 逆位】", inline=False)
        embed34.add_field(name="牌義", value= "教皇逆位代表你是無教養，缺乏引導的年輕人。但同時打破常規，打破平常的戒律和道德規範，大膽地創新。與眾不同。卻可能極度地固執，或者極度地標新立異。", inline=True)
        #4
        embed35=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed35.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed35.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/04/05/22/42/the-emperor-6154771_960_720.jpg")
        embed35.add_field(name="你今天ㄉ牌是", value="【皇帝 正位】", inline=False)
        embed35.add_field(name="牌義", value= "皇帝正位代表對別人強大的影響力和控制力的人。情況好時，能夠給別人正確的引導並且達到成就，情況不好時，會控制別人，甚至會讓別人走入錯誤的路上而不自知。然後可能會喜歡上比自己年齡稍長的男人", inline=True)

        embed36=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed36.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed36.set_thumbnail(url="https://cdn.pixabay.com/photo/2021/04/05/22/42/the-emperor-6154771_960_720.jpg")
        embed36.add_field(name="你今天ㄉ牌是", value="【皇帝 逆位】", inline=False)
        embed36.add_field(name="牌義", value= "皇帝逆位代表無教養，缺乏引導的年輕人。而且打破常規，打破平常的戒律和道德規範，大膽地創新。與眾不同。極度地固執，或者極度地標新立異。", inline=True)
        #3
        embed37=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed37.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed37.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-empress.jpg")
        embed37.add_field(name="你今天ㄉ牌是", value="【女皇 正位】", inline=False)
        embed37.add_field(name="牌義", value= "女皇正位代表寬和的包容力，豐滿的感知力，自然溫柔的影響力。成績進步而且非常的優秀、在藝術領域頗有收穫。", inline=True)

        embed38=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed38.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed38.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-empress.jpg")
        embed38.add_field(name="你今天ㄉ牌是", value="【女皇 逆位】", inline=False)
        embed38.add_field(name="牌義", value= "女皇逆位代表處事優柔寡斷、愛好太多不知道哪個是輕哪個是重、談吐輕浮、金玉其外敗絮其中。並且根據自己的喜好來選擇學科、成績較差、注意力無法集中。", inline=True)
        #2
        embed39=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed39.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed39.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-highpriestess.jpg")
        embed39.add_field(name="你今天ㄉ牌是", value="【女祭司 正位】", inline=False)
        embed39.add_field(name="牌義", value= "女祭司正位代表冷靜且客觀的判斷，你會遇到展現你能力的機會，或是交到新的朋友。而且對發生的事務已經掌握了足夠的信息量，你所想到的，大部分都是真實的。", inline=True)

        embed40=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed40.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed40.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-highpriestess.jpg")
        embed40.add_field(name="你今天ㄉ牌是", value="【女祭司 逆位】", inline=False)
        embed40.add_field(name="牌義", value= "女祭司逆位代表不學無術，無知。缺乏理解力和判斷力，對周圍的事情反應非常遲鈍。你失去內心的平靜，無法冷靜地思考，對事務的看法偏激。", inline=True)
        #1
        embed41=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed41.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed41.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/The-Magician-1.jpg")
        embed41.add_field(name="你今天ㄉ牌是", value="【魔術師 正位】", inline=False)
        embed41.add_field(name="牌義", value= "魔術師正位代表思維敏捷，行動迅速，強有力的表達能力。充滿了無比的自信。並且周遭有輔助自己的事務出現，在工作中，會出現較之前更順利的進展。", inline=True)

        embed42=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed42.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed42.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/The-Magician-1.jpg")
        embed42.add_field(name="你今天ㄉ牌是", value="【魔術師 逆位】", inline=False)
        embed42.add_field(name="牌義", value= "魔術師逆位代表面前可能會有意想不到的阻撓發生，讓良好的計劃無法正常實施。可能你頭腦有些混亂，無法正常判斷，對周遭發生的事情失去了控制力，無能力改變。", inline=True)
        #0
        embed43=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed43.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed43.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-fool.jpg")
        embed43.add_field(name="你今天ㄉ牌是", value="【愚者 正位】", inline=False)
        embed43.add_field(name="牌義", value= "愚者正位代表冒險，有夢想，不拘泥于傳統的觀念，自由奔放，居無定所，一切從基礎出發。愚者暗示通往成功之路是經由自發的行動，而長期的計劃則是將來的事。", inline=True)

        embed44=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed44.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed44.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-fool.jpg")
        embed44.add_field(name="你今天ㄉ牌是", value="【愚者 逆位】", inline=False)
        embed44.add_field(name="牌義", value= "愚者逆位代表魯莽且瘋狂的人，會面臨情緒低落，缺乏耐心，還有會失敗，純潔逐漸失去，心靈無法得到滿足然後開始墮落。", inline=True)
        #權杖
        embed45=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed45.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed45.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-01.jpg")
        embed45.add_field(name="你今天ㄉ牌是", value="【權杖一 正位】", inline=False)
        embed45.add_field(name="牌義", value= "權杖一正位代表你在一開始應該要掌握到核心才是重點，細枝末節的東西不用太在意。並且對於沒有接觸過的東西充滿好奇心，但是也因為不熟悉而覺得沒有安全感，要對自己有信心。", inline=True)

        embed46=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed46.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed46.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-01.jpg")
        embed46.add_field(name="你今天ㄉ牌是", value="【權杖一 逆位】", inline=False)
        embed46.add_field(name="牌義", value= "權杖一逆位代表你不知道自己做什麼，需要等待最佳時機。現在開始面臨到人際關係的一點波動，雖然不太順利，但是還可以過得去。你在學習上遇到新的困難，問題是你基礎不穩固，所以還是要努力把過去不足之處補起來。", inline=True)
        
        embed47=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed47.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed47.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-02.jpg")
        embed47.add_field(name="你今天ㄉ牌是", value="【權杖二 正位】", inline=False)
        embed47.add_field(name="牌義", value= "權杖二正位代表你正在仔細規劃未來，積極準備，必須離開熟悉的地方才有機會。你在學業上的表現還不錯，但是你自己對於這個狀況並不滿足，仍然想要有更好的表現，只是現在沒有好的辦法。", inline=True)

        embed48=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed48.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed48.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-02.jpg")
        embed48.add_field(name="你今天ㄉ牌是", value="【權杖二 逆位】", inline=False)
        embed48.add_field(name="牌義", value= "權杖二逆位代表你在學業上的表現起伏很大，也常因為粗心大意而犯錯，你應該想更小心地表現自己，不要只是傻傻地向前衝。並且你要切忌主觀衝動地決定情事，會造成更多損失。", inline=True)

        embed49=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed49.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed49.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-03.jpg")
        embed49.add_field(name="你今天ㄉ牌是", value="【權杖三 正位】", inline=False)
        embed49.add_field(name="牌義", value= "權杖三正位代表你現在學業上已經打下了良好的基礎，也具備了進一步發展的能力，只要你能在這個基礎上好好努力就能成功。並且你的計劃順利進行，正在擴大規模，前方即將發生變化，鼓勵你去冒險。", inline=True)

        embed50=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed50.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed50.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-03.jpg")
        embed50.add_field(name="你今天ㄉ牌是", value="【權杖三 逆位】", inline=False)
        embed50.add_field(name="牌義", value= "權杖三逆位代表你在學業上你算是苦盡甘來，已經開始看到一些好的成果，你應該在這個基礎上持續努力，不要放棄任何希望。你目前的人際關係還不錯，但有時候會因為自己的傲慢無知的表現而使朋友不高興，這個時候應該親自向他道歉。", inline=True)

        embed51=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed51.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed51.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-04.jpg")
        embed51.add_field(name="你今天ㄉ牌是", value="【權杖四 正位】", inline=False)
        embed51.add_field(name="牌義", value= "權杖四正位代表你現在努力已經有了成果，也是應該好好享受自己的成果，這個時候應該要放鬆心情，在穩定中求發展。你可以慶祝自己的勞動成果，考試過關，業績突出，結果很理想。", inline=True)

        embed52=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed52.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed52.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-04.jpg")
        embed52.add_field(name="你今天ㄉ牌是", value="【權杖四 逆位】", inline=False)
        embed52.add_field(name="牌義", value= "權杖四逆位代表你家庭溝通有障礙，不和諧，家庭成員關係緊張，與愛人不和，分手，沒有結果的戀情。你在學業上的表現很穩定，也少有遇到什麼問題，所以只要保持原本該有的實力，就不用特別提心學業方面的問題。", inline=True)

        embed53=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed53.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed53.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-05.jpg")
        embed53.add_field(name="你今天ㄉ牌是", value="【權杖五 正位】", inline=False)
        embed53.add_field(name="牌義", value= "權杖五正位代表你在朋友當中常常與人起爭執，而且他們也很愛和你吵，大家真的是不打不相識，但是你也沒有什麼真心的朋友。你在學業上十分努力，但是目前還看不到明顯的成果，所以你應該檢驗自己的學習方法，是否有應該修正的地方。", inline=True)

        embed54=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed54.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed54.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-05.jpg")
        embed54.add_field(name="你今天ㄉ牌是", value="【權杖五 逆位】", inline=False)
        embed54.add_field(name="牌義", value= "逆位代表你對未來發展產生分歧，問題是逃避可不是好辦法。在你的內心其實是很抗拒現在的學習環境，也許是討厭老師、同學或某一個個科目，因此就很難把該學的東西學好。", inline=True)

        embed55=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed55.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed55.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-06.jpg")
        embed55.add_field(name="你今天ㄉ牌是", value="【權杖六 正位】", inline=False)
        embed55.add_field(name="牌義", value= "權杖六正位代表你目前在學業上的表現非常優秀，之前的付出在這個時候也都看到了成果，也很有可能在各種比賽中贏得勝利。應該發揮你的影響力，你可以讓其他的朋友幫你說好話，在適當的時候再親自予以說明，相信對方一定會接受的", inline=True)

        embed56=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed56.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed56.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-06.jpg")
        embed56.add_field(name="你今天ㄉ牌是", value="【權杖六 逆位】", inline=False)
        embed56.add_field(name="牌義", value= "權杖六逆位代表你失寵，暫時沒有人追求，努力白費，沒有得到回應。而且你十分擔心自己工作的狀況，因為問題已經大到不是你自己可以解決的了，也可能是其他人在背後拖你的後腿。", inline=True)

        embed57=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed57.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed57.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-07.jpg")
        embed57.add_field(name="你今天ㄉ牌是", value="【權杖七 正位】", inline=False)
        embed57.add_field(name="牌義", value= "權杖七正位代表你有令人羨慕的事業，遭遇措手不及的競爭，匆忙的應對，艱苦奮鬥。你應該對朋友有更多的包容，而不是立刻指出他們的錯誤，如果你能擇善而從之，相信到最後朋友都會贊同你的。", inline=True)

        embed58=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed58.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed58.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-07.jpg")
        embed58.add_field(name="你今天ㄉ牌是", value="【權杖七 逆位】", inline=False)
        embed58.add_field(name="牌義", value= "權杖七逆位代表你競爭中失敗了，不堅持自己的觀點，主見性不強。你在學業上陷入慌亂當中，有太多的事情該做，但是不知從何下手。這個時候應該要用積少成多的辦法，注重將每一步的學習累積起來，經過一段時間的努力，就可以看到明顯的進步。", inline=True)

        embed59=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed59.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed59.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-08.jpg")
        embed59.add_field(name="你今天ㄉ牌是", value="【權杖八 正位】", inline=False)
        embed59.add_field(name="牌義", value= "權杖八正位代表你現在非常忙碌，而且也很要求速度，如果自己不夠努力的話，很快就會被別人追趕過去，所以經常需要拼命。你現在的玩心很重，根本不想唸書，每天都想往外跑，若是不能快點定下心來學習，狀況將會越來越難補救。", inline=True)

        embed60=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed60.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed60.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-08.jpg")
        embed60.add_field(name="你今天ㄉ牌是", value="【權杖八 逆位】", inline=False)
        embed60.add_field(name="牌義", value= "權杖八逆位代表你並沒有足夠地用心在課業上，因此學習的交果也不好，這個時候應該快點收心好好學習，不要再渾水摸魚了。你的人際關係遇到很多問題，常常會和朋友們吵個沒完，其實你現在的狀況並不好，還是要自己去自己的事情。", inline=True)

        embed61=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed61.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed61.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-09.jpg")
        embed61.add_field(name="你今天ㄉ牌是", value="【權杖九 正位】", inline=False)
        embed61.add_field(name="牌義", value= "權杖九正位代表你剛行動就遭遇挫折，而且已經變成在原地踏步的狀況，這個時候即使再怎麼努力，也看不到任何實質進展，這只是一次勇氣的測試，不要放棄。", inline=True)

        embed62=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed62.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed62.set_thumbnail(url="https4://myscith.com/wp-content/uploads/2021/03/tarot-wands-09.jpg")
        embed62.add_field(name="你今天ㄉ牌是", value="【權杖九 逆位】", inline=False)
        embed62.add_field(name="牌義", value= "權杖九逆位代表你現在在學習上遇到重大障礙，而且常覺得怎麼樣都無法學會新東西，其實是因為你腦中已經擠了太多東西了。", inline=True)

        embed63=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed63.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed63.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-10.jpg")
        embed63.add_field(name="你今天ㄉ牌是", value="【權杖十 正位】", inline=False)
        embed63.add_field(name="牌義", value= "權杖十正位代表你現在的工作非常忙，工作的壓力也很大，可能會有過勞的傾向，太多的工作已經讓你無法看清楚事情的真相了。而且你每天忙於自己的事情，反而常常都會忽略了朋友，如果再不重視人際關係的經營，你的朋友將會越來越少。", inline=True)

        embed64=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed64.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed64.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-10.jpg")
        embed64.add_field(name="你今天ㄉ牌是", value="【權杖十 逆位】", inline=False)
        embed64.add_field(name="牌義", value= "權杖十逆位代表你在學業上的遇到很大的困難，對你自己形成很大的心理壓力，這時候應該衡量自己的實力，才能訂出合理的目標。 這個時候應該注重基礎的部分，把基礎打好後面的發展就容易了，因此對於前面有不了解的部分要徹底搞懂。", inline=True)

        embed65=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed65.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed65.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-13.jpg")
        embed65.add_field(name="你今天ㄉ牌是", value="【權杖皇后 正位】", inline=False)
        embed65.add_field(name="牌義", value= "權杖皇后正位代表你現在學習上是一段平穩累積的時期，沒有太多的機會可以投機取巧，一切都要靠自己的努力，以後才會看到成果。團隊聚會的核心，有時候也很感性，會給人留下深刻的印象，外剛內柔。", inline=True)

        embed66=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed66.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed66.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-13.jpg")
        embed66.add_field(name="你今天ㄉ牌是", value="【權杖皇后 逆位】", inline=False)
        embed66.add_field(name="牌義", value= "權杖皇后逆位代表你學業上沒有太多的變化，但是對於自己的表現並不滿意，這個時候應該要更努力地唸書，而不只是消極地羨慕別人。而且你與大家只能維持表面的關係，很難建立深厚的友誼，你對於別人的付出太過計較，別人也很難對你全心付出。 ", inline=True)

        embed67=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed67.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed67.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-14.jpg")
        embed67.add_field(name="你今天ㄉ牌是", value="【權杖國王 正位】", inline=False)
        embed67.add_field(name="牌義", value= "權杖國王正位代表你現在所學的東西對你來說是駕輕就熟，但是由於已經到了進步的瓶頸，所以若是要有所突破，就要有新的創意。而且你擅長傳授工作經驗，生活中的指導者，成就很高，不會隨波逐流。", inline=True)

        embed68=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed68.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed68.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-14.jpg")
        embed68.add_field(name="你今天ㄉ牌是", value="【權杖國王 逆位】", inline=False)
        embed68.add_field(name="牌義", value= "權杖國王逆位代表你學業方面現在面對著很大的壓力，雖然都是你所熟悉的東西，但還是覺得自己做得不夠好，別給自己太大的壓力。並且不要給自己或他人不切實際的願望，目標無法實現，因面子導致失敗。", inline=True)

        embed69=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed69.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed69.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-11.jpg")
        embed69.add_field(name="你今天ㄉ牌是", value="【權杖侍者 正位】", inline=False)
        embed69.add_field(name="牌義", value= "權杖侍者正位代表你有一顆好奇心，需要導師帶你少走彎路。你剛進入一個新的環境，也會認識不少的新朋友，這時應該放開心胸接受各種不一樣的人，才能擴展你的人脈。", inline=True)

        embed70=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed70.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed70.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-11.jpg")
        embed70.add_field(name="你今天ㄉ牌是", value="【權杖侍者 逆位】", inline=False)
        embed70.add_field(name="牌義", value= "權杖侍者逆位代表你在學習的過程中並不快樂，因為有很多部分你無法搞清楚，但是又沒有人可以問，在你心中充滿了疑問和挫折感。你要避免給別人不好的第一印象，否則你就要花很多時間才能去改變大家對你的看法，記得在朋友之間言多必失", inline=True)

        embed71=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed71.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed71.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-12.jpg")
        embed71.add_field(name="你今天ㄉ牌是", value="【權杖騎士 正位】", inline=False)
        embed71.add_field(name="牌義", value= "權杖騎士正位代表你是先動手後動腦，潛力無限，萬事可成。想涉足未知領域，不在乎前方危險，執著於理想目標，感覺可以征服全世界。你的財務狀況並不算很穩定，其中大筆或無法預期的支出佔了過高的比例，應該要多存一些本錢以應付不時之需。", inline=True)

        embed72=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed72.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed72.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-wands-12.jpg")
        embed72.add_field(name="你今天ㄉ牌是", value="【權杖侍者 逆位】", inline=False)
        embed72.add_field(name="牌義", value= "權杖騎士逆位代表你現在學習受到很多外在因素的干擾，自己也會因此而分心，如果不能在這個時候收心努力，接下來就很難補救了。你會與朋友因為理念不合而發生衝突，因此如何找到志同道合的朋友才是最重要的，其他不合的人就不用理會了。", inline=True)
        #寶劍
        embed73=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed73.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed73.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-01.jpg")
        embed73.add_field(name="你今天ㄉ牌是", value="【寶劍一 正位】", inline=False)
        embed73.add_field(name="牌義", value= "寶劍一正位代表其實在同學中你的朋友不是很多，你常常太過主觀而刺傷別人，改變自己才有幫助。現在很有可能發生新的戀情，也面對與之前不同的挑戰，小心處理，避免爭吵。", inline=True)

        embed74=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed74.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed74.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-01.jpg")
        embed74.add_field(name="你今天ㄉ牌是", value="【寶劍一 逆位】", inline=False)
        embed74.add_field(name="牌義", value= "寶劍一逆位代表你失敗的概率很大，奮鬥的路上障礙非常多，事情的發展出乎意料。你在學業上表現不好，因為外力使你無法專心唸書，如果能收心還是來得及。你在同學中並不快樂，甚至覺得自己是多餘的，你應該暫時把人際關係放在一邊，多花一些時間唸書。", inline=True)
        
        embed75=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed75.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed75.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-02.jpg")
        embed75.add_field(name="你今天ㄉ牌是", value="【寶劍二 正位】", inline=False)
        embed75.add_field(name="牌義", value= "寶劍二正位代表你在學業上表現平平，但是其實你自己並不滿意，你常會想要改善自己的學習情況，只是自己沒有什麼行動力。你和同學的關係比較疏離，甚至會有一點逃避與別人建立人際關係，你應該打開自己的心和大家真心做朋友。", inline=True)

        embed76=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed76.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed76.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-02.jpg")
        embed76.add_field(name="你今天ㄉ牌是", value="【寶劍二 逆位】", inline=False)
        embed76.add_field(name="牌義", value= "寶劍二逆位代表你在學業上的表現不太好，覺得自己沒有什麼能力改善。這個時候不要自欺欺人了，現在起要認真檢討自己不足之處。財務狀況不好，需要請教專業人士，會被騙。", inline=True)
        
        embed77=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed77.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed77.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-03.jpg")
        embed77.add_field(name="你今天ㄉ牌是", value="【寶劍三 正位】", inline=False)
        embed77.add_field(name="牌義", value= "寶劍三正位代表你感情受傷，很失望，失去了生活中所一直享有的愛。可能因為考試失利或是其他原因，使你對學業上的表現感到傷心難過，你應該要痛定思痛，反省之後再出發。", inline=True)

        embed78=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed78.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed78.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-03.jpg")
        embed78.add_field(name="你今天ㄉ牌是", value="【寶劍三 逆位】", inline=False)
        embed78.add_field(name="牌義", value= "寶劍三逆位代表你過於敏感，言者無心聽者有意，不安的感覺越來越重，不要害怕說對不起。最近經歷了一段困難時期，你發現自己很難從最近的失落或心碎中走出來，不願意接受別人幫助。", inline=True)
        
        embed79=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed79.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed79.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-04.jpg")
        embed79.add_field(name="你今天ㄉ牌是", value="【寶劍四 正位】", inline=False)
        embed79.add_field(name="牌義", value= "寶劍四正位代表你需要休息一下，以退​​為進，要向對方讓步，反省。凡是要學會做暫時性的讓步，需要自己更獨立，遠離是非之地。", inline=True)

        embed80=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed80.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed80.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-04.jpg")
        embed80.add_field(name="你今天ㄉ牌是", value="【寶劍四 逆位】", inline=False)
        embed80.add_field(name="牌義", value= "寶劍四逆位代表你你累了，要戒掉社交軟件的毒癮，需要休息給自己充電，立刻想做所有的事，不行動會有更大損失。要提醒自己且忽急躁，凡是細細想", inline=True)
        
        embed81=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed81.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed81.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-05.jpg")
        embed81.add_field(name="你今天ㄉ牌是", value="【寶劍五 正位】", inline=False)
        embed81.add_field(name="牌義", value= "寶劍五正位代表你對於自己在學業上的表現十分得意，去參加比賽也很容易獲獎，但是這都只是你時的好處，其實基礎並不穩固。要環視周圍有沒有對你懷由敵意的人，正在墮落，對人際關係產生迷惑", inline=True)

        embed82=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed82.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed82.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-05.jpg")
        embed82.add_field(name="你今天ㄉ牌是", value="【寶劍五 逆位】", inline=False)
        embed82.add_field(name="牌義", value= "寶劍五逆位代表你在人際關第當中很怕與別人發生衝突，也缺乏自己的主見，因此常常會被別人欺負，但是又不知道如何反擊。你現在學業上的表現非常差，或是在重要的考試上遭遇失敗，你應該收拾自己的情緒重新開始，不要被擊倒。", inline=True)
        
        embed83=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed83.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed83.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-06.jpg")
        embed83.add_field(name="你今天ㄉ牌是", value="【寶劍六 正位】", inline=False)
        embed83.add_field(name="牌義", value= "寶劍六正位代表你創傷遲遲沒有辦法痊癒，不肯接受幫助，需要向誤解你的人吐露心聲，離開熟悉的環境。還要再過一陣子才會看到成果，這段時間應該要低調埋頭苦幹，等到時機成熟之後自然就會達到成功。", inline=True)

        embed84=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed84.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed84.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-06.jpg")
        embed84.add_field(name="你今天ㄉ牌是", value="【寶劍六 逆位】", inline=False)
        embed84.add_field(name="牌義", value= "寶劍六逆位代表你需要改變生活，需要中介者幫忙。工作或者學業未完成，歷盡艱難後才會萬事太平。", inline=True)
        
        embed85=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed85.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed85.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-07.jpg")
        embed85.add_field(name="你今天ㄉ牌是", value="【寶劍七 正位】", inline=False)
        embed85.add_field(name="牌義", value= "寶劍七正位代表你被環境所束縛，失去自由，四周有對你的責難，被團隊所孤立，處處掣肘，債務需要長時間償還，自己把自己困住。害怕任何一種選擇都是壞選擇，結果只能原地踏步。", inline=True)

        embed86=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed86.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed86.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-07.jpg")
        embed86.add_field(name="你今天ㄉ牌是", value="【寶劍七 逆位】", inline=False)
        embed86.add_field(name="牌義", value= "寶劍七逆位代表你自我感覺做不好，所以就放棄了嘗試。但危機解除了，終於可以鬆一口氣，生活已經重新開始。你在學習上很有耐心，但是又常常粗心大意，應該要訓練自己學會集中住意力。", inline=True)
        
        embed87=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed87.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed87.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-08.jpg")
        embed87.add_field(name="你今天ㄉ牌是", value="【寶劍八 正位】", inline=False)
        embed87.add_field(name="牌義", value= "寶劍八正位代表你目前在學習上缺乏方向，因此即使想努力也無能為力，你應該認清現在的目標，這樣付出才會有相應的回報，你的財務狀況出現了困境，先看看周邊情況再尋求突破。", inline=True)

        embed88=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed88.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed88.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-08.jpg")
        embed88.add_field(name="你今天ㄉ牌是", value="【寶劍八 逆位】", inline=False)
        embed88.add_field(name="牌義", value= "寶劍八逆位代表你認為自己不會擁有，內心想法過於消極，擺脫束縛，獲得自由。你應該放開心胸，不要為了小事情就鬧脾氣。", inline=True)
        
        embed89=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed89.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed89.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-09.jpg")
        embed89.add_field(name="你今天ㄉ牌是", value="【寶劍九 正位】", inline=False)
        embed89.add_field(name="牌義", value= "寶劍九正位代表你正處在苦難之中或苦難即將來臨，中途夭折，越怕犯錯錯誤越多，需要老師幫助。你感受到非常大的壓力，但是又找不到方法可以解決，這個時候如果找個輔導老師談談應該會有幫助。", inline=True)

        embed90=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed90.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed90.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-09.jpg")
        embed90.add_field(name="你今天ㄉ牌是", value="【寶劍九 逆位】", inline=False)
        embed90.add_field(name="牌義", value= "寶劍九逆位代表你做事優柔寡斷，瀰漫著恐懼感，尋求幫助，妄自菲薄，被嚇退。你常常會不想去上學，可能也對學校有很深的恐懼感，這時應該要勇敢面對這些情況。", inline=True)
        
        embed91=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed91.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed91.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-10.jpg")
        embed91.add_field(name="你今天ㄉ牌是", value="【寶劍十 正位】", inline=False)
        embed91.add_field(name="牌義", value= "寶劍十正位代表你發揮失常，面臨或已經慘敗，撕毀合同，找不到出路，再去找工作，突然失敗。你在學習上應該要完全放棄過去的方法，檢討之後再重新開始，如果沒有破釜沉舟的決心去努力是不可能成功的。", inline=True)

        embed92=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed92.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed92.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-10.jpg")
        embed92.add_field(name="你今天ㄉ牌是", value="【寶劍十 逆位】", inline=False)
        embed92.add_field(name="牌義", value= "寶劍十逆位代表你有東山再起的希望，難受也要把事情做完。人際關係中有瞬間可以成功翻盤的機會，有改善的可能性。", inline=True)
         
        embed93=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed93.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed93.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-11.jpg")
        embed93.add_field(name="你今天ㄉ牌是", value="【寶劍侍者 正位】", inline=False)
        embed93.add_field(name="牌義", value= "正位代表你對新的想法感到興奮，在事情有變之前已察覺，經歷過挫折，已柳暗花明，去尋找新的項目。學會了新的東西，看起來很有希望，但缺乏經驗。", inline=True)

        embed94=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed94.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed94.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-11.jpg")
        embed94.add_field(name="你今天ㄉ牌是", value="【寶劍侍者 逆位】", inline=False)
        embed94.add_field(name="牌義", value= "逆位代表你沒有預見到事情變化，沒有做好準備，做事有漏洞，不想做事情，沒有行動，喜歡提問。一時無力應對強勁的對手，很匆忙的做事情，做事不認真，問題太多惹人生氣。", inline=True)
         
        embed95=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed95.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed95.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-12.jpg")
        embed95.add_field(name="你今天ㄉ牌是", value="【寶劍騎士 正位】", inline=False)
        embed95.add_field(name="牌義", value= "寶劍騎士正位代表你具有挑戰的勇氣和勇往直前的行動力，正在執行任務，直面解決難題，下手太快沒有看情周圍情況，沒有看題就寫答案。對待突發事件不乏手段，有行動力，不乏手腕，做事打折扣。", inline=True)

        embed96=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed96.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed96.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-12.jpg")
        embed96.add_field(name="你今天ㄉ牌是", value="【寶劍騎士 逆位】", inline=False)
        embed96.add_field(name="牌義", value= "寶劍騎士逆位代表你自負，輕狂，做決定較輕率，不經分析與考量，題沒有認真思考，需要你靜下心來，經常犯錯誤。易受情緒支配，朋友不和，沒有足夠的資源，衝動的把他人拖下水。", inline=True)
         
        embed97=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed97.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed97.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-13.jpg")
        embed97.add_field(name="你今天ㄉ牌是", value="【寶劍皇后 正位】", inline=False)
        embed97.add_field(name="牌義", value= "寶劍皇后正位代表你事業如意卻倍感孤獨，或者事業失意，其他方面還可以，接受能力強。說話直接了當，坦率又真實，生活上缺乏的過激行為，強烈的失落感，同情他人分散了自己的注意力。", inline=True)

        embed98=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed98.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed98.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-13.jpg")
        embed98.add_field(name="你今天ㄉ牌是", value="【寶劍皇后 逆位】", inline=False)
        embed98.add_field(name="牌義", value= "寶劍皇后逆位代表你情緒經常失控，扭曲他人想法，關係暖味，把戀人推向情敵。過於盛氣凌人，沒有同情心，不寬容。積極性不高，失去某些支持者。", inline=True)
         
        embed99=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed99.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed99.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-14.jpg")
        embed99.add_field(name="你今天ㄉ牌是", value="【寶劍國王 正位】", inline=False)
        embed99.add_field(name="牌義", value= "寶劍國王正位代表你冷靜且想像力豐富，謹慎到需要勇氣，掌握主導權，控制自己的情緒。有統率力，領導能力出眾，在專業領域內如魚得水。", inline=True)

        embed100=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed100.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed100.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-swords-14.jpg")
        embed100.add_field(name="你今天ㄉ牌是", value="【寶劍國王 逆位】", inline=False)
        embed100.add_field(name="牌義", value= "寶劍國王逆位代表你常遭不正常手段的打擊，處理結果不公平，利用自己的才智傷害他人，無法做決定。你會濫用自己的權力，生活中時常發生自己意想不到的衝突，身邊始終有群很殘酷自私的人，過於嚴厲。", inline=True)
        #聖杯
        embed101=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed101.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed101.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-01.jpg")
        embed101.add_field(name="你今天ㄉ牌是", value="【聖杯一 正位】", inline=False)
        embed101.add_field(name="牌義", value= "聖杯一正位代表你感覺生活很美好，一切順利，新的伙伴。你與朋友之間的感情都很好，也能與大家建立起真心的關係，你能主動地付出，因此大家也會信任你。你在學業上的表現很好，也會在適當時機幫助其它同學。", inline=True)

        embed102=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed102.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed102.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-01.jpg")
        embed102.add_field(name="你今天ㄉ牌是", value="【聖杯一 逆位】", inline=False)
        embed102.add_field(name="牌義", value= "聖杯一逆位代表你的喜悅伴隨著隱憂，需要發洩自己，曾經的快樂消失了。你面對新的學習環境，到現在還沒有很適應，你可以多花一些時間在人際關係上，會對你的課業有間接的幫助。", inline=True)
        
        embed103=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed103.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed103.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-02.jpg")
        embed103.add_field(name="你今天ㄉ牌是", value="【聖杯二 正位】", inline=False)
        embed103.add_field(name="牌義", value= "聖杯二正位代表你很喜歡現在的工作，也會為這個工作主動付出很多，由於在工作當中常常需要與別人合作，所以溝通也很重要。你常常會照顧自己的朋友，和他們相處也會很愉快。", inline=True)

        embed104=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed104.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed104.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-02.jpg")
        embed104.add_field(name="你今天ㄉ牌是", value="【聖杯二 逆位】", inline=False)
        embed104.add_field(name="牌義", value= "聖杯二逆位代表你自私，自視甚高。無法使人信服，關係比較對立。相處中的小問題正在逐漸演變成大問題，這時候應該試著放下自己的成見，才能學到新的東西。", inline=True)
        
        embed105=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed105.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed105.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-03.jpg")
        embed105.add_field(name="你今天ㄉ牌是", value="【聖杯三 正位】", inline=False)
        embed105.add_field(name="牌義", value= "聖杯三正位代表共襄盛舉，獲得創意，團結就是力量。你在學業上的表現很好，也會在成績上反映出來，你常常會因為自己學習的表現得獎，或是因此得到別人的肯定。", inline=True)

        embed106=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed106.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed106.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-03.jpg")
        embed106.add_field(name="你今天ㄉ牌是", value="【聖杯三 逆位】", inline=False)
        embed106.add_field(name="牌義", value= "聖杯三逆位代表你很努力，創造力被抑制，被迫服從群體意志，工作學業繁重。與家人朋友聯繫很少，過度放縱自己，對某些物品上癮，自已有可能是第三者，有關於自已的流言。", inline=True)
        
        embed107=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed107.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed107.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-04.jpg")
        embed107.add_field(name="你今天ㄉ牌是", value="【聖杯四 正位】", inline=False)
        embed107.add_field(name="牌義", value= "聖杯四正位代表你沒有動力，錯過了很多機會，結果是好是壞無所謂。身心俱憊，表現的不關心他人生活，喜歡宅在家裡，不想接受邀請。不願表達自己的真實感受，不想敞開心扉。", inline=True)

        embed108=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed108.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed108.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-04.jpg")
        embed108.add_field(name="你今天ㄉ牌是", value="【聖杯四 逆位】", inline=False)
        embed108.add_field(name="牌義", value= "聖杯四逆位代表你發現新的方法，去找新的機會，脫離了低潮期，尋找新平台。最近還會認識不少新朋友，如果你可以好好與他們交往，也會帶給你很多快樂。", inline=True)
        
        embed109=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed109.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed109.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-05.jpg")
        embed109.add_field(name="你今天ㄉ牌是", value="【聖杯五 正位】", inline=False)
        embed109.add_field(name="牌義", value= "聖杯五正位代表你最近遭遇挫折或損失，繼續奮鬥，東山再起。因此過去的就讓它過去吧，還要繼續未完成的事，沒有辦法挽回損失。", inline=True)

        embed110=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed110.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed110.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-05.jpg")
        embed110.add_field(name="你今天ㄉ牌是", value="【聖杯五 逆位】", inline=False)
        embed110.add_field(name="牌義", value= "聖杯五逆位代表你很後悔，以前沒有打好基礎，過去導到現在的困境，局部錯誤全局被動，做事情想的太簡單，自以為很好卻不好，留戀曾經的輝煌。", inline=True)
        
        embed111=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed111.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed111.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-06.jpg")
        embed111.add_field(name="你今天ㄉ牌是", value="【聖杯六 正位】", inline=False)
        embed111.add_field(name="牌義", value= "聖杯六正位代表你回到熟悉的地方，重溫奮鬥的歷史並展望未來，以前的奮鬥或美好的事還在影響現在的你。聯繫曾經的朋友，想家，與朋友體驗童年的樂趣。", inline=True)

        embed112=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed112.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed112.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-06.jpg")
        embed112.add_field(name="你今天ㄉ牌是", value="【聖杯六 逆位】", inline=False)
        embed112.add_field(name="牌義", value= "聖杯六逆位代表你不關心未來，學習退步，感覺越來越差勁。漸漸的失去了童心，想要未來仍然有好的表現，就要保持過去努力的方法，應該很快就會看到成果了。", inline=True)
        
        embed113=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed113.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed113.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-07.jpg")
        embed113.add_field(name="你今天ㄉ牌是", value="【聖杯七 正位】", inline=False)
        embed113.add_field(name="牌義", value= "聖杯七正位代表也許你覺得自己非常成功，但那只是虛幻的假象，你會有很多理想和抱負，只是絕大部分並不可行。幻想財富，自已認為自己會成功，建議走出想像去做出選擇，選擇要謹慎", inline=True)

        embed114=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed114.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed114.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-07.jpg")
        embed114.add_field(name="你今天ㄉ牌是", value="【聖杯七 逆位】", inline=False)
        embed114.add_field(name="牌義", value= "聖杯七逆位代表你沉迷幻想當中無法自拔，此時此刻是脫離幻想面對現實的分界線。你的選擇太多，使你應接不暇。", inline=True)
        
        embed115=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed115.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed115.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-08.jpg")
        embed115.add_field(name="你今天ㄉ牌是", value="【聖杯八 正位】", inline=False)
        embed115.add_field(name="牌義", value= "聖杯八正位代表你從人群的視線中消失一段時間，悄悄的去做一件大事。雖然你的朋友還不少，但是其實你常常想要一個人就好，你應該勇敢地去做自己想做的事情，不要太被朋友牽絆。", inline=True)

        embed116=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed116.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed116.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-08.jpg")
        embed116.add_field(name="你今天ㄉ牌是", value="【聖杯八 逆位】", inline=False)
        embed116.add_field(name="牌義", value= "聖杯八逆位代表你半途而廢，周邊人對自己不滿意被排擠，事情很不順利。失去追求目標，隨便怎麼樣，離開去逃避而不做出改變。", inline=True)
        
        embed117=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed117.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed117.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-09.jpg")
        embed117.add_field(name="你今天ㄉ牌是", value="【聖杯九 正位】", inline=False)
        embed117.add_field(name="牌義", value= "聖杯九正位代表你滿足，知足常樂，願望實現。物質生活很豐富，揮霍，形勢對你有利。你在學業上的表現非常好，這個時候若是參加競賽或考試，都會有很不錯的表現。", inline=True)

        embed118=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed118.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed118.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-09.jpg")
        embed118.add_field(name="你今天ㄉ牌是", value="【聖杯九 逆位】", inline=False)
        embed118.add_field(name="牌義", value= "聖杯九逆位代表你的願望沒有實現，錯誤百出，不要過度放縱自己，有一定的物質損失。你非常追求完美，但是總是很難達到自己的理想，有時候也因為對自己太有信心以致犯了嚴重錯誤。", inline=True)
        
        embed119=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed119.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed119.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-10.jpg")
        embed119.add_field(name="你今天ㄉ牌是", value="【聖杯十 正位】", inline=False)
        embed119.add_field(name="牌義", value= "聖杯十正位代表你相信自己，不會走別人希望你走的路，獲得最大利益。要用自己熟悉的方法學習，才是最穩固的成功方法，也許有些時候會覺得效果不如預期，但是仍然應該堅持下去。", inline=True)

        embed120=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed120.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed120.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-10.jpg")
        embed120.add_field(name="你今天ㄉ牌是", value="【聖杯十 逆位】", inline=False)
        embed120.add_field(name="牌義", value= "聖杯十逆位代表你你在學習上常常過於理想化，覺得自己應該很快就可以學會，但是又不夠務實地去努力，所以反而會無法跟上進度。或是你價值觀錯誤，忽視家庭，失去友情，人際關係不和。", inline=True)
        
        embed121=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed121.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed121.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-11.jpg")
        embed121.add_field(name="你今天ㄉ牌是", value="【聖杯侍者 正位】", inline=False)
        embed121.add_field(name="牌義", value= "聖杯侍者正位代表你有新的想法或機會，好奇的頭腦，正在努力著。你在學習上非常認真，而且也很愛自由思考，充滿好奇心，所以不僅學習效果好，也因為了解得很深入而可以靈活運用。", inline=True)

        embed122=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed122.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed122.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-11.jpg")
        embed122.add_field(name="你今天ㄉ牌是", value="【聖杯侍者 逆位】", inline=False)
        embed122.add_field(name="牌義", value= "聖杯侍者逆位代表你懷疑自已的能力，正在拖延。你在學習上並不是很認真，每天還是很想要玩，而且只學習自己有興趣的東西，所以在學習上就會無法平衡發展。", inline=True)
        
        embed123=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed123.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed123.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-12.jpg")
        embed123.add_field(name="你今天ㄉ牌是", value="【聖杯騎士 正位】", inline=False)
        embed123.add_field(name="牌義", value= "聖杯騎士正位代表你很和平相處，新的機會再慢慢靠近，生活正慢慢起變化。因美好的未來努力奮鬥，身邊充滿誘惑，但你意識不到。", inline=True)

        embed124=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed124.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed124.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-12.jpg")
        embed124.add_field(name="你今天ㄉ牌是", value="【聖杯騎士 逆位】", inline=False)
        embed124.add_field(name="牌義", value= "聖杯騎士逆位代表你想像力過度活躍，思維跳躍，不切實際。自己沒有做好準備，需要採取行動，計劃趕不上變化。小心欺詐，小心身邊乖巧之人，處境表面很好，但其實很危險。", inline=True)
        
        embed125=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed125.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed125.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-13.jpg")
        embed125.add_field(name="你今天ㄉ牌是", value="【聖杯皇后 正位】", inline=False)
        embed125.add_field(name="牌義", value= "聖杯皇后正位代表你富有同情心，樂於助人，第六感準確。經常換位思考，非常理解他人，是善良而公平的人，感情豐富而細膩，但要節制情緒。", inline=True)

        embed126=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed126.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed126.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-13.jpg")
        embed126.add_field(name="你今天ㄉ牌是", value="【聖杯皇后 逆位】", inline=False)
        embed126.add_field(name="牌義", value= "聖杯皇后逆位代表你沒有辦法信賴身邊的人，為一種尷尬的環境所困，事倍功伴，被心情支配頭腦，去花點時間獨處。性情需要改變，你面臨的困難，往往是壞脾性造成的，要注重口碑和聲譽。", inline=True)
        
        embed127=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed127.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed127.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-14.jpg")
        embed127.add_field(name="你今天ㄉ牌是", value="【聖杯國王 正位】", inline=False)
        embed127.add_field(name="牌義", value= "聖杯國王正位代表你情緒平穩，讓人尊敬，有創造性，常想人所未想的，某方面的專家，在某方面有突出的作為，頭腦冷靜。", inline=True)

        embed128=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed128.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed128.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-cups-14.jpg")
        embed128.add_field(name="你今天ㄉ牌是", value="【聖杯國王 逆位】", inline=False)
        embed128.add_field(name="牌義", value= "聖杯國王逆位代表你的外界壓力很大，失控的邊緣，情緒影響太深。缺乏同情心，道德欠缺，在追逐名利不擇手段，面臨損失。", inline=True)
        #錢幣
        embed129=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed129.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed129.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-01.jpg")
        embed129.add_field(name="你今天ㄉ牌是", value="【錢幣一 正位】", inline=False)
        embed129.add_field(name="牌義", value= "錢幣一正位代表你有新的開始，全新領域。你在學業上的表現還不錯，但是你並沒有花很多力氣就得到這個成果，算是有一點幸運，應該要更用功地累積實力。", inline=True)

        embed130=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed130.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed130.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-01.jpg")
        embed130.add_field(name="你今天ㄉ牌是", value="【錢幣一 逆位】", inline=False)
        embed130.add_field(name="牌義", value= "錢幣一逆位代表你錯過了機會，缺乏計劃遠見，新任務有重大風險。你學業上表現還不錯，但是很多都是用不正當的方法作弊得來的，你應該誠實地面對自己，不要再自欺欺人了。", inline=True)
        
        embed131=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed131.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed131.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-02.jpg")
        embed131.add_field(name="你今天ㄉ牌是", value="【錢幣二 正位】", inline=False)
        embed131.add_field(name="牌義", value= "錢幣二正位代表你日程安排的很滿，工作量很大，正在執行高專注力的工作。麻煩一個接一個，時間很緊張，來回奔波。", inline=True)

        embed132=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed132.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed132.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-02.jpg")
        embed132.add_field(name="你今天ㄉ牌是", value="【錢幣二 逆位】", inline=False)
        embed132.add_field(name="牌義", value= "錢幣二逆位代表你過度承諾，過度保證。超負荷的工作與學習，或貪玩不學習。不要隨著環境狀況變化而搖擺，可以跟著其他同學一起唸書也許會比較專心一些。", inline=True)
        
        embed133=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed133.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed133.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-03.jpg")
        embed133.add_field(name="你今天ㄉ牌是", value="【錢幣三 正位】", inline=False)
        embed133.add_field(name="牌義", value= "錢幣三正位代表團隊合作。你應該把握機會和同學多多討論，聽聽各種不同的想法和做法，這有助於拓展你學習的廣度，也可以得到新的觀念。", inline=True)

        embed134=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed134.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed134.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-03.jpg")
        embed134.add_field(name="你今天ㄉ牌是", value="【錢幣三 逆位】", inline=False)
        embed134.add_field(name="牌義", value= "錢幣三逆位代表你不願合作，意見不合，團隊成員缺乏相互尊重。沒有得到賞識，成長進步的機會不多，推薦跳槽。", inline=True)
        
        embed135=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed135.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed135.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-04.jpg")
        embed135.add_field(name="你今天ㄉ牌是", value="【錢幣四 正位】", inline=False)
        embed135.add_field(name="牌義", value= "錢幣四正位代表你很保守，限制很多。生活中精打細算，失去了很多生活樂趣，過分節約，太過看重財富。你對事情的看法太過主觀，所以很難和朋友達成和解，如果能夠做出有限的讓步，問題就有可能完美地解決。", inline=True)

        embed136=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed136.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed136.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-04.jpg")
        embed136.add_field(name="你今天ㄉ牌是", value="【錢幣四 逆位】", inline=False)
        embed136.add_field(name="牌義", value= "錢幣四逆位代表你貪婪貪心，過度看重財富，超支消費，物質欲膨脹，對錢財貪婪。", inline=True)
        
        embed137=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed137.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed137.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-05.jpg")
        embed137.add_field(name="你今天ㄉ牌是", value="【錢幣五 正位】", inline=False)
        embed137.add_field(name="牌義", value= "錢幣五正位代表你面臨經濟損失，貧窮。正處於困難時期，自我價值遭遇打擊，看到問題卻無法改變。失去經濟保障，因為錢財自尊心受到傷害，尋求幫助就有會有人幫助。", inline=True)

        embed138=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed138.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed138.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-05.jpg")
        embed138.add_field(name="你今天ㄉ牌是", value="【錢幣五 逆位】", inline=False)
        embed138.add_field(name="牌義", value= "錢幣五逆位代表你的經濟復甦，獲得賠償。困難時期結束，有了新的收入來源，有人幫你重新站了起來，重拾希望，擔心錢不夠。", inline=True)
        
        embed139=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed139.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed139.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-06.jpg")
        embed139.add_field(name="你今天ㄉ牌是", value="【錢幣六 正位】", inline=False)
        embed139.add_field(name="牌義", value= "錢幣六正位代表你慷慨大方。人脈關係廣，與人為善，樂善好施，助人為樂，心胸寬廣。要分享才能造就更大的利益，所在以成功之餘也不要忽略了幫助別人。", inline=True)

        embed140=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed140.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed140.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-06.jpg")
        embed140.add_field(name="你今天ㄉ牌是", value="【錢幣六 逆位】", inline=False)
        embed140.add_field(name="牌義", value= "錢幣六逆位代表你只有付出沒有收穫，遇到的事超出自己的能力範圍，為他人利益做出妥協。你現在處於財務上的弱勢，常需要靠別人的照顧，也許在這段期間你可以接受別人的幫忙，但是也要想辦法振作起來。", inline=True)
        
        embed141=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed141.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed141.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-07.jpg")
        embed141.add_field(name="你今天ㄉ牌是", value="【錢幣七 正位】", inline=False)
        embed141.add_field(name="牌義", value= "錢幣七正位代表你有不屈不撓的精神。因辛勤勞作而獲得成功，雖然回報來的比預期要晚。你在學業上的表現還不錯，也已經有一定的成果了，但是現在好像遇到了一個階段的瓶頸，想要突破就要靠創意。", inline=True)

        embed142=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed142.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed142.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-07.jpg")
        embed142.add_field(name="你今天ㄉ牌是", value="【錢幣七 逆位】", inline=False)
        embed142.add_field(name="牌義", value= "錢幣七逆位代表你缺乏長遠眼光，結果不理想。因無知做出輕率的決定，見識不足，不承認失敗，妄想掙扎挺過去。付出了多餘的努力或產能過剩，努力得不到回報，浪費資源。", inline=True)
        
        embed143=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed143.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed143.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-08.jpg")
        embed143.add_field(name="你今天ㄉ牌是", value="【錢幣八 正位】", inline=False)
        embed143.add_field(name="牌義", value= "錢幣八正位代表你正在練習新技能，深造，考取證書，想要成為自己領域專家，目標很偉大。會自我激勵，上進心很強，精益求精，自己會什麼就追求什麼。", inline=True)

        embed144=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed144.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed144.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-08.jpg")
        embed144.add_field(name="你今天ㄉ牌是", value="【錢幣八 逆位】", inline=False)
        embed144.add_field(name="牌義", value= "錢幣八逆位代表你有完美主義，或用的方法不對。本事沒有用到正經地方，野心受到挫折，要求完美適應性差，沒有真才實學。非常努力但結果相反，為了金錢不擇手段", inline=True)
        
        embed145=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed145.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed145.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-09.jpg")
        embed145.add_field(name="你今天ㄉ牌是", value="【錢幣九 正位】", inline=False)
        embed145.add_field(name="牌義", value= "錢幣九正位代表你財富自由，自信自律可獲得成功。你並沒有花很多時間在學習，反而對課外的東西比較感興趣，要小心保持平衡。", inline=True)

        embed146=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed146.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed146.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-10.jpg")
        embed146.add_field(name="你今天ㄉ牌是", value="【錢幣九 逆位】", inline=False)
        embed146.add_field(name="牌義", value= "錢幣九逆位代表你工作過度。質疑自已的能力，你的專業是否有價值，沒有休息的時間。你需要向自己投資，別對自己不滿意。", inline=True)
        
        embed147=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed147.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed147.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-10.jpg")
        embed147.add_field(name="你今天ㄉ牌是", value="【錢幣十 正位】", inline=False)
        embed147.add_field(name="牌義", value= "錢幣十正位代表你正在階段的頂點，成就達成，職業為你帶來成功，為未來的成功打下基礎。目前經濟很安全，團隊事業發展良好。", inline=True)

        embed148=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed148.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed148.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-10.jpg")
        embed148.add_field(name="你今天ㄉ牌是", value="【錢幣十 逆位】", inline=False)
        embed148.add_field(name="牌義", value= "錢幣十逆位代表你遭受損失，缺德賺錢。你在學習上的反應比較慢一些，所以需要加倍努力才能跟上其他同學，你應該持續努力學習，千萬不要選擇放棄。", inline=True)
        
        embed149=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed149.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed149.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-11.jpg")
        embed149.add_field(name="你今天ㄉ牌是", value="【錢幣侍者 正位】", inline=False)
        embed149.add_field(name="牌義", value= "錢幣侍者正位代表你求知欲旺盛，有新的教育機會，學會新的技能。有很大的成長空間，也有很多東西可以學會，所以應該把握所有學習機會，好好充實自己。", inline=True)

        embed150=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed150.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed150.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-11.jpg")
        embed150.add_field(name="你今天ㄉ牌是", value="【錢幣侍者 逆位】", inline=False)
        embed150.add_field(name="牌義", value= "錢幣侍者逆位代表你缺乏進展，停滯不前，但可以汲取教訓，總結經驗。目前事情可能處於設想階段，你會擔心沒有足夠的資源，感覺失敗沒有意義，知識面窄，一知半解。", inline=True)
        
        embed151=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed151.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed151.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-12.jpg")
        embed151.add_field(name="你今天ㄉ牌是", value="【錢幣騎士 正位】", inline=False)
        embed151.add_field(name="牌義", value= "錢幣騎士正位代表你勤奮工作，有自自己的原則。承擔未來的責任，特別注重細節，步步為營，累了也不會停止，很自律。你在學業上的表現很突出，這是你長時間努力得來的成果，你已經為未來打下了良好的基礎。", inline=True)

        embed152=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed152.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed152.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-12.jpg")
        embed152.add_field(name="你今天ㄉ牌是", value="【錢幣騎士 逆位】", inline=False)
        embed152.add_field(name="牌義", value= "錢幣騎士逆位代表你面臨瓶頸，需要按照計劃執行，沒有創新能力，做事三分鐘熱度。生活懈怠，被生活鎖事所困。最近都不太想唸書，在考試的時候容易粗心大意。", inline=True)
        
        embed153=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed153.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed153.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-13.jpg")
        embed153.add_field(name="你今天ㄉ牌是", value="【錢幣皇后 正位】", inline=False)
        embed153.add_field(name="牌義", value= "錢幣皇后正位代表你養育或包養別人。善於照顧他人，關心家庭，有足夠的時間養育愛人。你成熟又獨立，有穩定的收入，樂於助人，好客，值得信賴的人。", inline=True)

        embed154=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed154.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed154.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-13.jpg")
        embed154.add_field(name="你今天ㄉ牌是", value="【錢幣皇后 逆位】", inline=False)
        embed154.add_field(name="牌義", value= "錢幣皇后逆位代表你經濟獨立，但工作與家庭衝突。現在需要非常專注，細心檢查所有的步驟是否正確，當中可能存在很多錯誤的陷阱。", inline=True)
        
        embed155=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed155.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed155.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-14.jpg")
        embed155.add_field(name="你今天ㄉ牌是", value="【錢幣國王 正位】", inline=False)
        embed155.add_field(name="牌義", value= "錢幣國王正位代表自我控制，嚴格要求。你可以為他人提供建議，擅於長期投資，物質財富的成功。你在學業上的表現很好，也得到老師及同學們的肯定，你會用最快速有效的辦法學習，所以也不用花費太多時間。", inline=True)

        embed156=discord.Embed(title="每日塔羅牌", color=0x9a7a9f)
        embed156.set_author(name="塔可巫師aka解牌巫師", icon_url="https://images.emojiterra.com/twitter/v14.0/512px/1f52e.png")
        embed156.set_thumbnail(url="https://myscith.com/wp-content/uploads/2021/03/tarot-pentacles-14.jpg")
        embed156.add_field(name="你今天ㄉ牌是", value="【錢幣國王逆位】", inline=False)
        embed156.add_field(name="牌義", value= "錢幣國王逆位代表你沒有商業頭腦，沉迷於金錢與社會地位，固執。你現在處理的事出現了很大的漏洞，之前的問題也慢慢地浮現出來，也許必須要投入更多的資源，才能安全渡過這個危機。", inline=True)
                
        embed = [embed1,embed2,embed3,embed4,embed5,embed6,embed7,embed8,embed9,embed10,
        embed11,embed12,embed13,embed14,embed15,embed16,embed17,embed18,embed19,embed20,
        embed21,embed22,embed23,embed24,embed25,embed26,embed27,embed28,embed29,embed30,
        embed31,embed32,embed33,embed34,embed35,embed36,embed37,embed38,embed39,embed40,
        embed41,embed42,embed43,embed44,embed45,embed46,embed47,embed48,embed49,embed50,
        embed51,embed52,embed53,embed54,embed55,embed56,embed57,embed58,embed59,embed60,
        embed61,embed62,embed63,embed64,embed65,embed66,embed67,embed68,embed69,embed70,
        embed71,embed72,embed73,embed74,embed75,embed76,embed77,embed78,embed79,embed80,
        embed81,embed82,embed83,embed84,embed85,embed86,embed87,embed88,embed89,embed90,
        embed91,embed92,embed93,embed94,embed95,embed96,embed97,embed98,embed99,embed100,
        embed101,embed102,embed103,embed104,embed105,embed106,embed107,embed108,embed109,embed110,
        embed111,embed112,embed113,embed114,embed115,embed116,embed117,embed118,embed119,embed120,
        embed121,embed122,embed123,embed124,embed125,embed126,embed127,embed128,embed129,embed130,
        embed131,embed132,embed133,embed134,embed135,embed136,embed137,embed138,embed139,embed140,
        embed141,embed142,embed143,embed144,embed145,embed146,embed147,embed148,embed149,embed150,
        embed151,embed152,embed153,embed154,embed155,embed156]

        await message.channel.send(embed=random.choice(embed))

client.run('YOUR_TPKEN')
