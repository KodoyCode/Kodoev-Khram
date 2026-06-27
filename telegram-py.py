
import telebot

TOKEN = ""

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])

def start(message):
    bot.send_message(message.chat.id, "HELLO")



@bot.message_handler(commands=["help"])

def help(message):
    bot.send_message(message.chat.id, "How can I help you?")
    


@bot.message_handler(commands=["more"])

def more(message):
    bot.send_message(message.chat.id, "This is a test telegram bot by Wempt_23")



@bot.message_handler(commands=["image"])

def image(message):
    with open("kal.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="Random-ahh image from internet")



bot.infinity_polling()





