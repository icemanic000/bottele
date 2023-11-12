
import requests
from bs4 import BeautifulSoup
from telegram import Bot, InputFile

# Укажите токен вашего бота
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = Bot(token=TOKEN)

# URL для вытягивания изображения
target_url = 'YOUR_TARGET_WEBSITE_URL'

def get_image_url():
    response = requests.get(target_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Используйте соответствующие селекторы для вашего сайта
    image_element = soup.select_one('YOUR_IMAGE_SELECTOR')
    if image_element and 'src' in image_element.attrs:
        return image_element['src']
    return None

def send_image_to_channel(image_url, channel_id):
    image_data = requests.get(image_url).content
    bot.send_photo(chat_id=channel_id, photo=InputFile(io.BytesIO(image_data)))

def main():
    image_url = get_image_url()
    if image_url:
        # Укажите ID вашего телеграм-канала
        channel_id = '@YOUR_CHANNEL_ID'
        send_image_to_channel(image_url, channel_id)
    else:
        print("Не удалось получить URL изображения.")

if __name__ == "__main__":
    main()