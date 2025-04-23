import discord
from discord.ext import commands
import os
from model import get_class

# Görsellerin kaydedileceği klasör
IMAGE_DIR = "images"
os.makedirs(IMAGE_DIR, exist_ok=True)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

@bot.command()
async def yukle(ctx):
    attachments = ctx.message.attachments

    if not attachments:
        await ctx.send("Herhangi bir görsel bulamadım. Lütfen komutu kullanırken bir görsel ekleyin!")
        return

    for attachment in attachments:
        file_name = attachment.filename
        file_path = os.path.join(IMAGE_DIR, file_name)

        try:
            await attachment.save(file_path)
            
            
            # Modeli çalıştır
            model_path = "keras_model.h5"
            labels_path = "labels.txt"
            class_name, confidence = get_class(file_path, model_path, labels_path)


            messages = {
    "0 balık": "BALIKLARR\n\n"
            "Balıklara bakımı kolaydır ve beslemeside bait "
            "\n\n",
    "1 karadees": "kaarades\n\n"
            "yenilebilen bir hayvandır"
            "\n\n",
    "2 köpek balığı": "köpekbalığı\n\n"
            "seni yiyebilir görünce bence kaç"
            "\n\n",
    "3 yunus": "Yunus\n\n"
            "baya tatlı bir hayvandır"
            "\n\n",
    "4 deniz atı":"deniz atı\n\n"
            "ata benziyoo"
            "\n\n",
    "5 deniz kaplumbağası":"deniz kaplumbağası\n\n"
            "uzun yıllar yaşar"
            "\n\n",
}

            # class_name'in küçük harf olup olmadığını kontrol et
            
            special_message = messages.get(class_name, "Bu sınıf için özel bir mesaj yok.")
            
            await ctx.send(f"🔍 Tahmin: `{class_name[5:]}` (%{confidence*100:.2f} güven) {special_message}")
        except Exception as e:
            await ctx.send(f"⚠️ Hata oluştu: {str(e)}")
    


bot.run("MTM2MTAzMTk3OTA5MjQxNDY3NQ.GumsuO.JD0Svu94VscjzX4fLQgW2QmtV51vvl5LB8seJg")