import telebot
import os
import random
import requests
  
images = os.listdir('images')

bot = telebot.TeleBot("7589067719:AAFBMTTF5DQNLiwJQ_EoMqVqEZ58zuk1HxI")

@bot.message_handler(commands=['meme'])
def send_mem(message):
    random_image = random.choice(images)
    with open(f'images/{random_image}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

def get_duck_image_url(): 
        url = 'https://random-d.uk/api/random'
        res = requests.get(url)
        data = res.json()
        return data['url']
    
    
@bot.message_handler(commands=['duck'])
def duck(message):
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)

def get_dog_image_url():
    try:
        url = 'https://random.dog/woof.json'
        res = requests.get(url)
        data = res.json()
        return data['url']
    except Exception as e:
        return "упс! не удалось получить изображение собаки"

def get_fox_image_url():
    try:
        url = 'https://randomfox.ca/floof/'
        res = requests.get(url)
        data = res.json()
        return data['url']
    except Exception as e:
        return "упс! не удалось получить изображение лисы"

@bot.message_handler(commands=['animal'])
def animal(message):
  choice = random.choice([1, 2])
  image_url = get_dog_image_url() if choice == 1 else get_fox_image_url()
  bot.reply_to(message, image_url)

bot.infinity_polling()
