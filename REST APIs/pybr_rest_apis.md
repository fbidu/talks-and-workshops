class: center, middle, vintage, splash
# Arquitetura, Especificação e Implementação de APIs REST
### por [Felipe Videira](https://felipevr.com)
---
class: middle, vintage
# Agenda

* API? REST?? — Motivação
* GET &amp; 404 — Verbos e códigos HTTP
* JSON &amp; YAML — Comunicação
* OAUTH &amp; JWT — Autenticação
* Blueprint &amp; Swagger — Documentação
* Django, Flask &amp; *Pythonicidade* — Implementação
* Py.test, doctest &amp; unittest — Testando seu código
* Heroku, EC2, EBS, Lambda — Colocando seu código no ar
* AB — Teste de carga
---
class: center, middle, vintage
# API? REST??
### Motivação
---
class: vintage
# API
- Um conjunto de estruturas, operações, protocolos e ferramentas para construção de software
- Uma API define um *contrato*, um pacto entre o usuário da API e o programador
- Permite que outros programas façam uso das suas características
---
class: vintage
## Uma Cafeteira
- Faz *só um trabalho* - café
- Exige o *mínimo necessário* - água, pó de café e energia
- Depois de alimentada com o input necessário, faz o trabalho
- Entrega o *resultado esperado*. Nem mais, nem menos
---
class: vintage
## E uma cafeteira *com API?*
- De alguma forma mágica nós automatizamos nossa cafeteira e ensinamos Python para ela
```python
import cafeteira
cafeteira.faça_café()  # Python 3 ❤
```
- Agora nós temos *acesso programático* para nossa cafeteira
- Podemos utilizar sua funcionalidade *em nossos códigos!*
---
class: vintage, middle
```python
# 8h da manhã, hora do café!
if hora_atual == 8:
    cafeteira.faça_café()
```
```python
# Eu não gosto de números ímpares, vou fazer um café pra relaxar
if n % 2:
    cafeteira.faça_café()
```
---
class: vintage
# APIs Web
- Permitem que a gente faça acesso a **recursos remotos**
- Podemos utilizar de funcionalidades **já existentes** em outros serviços disponíveis na Internet
- Tornam a Internet **programável**
---
class: vintage
## Exemplos
- placekitten — Retorna imagens de gatinhos, nas dimensões pedidas [`http://placekitten.com/800/600`](http://placekitten.com/800/600)
- ipify — Retorna o seu endereço de IP na Internet [`https://api.ipify.org/`](https://api.ipify.org/)
- mathjs — Faz cálculos matemáticos [`http://api.mathjs.org/v1/?expr=2*7`](http://api.mathjs.org/v1/?expr=2*7)
---
class: vintage
## Exemplos
- [APIs do Twitter](https://dev.twitter.com/rest/public) — Permitem que você interaja com o serviço de forma bastante ampla - poste novos tweets, busque por tweets, etc
- [Facebook Graph API](https://developers.facebook.com/docs/graph-api) — Analogamente à API do Twitter, permite que você execute ações dentro do Facebok diretamente do seu código - Publique status, faça upload de imagens, determine se duas pessoas são amigos, liste os eventos que a pessoa foi convidada, etc
---
class: vintage, middle, center
# REST
*Representational State Transfer* — Transferência de Estado de Representação
---
class: vintage, middle, center
# Hein?
---
class: vintage
# REST
- É o **padrão desejável** de **arquitetura da Internet**
- Define uma série de regras que os componentes de um **sistema Web ideal** devem seguir
- Ao seguir estas regras, o sistema ganha diversas vantagens como **simplicidade**, **escalabilidade**,
**portabilidade**, **estabilidade**
---
class: vintage
# REST
- Define 5 elementos básicos
1. Recurso
2. Identificador de Recurso
3. Representação
4. Metadados da Representação
5. Dados de Controle
---
class: vintage
# REST
### Recursos e Identificadores de Recurso
- **Qualquer informação nomeável** pode ser considerado um "recurso" -
uma imagem, um documento, uma pessoa, um serviço, uma coleção de outros recursos
- O Identificador de Recurso é uma informação - por exemplo um nome - que é **mapeado para o recurso em si**
- Por mais que o Recurso em si possa **mudar ao longo do tempo**, o Identificador **sempre** aponta para ele
---
class: vintage
# REST
### Recursos e Identificadores de Recurso
- **Identificador** — Presidente dos EUA
- **Recurso** — Barack Obama
- Ano que vem, esse Identificador não apontará mais para *Barack Obama* mas
ainda apontará para seja lá quem for o presidente
---
class: vintage
# REST
### Recursos e Identificadores de Recurso
- **Identificador** — Tony Ramos
- **Recurso** — Tony Ramos
- Este Identificador sempre irá mapear para a mesma pessoa
---
class: vintage
# REST
### Recursos e Identificadores de Recurso
- **Identificador** — Países que são membros da União Europeia
- **Recurso** — [França, Alemanha, Itália, Espanha...]
- Este Identificador aponta para uma lista de Recursos. Quando a Inglaterra
completar sua saída da UE, a lista mudará mas o Identificador continuará
apontando para o lugar certo
---
class: vintage
# REST
### Recursos e Identificadores de Recurso
- **Identificador** — [`http://ecorp.com/financeiro/relatorio_atual`](http://ecorp.com/financeiro/relatorio_atual)
- **Recurso** — O relatório financeiro do ano atual
- Independente do ano em que estamos, obteremos o relatório corrente
---
class: vintage
# REST
### Recursos e Identificadores de Recurso
- **Identificador** — [`http://ecorp.com/financeiro/relatorio_2010`](http://ecorp.com/financeiro/relatorio_2010)
- **Recurso** — O relatório financeiro do ano de 2010
- Sempre obteremos o relatório de 2010
---
class: vintage
# REST
### Recursos e Identificadores de Recurso
- Seja lá quem nomeou o Recurso é responsável por garantir o mapeamento entre o
Identificador e o Recurso em si!
- Falhas neste mapeamento pode levar a inconsistências e a erros, como o famoso
erro **404 Não Encontrado**, onde um Identificador não é mapeado para recurso algum
---
class: vintage
# REST
### Representações de Recursos
- É uma captura do estado atual ou desejado de um Recurso
---
class: vintage
# REST
### Representações de Recursos
- **Identificador** — Logo do Python
-  **Representação**:

![python logo](img/python-logo.png)
---
class: vintage
# REST
### Representações de Recursos
- **Identificador** — Logo do Python em Preto
-  **Representação**:

![python logo black](img/python-logo-black.png)
---
class: vintage
# REST
### Metadados da Representação
- São informações que qualificam a Representação oferecida
- Deve ser apresentado em pares de chaves e valores, como num dicionário
- Podem incluir informações como o formato da representação, o tamanho, etc
---
class: vintage
# REST
### Metadados da Representação
.pull-left[
-  **Representação**:

![python logo](img/python-logo.png)
]
.pull-right[
- **Metadados**:
```python
    'tipo': 'PNG',
    'tamanho': '8.6kB'
```
]
---
class: vintage
# REST
### Dados de Controle
- Modificam o comportamento
- Também podemos oferecer dados que permitem ao cliente determinar a 'validade'
daquela representação
- Dessa forma o cliente pode fazer um *caching* local do recurso e possivelmente
economizar recursos computacionais se for pedir pelo mesmo recurso mais de uma vez
---
class: vintage
# REST
### Dados de Controle
.pull-left[
- **Identificador:** Foto do presidente dos EUA
- **Representação**:

![presidente dos EUA](img/obama.jpg)
]
.pull-right[
- **Metadados**:
```python
    'tipo': 'JPG',
    'tamanho': '13.5kB',
    'validade': '20/01/2017'
```
]
---
class: vintage
# REST
### Metadados de Controle — Cacheamento
- O cliente guarda a representação até a data especificada
- Caso queira acessar esse recurso novamente, verifica se o conteúdo já 'venceu'
- Se o conteúdo ainda é válido, o cliente economiza recursos pois pode utilizar
a representação armazenada ao invés de pedir uma nova
---
class: vintage, middle, center
# GET &amp; 404
### Verbos e códigos HTTP
---
class: vintage
# Protocolo HTTP
### Origem e importância
---
class: vintage
# Protocolo HTTP
### Verbos
---
class: vintage
# Protocolo HTTP
### Códigos
---
class: vintage
# Protocolo HTTP
### Cabeçalhos
---
class: vintage
# Protocolo HTTP
### Negociação de Conteúdo
---
class: vintage, middle, center
# JSON &amp; YAML
### Comunicação
---
class: vintage
# JSON &amp; YAML
### Papo de máquina e papo de gente
---
class: vintage
# JSON &amp; YAML
### Serialização e desserialização
---
class: vintage
# JSON &amp; YAML
### XML?
---
class: vintage, middle, center
# OAUTH &amp; JWT
### Autenticação
---
class: vintage
# OAUTH &amp; JWT
### Autenticação vs Autorização
---
class: vintage
# OAUTH &amp; JWT
### Tokens e segurança
---
class: vintage
# OAUTH &amp; JWT
### OAUTH e OAUTH2
---
class: vintage
# OAUTH &amp; JWT
### JWT
---
class: vintage
# OAUTH &amp; JWT
### Outros métodos
---
class: vintage
# OAUTH &amp; JWT
### Man in the Cloud?
---
class: vintage
# OAUTH &amp; JWT
### HTTPS
---
class: vintage, middle, center
# Blueprint &amp; Swagger
### Documentação
---
class: vintage
# Blueprint &amp; Swagger
### Documente uma vez, atualize primeiro.
---
class: vintage, middle, center
# Blueprint &amp; Swagger
### Mock Servers ou *como tirar o time de front-end do seu pé?*
---
class: vintage, middle, center
# Django, Flask &amp; *Pythonicidade*
### Implementação
---
class: vintage
# Django, Flask &amp; *Pythonicidade*
### Zen do Python e REST
---
class: vintage
# Django, Flask &amp; *Pythonicidade*
### Microframeworks, macroframeworks
---
class: vintage
# Django, Flask &amp; *Pythonicidade*
### Projeto exemplo?
---
class: vintage
# Django, Flask &amp; *Pythonicidade*
### Django REST Framework
---
class: vintage
# Django, Flask &amp; *Pythonicidade*
### Django OAUTH Toolkit
---
class: vintage, middle, center
# Py.test, doctest &amp; unittest
### Testando seu código
---
class: vintage
# Py.test, doctest &amp; unittest
### Testar pra quê?
---
class: vintage
# Py.test, doctest &amp; unittest
### Testes unitários e testes de integração
---
class: vintage
# Py.test, doctest &amp; unittest
### E os bancos de dados?
---
class: vintage, middle, center
# Heroku, EC2, EBS, Lambda
### Colocando seu código no ar
---
class: vintage
# Heroku, EC2, EBS, Lambda
### Cloud, PaaS, SaaS e outros nomes pra impressionar a galera
---
class: vintage, middle, center
# Heroku, EC2, EBS, Lambda
### Heroku
---
class: vintage, middle, center
# Heroku, EC2, EBS, Lambda
### EC2/DigitalOcean
---
class: vintage, middle, center
# Heroku, EC2, EBS, Lambda
### EBS
---
class: vintage, middle, center
# Heroku, EC2, EBS, Lambda
### Lambda
---
class: vintage, middle, center
# AB
### Teste de carga
---
class: vintage
# AB
### Centenas de requests simultâneos!
---
class: vintage, middle, center
# Fontes
---
[Architectural Styles and the Design of Network-based Software Architectures](http://www.ics.uci.edu/~fielding/pubs/dissertation/fielding_dissertation.pdf)
---
