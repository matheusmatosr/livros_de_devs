import requests
from bs4 import BeautifulSoup
import pandas as pd
from forex_python.converter import CurrencyRates

# Link de acesso
url = "https://books.toscrape.com/"
page_catalogue = "https://books.toscrape.com/catalogue/page-"

# Obtém a taxa de conversão de EUR para BRL
cr = CurrencyRates()
eur_to_brl = cr.get_rate('EUR', 'BRL')

# Carregar conteúdo da página com tratamento das exceções
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Verifica se houve um erro na requisição
except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("Something went wrong:", err)

# Continuar apenas se a resposta for bem sucedida
if response.status_code == 200:
    response_page = BeautifulSoup(response.text, 'html.parser')
    
    # Obtem o total de páginas
    text_num_pages = response_page.find('li', {'class': 'current'}).text.strip()
    total_pages = int(text_num_pages.split()[3])
    
    catalogo_livros = []  # Lista para obter todos os livros
    
    # Percorrer todas as páginas
    for num_page in range(1, total_pages + 1):
        # Acesso as páginas
        pagina = f"{page_catalogue}{num_page}.html"

        # Carregar conteúdo da página com tratamento de exceções
        try:
            response = requests.get(pagina, headers=headers)
            response.raise_for_status()  # Verifica se houve um erro na requisição
        except requests.exceptions.HTTPError as errh:
            print("HTTP Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("Something went wrong:", err)

        # Continuar apenas se a resposta for bem sucedida
        if response.status_code == 200:
            # Recebe boxes dos livros
            response_page = BeautifulSoup(response.text, 'html.parser')
            livros = response_page.find_all('article', {'class': 'product_pod'})
    
            # Percorre pelos boxes dos livros
            for livro in livros:
                # Obtem titulo, preço, link e imagem de cada livro
                titulo = livro.find('h3').a['title']
                preco = float(livro.find('p', {'class': 'price_color'}).text.lstrip('Â£'))
                ancora = livro.find('a')['href']
                link = f"{url}catalogue/{ancora}"
                img_relative_url = livro.find('img')['src']
                
                titulo = titulo.split(':')[0].split('(')[0].strip()
                img_url = f"{url}{img_relative_url}"

                # Converte o preço de Euro para Real
                preco_brl = round(preco * eur_to_brl, 2)

                # Dicionário para representar o livro
                livro_doc = {
                    'Título': titulo,
                    'Preço': preco_brl,
                    'Link': link,
                    'Imagem': img_url
                }

                # Adicione o documento do livro à lista
                catalogo_livros.append(livro_doc)