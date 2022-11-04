import requests

def send_to_telegram(message):

    apiToken = '5704612050:AAEIS4ZcP19CDgZ5-g3uNFxw64Dvsmn0HRA'
    chatID = '-819110848'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

send_to_telegram("Здравствуйте!")
