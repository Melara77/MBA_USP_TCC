

#Importando as bibliotecas utilizadas
import json
import pandas as pd
import numpy as np 
import datetime 
from urllib.request import urlopen, Request


# Definindo as variáveis da url p/ efetivação da busca
urlBase = 'http://www.webmotors.com.br/api/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}

print('Obtendo os dados, aguarde!')

# Extraindo os dados
data = [];
Specs = [];
 
#Caso necessário alterar o range para buscar a quantidades de paginas desejada. Exemplo Pagina 1 à 100 diretamente ou por intervalor ex: 1 a 10, 11 a 20...etc
for i in range(91, 100):

    url = urlBase + 'search/bike?url=https://www.webmotors.com.br/motos%2Fsp%3Festadocidade%3DS%25C3%25A3o%2520Paulo%26tipoveiculo%3Dmotos&actualPage='+str(i)

    req = Request(url, headers=headers)

    temp = json.load(urlopen(req))

    data += temp["SearchResults"]

# Salvando os dados extraídos em arquivo formato json
with open('C:/Users/maicon.melara/Documents/Python/data/data-bikes.json', 'w', encoding='utf-8') as f:
   json.dump(data, f, ensure_ascii=False, indent=4)


