import requests
import threading
def requisicao(url):
    headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html"}
    try:
        end = requests.get(url, headers=headers, verify=True, timeout=60)
        if end.status_code == 200:
            return end.text
    except requests.exceptions.ConnectionError as erro1:
             print("Hosts ,Sem serviço")
    except KeyboardInterrupt:
        print("parado pelo usuario")




