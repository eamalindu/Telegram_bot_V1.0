import telebot

API_KEY = '1941480414:AAHY5GQa-zJp5C71DOjwyupq1fYQdBuE7IM'
bot = telebot.TeleBot(API_KEY)

print("Bot Status : Booting")
print("Bot Status : Online")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi there ! 👋\nSend me /ICT to continue\nSend /help To find out what I can do\n\nCreated by Malindu Prabodhitha | 2021 ©")

@bot.message_handler(commands=['Greet'])
def greet(message):
  bot.reply_to(message, "Hey! \nHow’s it going?")

@bot.message_handler(commands=['SelfDestruct'])
def boom(message):
  bot.reply_to(message, "I will Self Destruct in 5 Seconds!")
  bot.send_message(message.chat.id, "5")
  bot.send_message(message.chat.id, "4")
  bot.send_message(message.chat.id, "3")
  bot.send_message(message.chat.id, "2")
  bot.send_message(message.chat.id, "1")
  bot.send_message(message.chat.id, "Boom! 💥")
  bot.send_message(message.chat.id, "Ha Ha just Kidding 😂")


@bot.message_handler(commands=['Welcome'])
def welcome(message):
  bot.reply_to(message, "Hi !\nMalindu sends his regards!")
  bot.send_message(message.chat.id, "Wanna see a Picture ?")
  img = open('RE3KCxd.jpg', 'rb')
  bot.send_photo(message.chat.id, img)
  img.close()


@bot.message_handler(commands=["ICT"])
def esoft(message):
  bot.send_message(message.chat.id, "දීපව්‍යාප්ත නොමිලේ DVD බෙදා දීමේ වැඩසටහන - 2021")
  img = open('ESOFT.jpg', 'rb')
  pdf = open('ReadMe.pdf', 'rb')
  bot.send_photo(message.chat.id, img)
  bot.send_document(message.chat.id, pdf)
  img.close()


@bot.message_handler(commands=["help"])
def help(message):
  bot.send_message(message.chat.id,"Help Lits \nThese are the things that I can helped you with \n /ICT - To get DVD Links 📀 \n /Greet - Greeting Message 👋 \n /Welcome - Welcomes You to Group 🤝 \n /SelfDestruct - I will go Boom !! 💥 \n /Malindu - Details about my creator 👨‍💻")


@bot.message_handler(commands=["Malindu"])
def malindu(message):
  bot.send_message(message.chat.id,"Details About My Creator \n Name - Malindu Prabodhitha \n Contact - eamalindu@gmail.com \n\n\n I was Created on 17th of July 2021 \n © Malindu Prabodhitha | 2021")

@bot.message_handler(commands=["stop"])
def stop(message):
  bot.send_message(message.chat.id,"Attempting to power down")
  bot.send_message(message.chat.id,"Power Down Sucessfully")
  bot.send_message(message.chat.id,"5")
  bot.send_message(message.chat.id,"4")
  bot.send_message(message.chat.id,"3")
  bot.send_message(message.chat.id,"2")
  bot.send_message(message.chat.id,"1")
  bot.send_message(message.chat.id,"All systems back online")
  bot.send_message(message.chat.id,"Power Down Failed! Error : 503")

#use this code to spam (duplicate all the msgs)
#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
    #bot.reply_to(message, message.text)
 
bot.polling()
