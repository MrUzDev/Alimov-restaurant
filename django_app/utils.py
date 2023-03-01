from eskiz_sms import EskizSMS
from twilio.rest import Client
import requests


TOKEN = '6107202586:AAFDSRF0eK8nA444SIOADp51zaj1a1TgIps'
CHAT_ID = '-1001831938868'


def send_telegram_message(message):
    requests.post(
        url=f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}')


def sms_verification(client_number, client_name, number_of_guests):

    your_saved_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjMwMjQsInJvbGUiOiIiLCJkYXRhIjp7ImlkIjozMDI0LCJuYW1lIjoiSnVyYWV2IEF6YW1qb24gQWR4YW0gbydnJ2xpIiwiZW1haWwiOiJqb3JhZXYuYXphbTEyNTJAZ21haWwuY29tIiwicm9sZSI6IiIsImFwaV90b2tlbiI6ImV5SjBlWEFpT2lKS1YxUWlMQ0poYkdjaU9pSklVekkxTmlKOS5leUp6ZFdJaU9qTXdNalFzSW5KdmJHVWlPaUlpTENKa1lYUmhJanA3SW1sa0lqb3pNREkwTENKdVlXMWxJam9pU25WeVlXVjJJRUY2WVcxcWIyNGdRV1I0WVcwZ2J5ZG5KMnhwSWl3aVpXMWhhV3dpT2lKcWIzSmhaWFl1WVhwaGJURXlOVEpBWjIxaGFXd3VZMjl0SWl3aWNtOXNaU0k2SWlJc0ltRndhVjkwYjJ0bGJpSTZiblZzYkN3aWMzUmhkSFZ6SWpvaVlXTjBhWFpsSWl3aWMyMXpYMiIsInN0YXR1cyI6ImFjdGl2ZSIsInNtc19hcGlfbG9naW4iOiJlc2tpejIiLCJzbXNfYXBpX3Bhc3N3b3JkIjoiZSQkayF6IiwidXpfcHJpY2UiOjUwLCJ1Y2VsbF9wcmljZSI6MTE1LCJ0ZXN0X3VjZWxsX3ByaWNlIjowLCJiYWxhbmNlIjo1MDAwLCJpc192aXAiOjAsImhvc3QiOiJzZXJ2ZXIxIiwiY3JlYXRlZF9hdCI6IjIwMjMtMDMtMDFUMTE6MTM6NTkuMDAwMDAwWiIsInVwZGF0ZWRfYXQiOiIyMDIzLTAzLTAxVDExOjE2OjU4LjAwMDAwMFoifSwiaWF0IjoxNjc3NjczMTcxLCJleHAiOjE2ODAyNjUxNzF9.Tvypseljh76kwmWqRS4rLvtbrTvY5CknYyrlEA_SUiY'
    eskiz = EskizSMS('joraev.azam1252@gmail.com', 'YdqyPL44HcuGtUlMFHorYrNPuWEGKQ5HqkAlRHjH')
    eskiz.token.set(your_saved_token)

    body = f'Здравствуйте {client_name}! Ваш заказ был принят и мы рассматриваем самое лучшее место для вашего отдыха!'
    eskiz.send_sms(client_number, message=body)

    tg_bot_body = f'У нас новый клиент!\nКлиент: {client_name},\nНомер клиента: {client_number},\nКоличество гостей: {number_of_guests}'
    send_telegram_message(tg_bot_body)


















