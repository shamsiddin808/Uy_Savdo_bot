import requests
from data.config import BOT_TOKEN

API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates'

response = requests.get(API_URL)

if response.status_code == 200:
    data = response.json()
    for result in data['result']:
        if 'channel_post' in result:
            channel_id = result['channel_post']['chat']['id']
            print(f"Kanal ID si: {channel_id}")
            break
else:
    print(f"Xatolik: {response.status_code}")
