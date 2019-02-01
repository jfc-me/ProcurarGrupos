from urls_google.listas_urls_googles import hosts
from tags.invalid import tag_span, tag_span_fim,tag_b, tag_b_fim, tag_br_fim
import requests
import bs4
import re
import threading
class Whatsapp:

    def filtro(self,pesuisar, quantidade_paginas):
        url = "/search?q=intext:%22https://chat.whatsapp.com/invite/%22%20intitle:%22{}%22&num={}".format(pesuisar,quantidade_paginas).replace( ' ', '%20')


        def hostsAtivos(*hostsGoogle):
            for listaAtivos in range(len(hostsGoogle)):
                integrar = hostsGoogle[listaAtivos]
                pesquisagoogle = integrar + url
                print(pesquisagoogle)
            def requisicao():
                try:
                    headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html"}
                    response = requests.get(pesquisagoogle,  headers=headers, verify=True, timeout=60)
                    page = response.text
                    sou = bs4.BeautifulSoup(page, 'html.parser')
                    for caracters in sou.find_all('span', class_='st'):
                        grupo_encontrado = re.sub(tag_span, '', str(caracters))
                        filtro_group_p_1 = re.sub(tag_b, '', grupo_encontrado)
                        filtro_group_p_2 = re.sub(tag_b_fim, '',filtro_group_p_1.replace('...', '').replace(tag_span_fim, ''))

                        grupo_whatsapp = re.sub(tag_br_fim, '', filtro_group_p_2)

                        primeira_letra = grupo_whatsapp.find("https://chat")
                        ultima_letra = grupo_whatsapp.find(' ', primeira_letra)
                        resultados = grupo_whatsapp[primeira_letra:ultima_letra]
                        print(resultados)
                except requests.exceptions.ConnectionError:
                        print("Serviço Inoperante, nao a resultados")

            #requisicao()
            threadObj = threading.Thread(target=requisicao)
            threadObj.start()
        hostsAtivos(*hosts)



x = Whatsapp()
x.filtro('vendas',10)