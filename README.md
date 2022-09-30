# Boas-vindas ao repositório do Tech News

<details>
  <summary><strong>👨‍💻 O que foi desenvolvido</strong></summary><br />

  Projeto que tem como principal objetivo fazer consultas em notícias sobre tecnologia(Raspagem de dados).

  As notícias foram obtidas através da raspagem do [_blog da Trybe_](https://blog.betrybe.com).

  <strong>🚵 Habilidades que foram trabalhadas e praticadas:</strong>
  <ul>
    <li>Utilizar o terminal interativo do Python</li>
    <li>Escrever seus próprios módulos e importá-los em outros códigos</li>
    <li>Aplicar técnicas de raspagem de dados</li>
    <li>Extrair dados de conteúdo HTML</li>
    <li>Armazenar os dados obtidos em um banco de dados</li>
  </ul>

</details>

<details>
  <summary><strong>Instalação do projeto</strong></summary><br />

  1. Clone o repositório

  - Use o comando: `git clone git@github.com:tryber/sd-016-a-tech-news.git`
  - Entre na pasta do repositório que você acabou de clonar:
    - `cd sd-016-a-tech-news`

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`
  
  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`
</details>

# Requisitos

## 1 - Função `fetch`
local: `tech_news/scraper.py`

Antes de fazer scrape, precisamos de uma página! Esta função será responsável por fazer a requisição HTTP ao site e obter o conteúdo HTML.
Alguns cuidados deverão ser tomados: como a função poderá ser utilizada várias vezes em sucessão, a implementação respeita o  __Rate Limit__.

- A função recebe uma URL
- A função efetua uma requisição HTTP `get` para esta URL utilizando a função `requests.get`
- A função retorna o conteúdo HTML da resposta.
- A função respeita um Rate Limit de 1 requisição por segundo; Ou seja, caso chamada múltiplas vezes, ela deve aguardar 1 segundo entre cada requisição que fizer.
**Dica:** Uma forma simples de garantir que cada requisição seja feita com um intervalo mínimo de um segundo é utilizar `time.sleep(1)` antes de cada requisição. (Existem outras formas mais eficientes.)
- Caso a requisição seja bem sucedida com `Status Code 200: OK`, deve ser retornado em seu conteúdo de texto;
- Caso a resposta tenha o código de status diferente de `200`, é retornado `None`;
- Caso a requisição não receba resposta em até 3 segundos, ela é abandonada (este caso é conhecido como "Timeout"), com isso retornando None.

📌 É preciso definir o _header_ `user-agent` para que a raspagem do blog da Trybe funcione corretamente. Com isso, foi preenchido com o valor `"Fake user-agent"` conforme exemplo abaixo:

```python
{ "user-agent": "Fake user-agent" }
```

## 2 - Função `scrape_novidades`
local: `tech_news/scraper.py`

Agora no proximo passo precisamos de links para várias páginas de notícias. Estes links estão contidos na página inicial do blog da Trybe (https://blog.betrybe.com). 

Esta função fará o scrape da página Novidades para obter as URLs das páginas de notícias. Com isso, foi utilizado a biblioteca Parsel, para obter os dados que queremos de cada página.

- A função recebe uma string com o conteúdo HTML da página inicial do blog.
- A função faz o scrape do conteúdo recebido para obter uma lista contendo as URLs das notícias listadas.
- A função retorna uma lista.
- Caso não encontre nenhuma URL de notícia, a função retorna uma lista vazia.

## 3 - Função `scrape_next_page_link`
local: `tech_news/scraper.py`

Para buscar mais notícias, é preciso fazer a paginação, e para isto, precisamos do link da próxima página. Esta função é responsável por fazer o scrape deste link.

- A função recebe como parâmetro uma `string` contendo o conteúdo HTML da página de novidades (https://blog.betrybe.com)
- A função faz o scrape deste HTML para obter a URL da próxima página.
- A função retorna a URL obtida.
- Caso não encontre o link da próxima página, a função retorna `None`

## 4 - Função `scrape_noticia`
local: `tech_news/scraper.py`

Agora é a hora de fazer o scrape dos dados que procuramos! 

- A função recebe como parâmetro o conteúdo HTML da página de uma única notícia
- A função com o conteúdo recebido, buscar as informações das notícias para preencher um dicionário com os seguintes atributos:
  - `url` - link para acesso da notícia.
  - `title` - título da notícia.
  - `timestamp` - data da notícia, no formato `dd/mm/AAAA`.
  - `writer` - nome da pessoa autora da notícia.
  - `comments_count` - número de comentários que a notícia recebeu.
    - Se a informação não for encontrada, salve este atributo como `0` (zero)
  - `summary` - o primeiro parágrafo da notícia.
  - `tags` - lista contendo tags da notícia.
  - `category` - categoria da notícia.

- Exemplo de um retorno da função com uma notícia fictícia:

```json
{
  "url": "https://blog.betrybe.com/novidades/noticia-bacana",
  "title": "Notícia bacana",
  "timestamp": "04/04/2021",
  "writer": "Eu",
  "comments_count": 4,
  "summary": "Algo muito bacana aconteceu",
  "tags": ["Tecnologia", "Esportes"],
  "category": "Ferramentas",
}
  ```

## 5 - Função `get_tech_news` para obter as notícias!
local: `tech_news/scraper.py`

Com estas ferramentas prontas, podemos agora fazer um scraper mais robusto com a paginação.

- A função recebe como parâmetro um número inteiro `n` e buscar as últimas `n` notícias do site.
- É utilizado as funções `fetch`, `scrape_novidades`, `scrape_next_page_link` e `scrape_noticia` para buscar as notícias e processar seu conteúdo.
- As notícias buscadas devem ser inseridas no MongoDB; 
- Após inserir as notícias no banco, a função retorna estas mesmas notícias.

Caso queira instalar e rodar o servidor MongoDB nativo na máquina, siga as instruções no tutorial oficial:
Ubuntu: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/  
MacOS:  https://docs.mongodb.com/guides/server/install/
  
Com o banco de dados rodando, o nosso módulo conseguirá acessá-lo sem problemas.

## 6 - Função `search_by_title`
local: `tech_news/analyzer/search_engine.py`

Agora que temos o meios de popular o banco de dados com notícias, Agora para o proximo passo foi feito a funcionalidade de busca.

- A função recebe uma string com um título de notícia
- A função efetua a buscar das notícias do banco de dados por título
- A função retorna uma lista de tuplas com as notícias encontradas nesta busca. 
Exemplo: 
```python
[
  ("Título1_aqui", "url1_aqui"),
  ("Título2_aqui", "url2_aqui"),
  ("Título3_aqui", "url3_aqui"),
]
```
- Caso nenhuma notícia seja encontrada, a função retornar uma lista vazia.

## 7 - Função `search_by_date`
local: `tech_news/analyzer/search_engine.py`

Esta função irá buscar as notícias do banco de dados por data.

- A função recebe como parâmetro uma data no formato ISO `AAAA-mm-dd`
- A função busca as notícias do banco de dados por data.
- A função  retorna no mesmo formato do requisito anterior.
- Caso a data seja inválida, ou esteja em outro formato, uma exceção `ValueError` é lançada com a mensagem `Data inválida`.
- Caso nenhuma notícia seja encontrada, a função retorna uma lista vazia.

## 8 - Função `search_by_tag`,
local: `tech_news/analyzer/search_engine.py`

Esta função irá buscar as notícias por tag.

- A função recebe como parâmetro o nome da tag completo.
- A função busca as notícias do banco de dados por tag.
- A função retorna no mesmo formato do requisito anterior.
- Caso nenhuma notícia seja encontrada, a função retorna uma lista vazia.

## 9 - Função `search_by_category`
local: `tech_news/analyzer/search_engine.py`

Esta função irá buscar as notícias por categoria.

- A função recebe como parâmetro o nome da categoria completo.
- A função busca as notícias do banco de dados por categoria.
- A função retorna no mesmo formato do requisito anterior.
- Caso nenhuma notícia seja encontrada, a função retorna uma lista vazia.