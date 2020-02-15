import telebot 

token = "1043599060:AAFNgKZFLs3i8LnBX8YYeMvvQmB4ObSk0Cg"
bot = telebot.TeleBot(token)

user_wish = input("Кого вы хотите посмотреть, котика или песика?").lower()
@bot.message_handler(commands=['photo']) 
def send_picture(message): 
    if user_wish == "котик":
        cat_img = open('images/Котик.jpg', 'rb')
        bot.send_photo(message.chat.id, cat_img)
 
    elif user_wish == "песик":
        dog_img = open('images/Песик.jpg', 'rb')
        bot.send_photo(message.chat.id, dog_img)
    
bot.polling()
