# Projeto 1: Web Scraping - Sistemas Web 


## Resumo

Projeto de Web Scraping utilizando linguagem Python e gravação do conteúdo no banco de dados MongoDB.

## Versão do Python

- Python 3.8.9

## Requerimentos

Todas bibliotecas e pacotes necessários para execução do projeto estão registradas no arquivo requirements.txt

## MongoDB

Instale o aplicativo MongoDB Compass.

Com o aplicativo instalado, deve-se conectar a url local = mongodb://localhost:27017/

Ao rodar o arquivo book.py, será criado o banco de dados chamado web com a coleção chamada livros com os dados.

## Para rodar o nosso programa, siga os seguintes passos

Abra o terminal e rode os seguintes comandos:

1° Ambiente virtual

Certifique-se de que você está trabalhando em um ambiente virtual isolado para evitar conflitos com outras instalações Python
Se você ainda não criou um ambiente virtual, pode fazê-lo usando o seguinte comando:

- python -m venv myenv

E em seguida, ative o ambiente virtual:

- myenv\Scripts\activate

2° Instalar as dependências

- pip install -r requirements.txt

- pip install requests bs4 pandas forex_python pymongo flask 

3° Realizar a busca na página web e adicionar as informações ao banco

- python book.py

4° Rodar a api para ter acesso a url do projeto

- python app.py
