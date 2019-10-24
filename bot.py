import requests

def telegram_bot_sendtext(bot_message):
    bot_token = '1067881398:AAFz_hWA-qqvpmIvenBgw8WASZdX2J1t2Ys'
    bot_chatID = '354467348'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

