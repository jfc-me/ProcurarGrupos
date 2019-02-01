

import re
import requests
import threading
from tags.invalid import h_3
from bs4 import BeautifulSoup
from urls_google.listas_urls_googles import hosts

class Facebook:

    def iniciadaBusca(self,palavra, quantidade_pagina):
        if isinstance(quantidade_pagina, int):
            url =  "/search?q={}&num={}".format(palavra, quantidade_pagina)

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
                    soup = BeautifulSoup(page, 'html.parser' )
                    tag = soup.find_all(h_3, class_='r' )
                    for links in tag:
                        try:
                            link_facebook = re.search('url\?q=(.+?)\&sa', links.a['href']).group(1)
                            print(link_facebook)
                        except:
                            continue


                except requests.exceptions.ConnectionError:
                    print("Sem Resultado, aguarde estabelecer o serviço")

                else:
                    print("Verificar campos")



            threadObj = threading.Thread(target=requisicao)
            threadObj.start()
        hostsAtivos(*hosts)



gTudo = Facebook()
gTudo.iniciadaBusca(palavra="site:pt-br.facebook.com/groups", quantidade_pagina=1)
