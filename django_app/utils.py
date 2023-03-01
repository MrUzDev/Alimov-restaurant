from twilio.rest import Client
import requests


TOKEN = '6107202586:AAFDSRF0eK8nA444SIOADp51zaj1a1TgIps'
CHAT_ID = '-1001831938868'


def send_telegram_message(message):
    requests.post(
        url=f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}')


def sms_verification(client_number, client_name, number_of_guests):
    # account_sid = 'ACe396bfab58467db3c34a6a93cef56443'
    # auth_token = '2f5cb3b73a979ada760caf9389e86728'
    # client = Client(account_sid, auth_token)
    # phone_number = client_number
    # message = client.messages.create(
    #     to=phone_number,
    #     from_='+12763303362',
    #     body=f'Здравствуйте {client_name}! Ваш заказ был принят и мы рассматриваем самое лучшее место для вашего отдыха!')
    tg_bot_body = f'У нас новый клиент!\nКлиент: {client_name},\nНомер клиента: {client_number},\nКоличество гостей: {number_of_guests}'
    send_telegram_message(tg_bot_body)
    # return message.sid