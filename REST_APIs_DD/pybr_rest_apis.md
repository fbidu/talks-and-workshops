class: center, middle, vintage, splash
# Arquitetura, Especificação e Implementação de APIs REST
### por [Felipe Videira Rodrigues](https://felipevr.com)
???
- O nosso tema hoje é falar sobre APIs REST, o que elas são, pra quê elas servem,
quais as tecnologias que estão envolvidas e como construir uma de forma correta.
- Boa parte do conteúdo de hoje serve pra qualquer linguagem de programação.
Só uma pequena parte do conteúdo é específica para Python.
- Nós temos alocado um tempo de 8 horas.
- Nesse tempo, eu preciso cobrir uma parte teórica do assunto mas eu prometo que
não vou só ficar passando slides se não todo mundo aqui vai morrer de sono depois de 30min
- Vou procurar diversificar bastante a apresentação do conteúdo e ele está disponível
integralmente no meu GitHub, fiquem a vontade pra acompanhar como vocês preferirem
seja só acompanhando a apresentação aqui, fazendo anotações, acompanhando no git, etc
---
class: middle, vintage
# Apresentação
- Felipe
- Ciência da Computação - UNICAMP
- PyLadies Campinas
- Desenvolvedor no [LaCTAD/UNICAMP](http://www.lactad.unicamp.br)
- Infraestrutura na [Devnup](http://devnup.com)
???
- Meu nome é Felipe, eu tenho 24 anos e faço ciência da computação na UNICAMP.
- Eu tô na programação faz mais ou menos 10 anos e nesse tempo eu já passei por
diversas lingugagens de programação, ferramentas, técnicas e etc até que nos últimos
anos eu me envolvi com programação em Python e desenvolvimento Web
- Adicionalmente eu trabalho também com infraestrutura, que é relacionado com
colocar os códigos 'no ar' e mantê-los funcionando
---
class: middle, vintage
# Agenda

* API? REST?? — Motivação
* GET &amp; 404 — Verbos e códigos HTTP
* JSON &amp; XML — Comunicação
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
class: vintage
# APIs
### Qual a vantagem de utilizar APIs?
???
- Como nós vimos, ao utilizar APIs nós reaproveitamos recursos que existem na
Internet, que foram feitos por outros programadores.
- Ao reutilizar funcionalidades, economizamos tempo e recursos no nosso lado
- Se já existe uma API que consegue, por exemplo, listar todos os programas de
TV que estão passando em um canal, nós não precisamos gastar tempo buscando e guardando esses dados
- Ou, por exemplo, se tivermos uma API que nos dá o CEP de uma rua. Nós podemos simplesmente
utilizá-la e não perder tempo montando nosso próprio banco de dados
---
class: vintage
# APIs
### Qual a vantagem de CRIAR APIs?
![why apis](img/api-diagram.png)
???
- Okay, utilizar APIs é legal mas, por qual motivo eu iria estrutrar meu projeto como uma API?
- Uma das grandes vantagens é a reutilização dos recursos que você cria em diferentes clientes.
- Suponha que você queira criar um projeto novo, um serviço de encontrar vendedores de cachorro-quente perto da casa do usuário
- Suponha também que você queira que seu serviço seja utilizável por um navegador, no computador e também por um aplicativo Android e outro iOs
- Se você estruturar seu código como uma API, você pode programar toda a lógica mais fundamental e pesada uma única vez
- Então você pode utilizar essa API para alimentar os diferentes clientes que você vai construir
- Além de facilitar o desenvolvimento, você garante de forma fácil que todos os clientes vão acessar os mesmos dados
---
class: vintage, middle, center
# REST
*Representational State Transfer* — Transferência de Estado de Representação
---
class: vintage, middle, center
# Hein?
---
class: vintage
## REST
- É o **padrão desejável** de **arquitetura da Internet**
- Define uma série de regras que os componentes de um **sistema Web ideal** devem seguir
- Ao seguir estas regras, o sistema ganha diversas vantagens como **simplicidade**, **escalabilidade**,
**portabilidade**, **estabilidade**
---
class: vintage
## REST
- Define 5 elementos básicos
1. Recurso
2. Identificador de Recurso
3. Representação
4. Metadados da Representação
5. Dados de Controle
---
class: vintage
## REST
### Recursos e Identificadores de Recurso
- **Qualquer informação nomeável** pode ser considerado um "recurso" -
uma imagem, um documento, uma pessoa, um serviço, uma coleção de outros recursos
- O Identificador de Recurso é uma informação - por exemplo um nome - que é **mapeado para o recurso em si**
- Por mais que o Recurso em si possa **mudar ao longo do tempo**, o Identificador **sempre** aponta para ele
---
class: vintage
## REST
### Recursos e Identificadores de Recurso
- **Identificador** — Presidente dos EUA
- **Recurso** — Barack Obama
- Ano que vem, esse Identificador não apontará mais para *Barack Obama* mas
ainda apontará para seja lá quem for o presidente
---
class: vintage
## REST
### Recursos e Identificadores de Recurso
- **Identificador** — Tony Ramos
- **Recurso** — Tony Ramos
- Este Identificador sempre irá mapear para a mesma pessoa
---
class: vintage
## REST
### Recursos e Identificadores de Recurso
- **Identificador** — Países que são membros da União Europeia
- **Recurso** — [França, Alemanha, Itália, Espanha...]
- Este Identificador aponta para uma lista de Recursos. Quando a Inglaterra
completar sua saída da UE, a lista mudará mas o Identificador continuará
apontando para o lugar certo
---
class: vintage
## REST
### Recursos e Identificadores de Recurso
- **Identificador** — [`http://ecorp.com/financeiro/relatorio_atual`](http://ecorp.com/financeiro/relatorio_atual)
- **Recurso** — O relatório financeiro do ano atual
- Independente do ano em que estamos, obteremos o relatório corrente
---
class: vintage
## REST
### Recursos e Identificadores de Recurso
- **Identificador** — [`http://ecorp.com/financeiro/relatorio_2010`](http://ecorp.com/financeiro/relatorio_2010)
- **Recurso** — O relatório financeiro do ano de 2010
- Sempre obteremos o relatório de 2010
---
class: vintage
## REST
### Recursos e Identificadores de Recurso
- Seja lá quem nomeou o Recurso é responsável por garantir o mapeamento entre o
Identificador e o Recurso em si!
- Falhas neste mapeamento pode levar a inconsistências e a erros, como o famoso
erro **404 Não Encontrado**, onde um Identificador não é mapeado para recurso algum
---
class: vintage
## REST
### Representações de Recursos
- É uma captura do estado atual ou desejado de um Recurso
---
class: vintage
## REST
### Representações de Recursos
- **Identificador** — Logo do Python
-  **Representação**:

![python logo](img/python-logo.png)
---
class: vintage
## REST
### Representações de Recursos
- **Identificador** — Logo do Python em Preto
-  **Representação**:

![python logo black](img/python-logo-black.png)
---
class: vintage
## REST
### Metadados da Representação
- São informações que qualificam a Representação oferecida
- Deve ser apresentado em pares de chaves e valores, como num dicionário
- Podem incluir informações como o formato da representação, o tamanho, etc
---
class: vintage
## REST
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
## REST
### Dados de Controle
- Modificam o comportamento
- Também podemos oferecer dados que permitem ao cliente determinar a 'validade'
daquela representação
- Dessa forma o cliente pode fazer um *caching* local do recurso e possivelmente
economizar recursos computacionais se for pedir pelo mesmo recurso mais de uma vez
---
class: vintage
## REST
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
## REST
### Metadados de Controle — Cacheamento
- O cliente guarda a representação até a data especificada
- Caso queira acessar esse recurso novamente, verifica se o conteúdo já 'venceu'
- Se o conteúdo ainda é válido, o cliente economiza recursos pois pode utilizar
a representação armazenada ao invés de pedir uma nova
---
class: vintage, middle, center
# GET &amp; 404
### O protocolo HTTP
---
class: vintage
## Protocolo HTTP
### [Mapa Mental](https://atlas.mindmup.com/2016/09/f0aedfa062f00134deff01735469202e/protocolo_http/index.html)
---
class: vintage, middle, center
# JSON &amp; XML
### Comunicação
---
class: vintage
## JSON &amp; XML
### Papo de máquina e papo de gente
![communication](img/communication.jpg)
???
* O protocolo HTTP define uma forma de empacotar e transmitir mensagens pela rede
* Cliente e servidor conseguem 'conversar' em HTTP.
* No entanto, nós precisamos definir também uma estrutura para o _conteúdo_ que iremos transmitir
* Usualmente, na internet, trabalhamos com HTML. Ele é bastante útil para estruturar o conteúdo para exibição.
No entanto, uma API tem necessidades diferentes de um navegador.
* Uma API normalmente não vai ser consumida diretamente por um ser humano mas sim por um front-end, que vai ser uma camada 'gráfica' sobre a API.
* Nós não precisamos, portanto, formatar o conteúdo em termos de cores, tipos e tamanhos de fonte, etc. Essas coisas são delegadas para o front-end
* No entanto, temos necessidades adicionais em relação ao HTML. Nós precisamos, por exemplo, definir dados booleanos, numéricos, listas de dados, etc.
* O padrão mais utilizado para isso atualmente é o JSON
---
class: vintage
## JSON &amp; XML
### Exemplo de JSON
```json
{
    "nome": "Felipe",
    "idade": 24,
    "altura": 1.88,
    "programa em Python": true,
    "bandas favoritas": [
        "Pink Floyd",
        "Led Zeppelin"
    ],
    "contatos": {
        "email": "felipe@felipevr.com",
        "github": "https://github.com/fbidu",
        "site": "http://felipevr.com"
    }
}
```
???
* Observe como temos uma estrutura de dicionário, no formato chaves-valores,
muito parecida com o dicionário nativo do Python!
* Observe também como temos valores com tipos de dados diferentes. Strings,
Inteiros, Decimais, Booleanos, Listas e até mesmo um objeto dentro do outro
---
class: vintage
## JSON &amp; XML
### Serialização e Deserialização
.pull-left[
```python
j = Pessoa()
j.nome = 'João'
j.idade = 23
j.altura = 1.70
j.bandas_favoritas = ['U2']
(...)
```
]
.pull-right[
```json
    {
        "nome": "João",
        "idade": 23,
        "altura": 1.70,
        "bandas favoritas": [
            "U2"
        ]
        (...)
    }
```
]
???
* No lado esquerdo temos uma instância do classe pessoa. Ela possui seus atributos definidos e tudo mais.
* No entanto, não é possível simplesmente transmitir ou salvar esses dados para usar depois no jeito em que eles estão.
* É necessário converter aquele objeto, que existe dentro do Python,
em alguma coisa que possa ser salva, seja num arquivo ou num banco de dados, por exemplo
* Esse processo é chamado de serialização.
* A serialização consiste em transformar uma estrutura de dados, um objeto, em alguma coisa que possa ser salva ou transmitida
e que depois a gente possa reconstruir o objeto original com base no que foi armazenado.
* Existem serializações que geram formatos binários, pouco legíveis para humanos mas bastante compactos e bastante legíveis por máquinas
* Nós podemos utilizar o JSON para serializar objetos em um formato de texto, que é legível tanto por humanos quanto por máquinas.
* O texto gerado pode ser transmitido, armazenado, lido e reconstruído para um objeto original
---
class: vintage
## JSON &amp; XML
### Juntando as coisas
* Temos agora três conhecimentos importantes - O padrão REST, o protocolo HTTP e o formato JSON.
* O REST nos diz como estruturar, como pensar nossa API.
* O HTTP, como nossa API pode se comunicar com o resto do mundo
* O JSON, como nós vamos estruturar as mensagens que nossa API irá enviar e receber.
???
* Bom, fazendo uma revisão rápida do que temos até aqui. REST, HTTP e JSON.
* Atualmente esse trio é utilizado na maioria das APIs. No entanto,
observem que nenhum deles *obriga* a utilização de nenhum dos outros dois
---
class: vintage
## JSON &amp; XML
---
class: vintage, middle, center
# OAUTH &amp; JWT
### Autenticação
---
class: vintage
## OAUTH &amp; JWT
### Autenticação vs Autorização
![Home](img/homer-id.jpg)
???
* São dois processos diferentes mas que muitos confundem
* Autenticação diz respeito a confirmar que uma pessoa de fato é quem ela diz que é
* Autorização é determinar que uma pessoa - já devidamente autenticada - pode executar uma determinada ação
* Suponha que você foi numa festa a fantasia com seu amigo, que está fantasiado de Homem de Ferro, com máscara e tudo
* Então seu amigo pede pra você guardar a carteira dele enquanto ele vai ao banheiro
* Depois de um tempo, chega uma pessoa fantasiada de Homem de Ferro e fala "dá minha carteira"
* Você fica na dúvida: é mesmo seu amigo?
* Só o seu amigo tem *autorização* para acessar aquela carteira
* No entanto, você precisa primeiro *autenticar* que aquela pessoa fantasiada é o seu amigo
* Quando a pessoa fantasiada arrancar a máscara, você vai de fato autenticar se aquela pessoa é seu amigo ou não
* Se ela for, você entrega a carteira. Caso contrário, você segura
* No mundo "físico" autenticações são feitas usando documentos como o RG
* No meio digital, o meio mais comum de autenticação são usuários e senhas
---
class: vintage
## OAUTH &amp; JWT
### Basic Auth
```
http://usuário:senha@servidor.com
```
![basic auth](img/basic-auth.svg)
???
* É a forma mais básica de autenticação na Internet
* Em cada chamada você passa o usuário e a senha para autenticação
* É extremamente simples e fácil de ser implementado
* Para aplicações bem simples ainda é utilizado. No entanto, alguns cuidados devem ser tomados
* O protocolo HTTP não criptografa nada por padrão, então qualquer ponto no
'meio do caminho' entre o cliente e o servidor poderá interceptar o nome de usuário e a senha
---
class: vintage
## OAUTH &amp; JWT
### Autenticações por Token
![token auth](img/token-auth.svg)
???
* Diversas implementações diferentes
* Basicamente o usuário não mais fornece suas credenciais da API para o cliente
* O usuário pede a um servidor de autenticação para gerar um token, que é basicamente um texto, uma string.
* Nesse pedido, o usuário conta pro servidor de autenticação, em nome de *qual cliente*
ele está gerando aquele token e quais ações o usuário quer permitir que o cliente execute em seu nome
* O usuário vai se autenticar nesse servidor com as suas credenciais, este servidor irá validá-las
e então irá gerar esse token, guardando ele atrelado à conta do usuário
* O servidor de autenticação envia esse token para o cliente
* A partir desse momento, o cliente vai utilizar esse token para autenticar suas chamadas à API feitas
em nome do usuário
* A API, ao receber uma chamada do cliente, pega o token e consulta de qual usuário é aquele token
para fazer a autenticação e quais permissões o usuário deu para o portador daquele token
---
class: vintage, middle, center
## OAUTH &amp; JWT
### Tokens vs Basic Auth
???
* Algumas diferenças importantes. A primeira é que o usuário não mais envia as credenciais da sua conta
ao cliente, mas sim a um servidor de autenticação
* Outro ponto importante, no basic auth se um usuário utilizasse 3 clientes diferentes para uma API, por exemplo
um cliente Android, um no navegador e outro numa Smart TV
* Nesse cenário, como as mesmas credenciais são usadas para todos os clientes, o usuário não consegue remover
o acesso de apenas um desses clientes. O máximo que ele pode fazer é mudar a própria senha, revogando o acesso
de todos eles
* Com uma autenticação baseada em tokens, o usuário pode revogar o acesso de apenas um aplicativo cliente
* Mais uma questão importante - o usuário pode dar à clientes diferentes,
autorizações diferentes sobre sua conta.
* Outro ponto interessante é que com tokens, o usuário e a API podem saber qual *cliente*
executou uma determinada ação em nome do usuário pois cada token é gerado para
um cliente específico
* Atualmente, a maioria das APIs utiliza alguma estrutura de autenticação baseada em tokens
---
class: vintage
## OAUTH &amp; JWT
### OAUTH e OAUTH2
---
class: vintage
## OAUTH &amp; JWT
### JWT
---
class: vintage
## OAUTH &amp; JWT
### Outros métodos
---
class: vintage
## OAUTH &amp; JWT
### *Man in the Middle* e *Man in the Cloud*
![token auth](img/token-auth.svg)
---
class: vintage
## OAUTH &amp; JWT
### HTTPS
---
class: vintage, middle, center
# Blueprint &amp; Swagger
### Documentação
---
class: vintage
## Blueprint &amp; Swagger
### Documente uma vez, atualize primeiro.
---
class: vintage
## Blueprint &amp; Swagger
### Mock Servers ou *como tirar o time de front-end do seu pé?*
---
class: vintage, middle, center
# Django, Flask &amp; *Pythonicidade*
### Implementação
---
class: vintage
## Django, Flask &amp; *Pythonicidade*
### Zen do Python e REST
---
class: vintage
## Django, Flask &amp; *Pythonicidade*
### Microframeworks, macroframeworks
---
class: vintage
## Django, Flask &amp; *Pythonicidade*
### Projeto exemplo?
---
class: vintage
## Django, Flask &amp; *Pythonicidade*
### Django REST Framework
---
class: vintage
## Django, Flask &amp; *Pythonicidade*
### Django OAUTH Toolkit
---
class: vintage, middle, center
# Py.test, doctest &amp; unittest
### Testando seu código
---
class: vintage
## Py.test, doctest &amp; unittest
### Testar pra quê?
---
class: vintage
## Py.test, doctest &amp; unittest
### Testes unitários e testes de integração
---
class: vintage
## Py.test, doctest &amp; unittest
### E os bancos de dados?
---
class: vintage, middle, center
# Heroku, EC2, EBS, Lambda
### Colocando seu código no ar
---
class: vintage
## Heroku, EC2, EBS, Lambda
### Cloud, PaaS, SaaS e outros nomes pra impressionar a galera
---
class: vintage
## Heroku, EC2, EBS, Lambda
### Heroku
---
class: vintage
## Heroku, EC2, EBS, Lambda
### EC2/DigitalOcean
---
class: vintage
## Heroku, EC2, EBS, Lambda
### EBS
---
class: vintage
## Heroku, EC2, EBS, Lambda
### Lambda
---
class: vintage, middle, center
# AB
### Teste de carga
---
class: vintage
## AB
### Centenas de requests simultâneos!
---
class: vintage, middle, center
# Fontes
---
class: vintage
- [**Architectural Styles and the Design of Network-based Software Architectures**](http://www.ics.uci.edu/~fielding/pubs/dissertation/fielding_dissertation.pdf)
- [**FAQ sobre HTTP/2**](https://http2.github.io/faq/)
- [**The HTTP OPTIONS method and potential for self-describing RESTful APIs**](http://zacstewart.com/2012/04/14/http-options-method.html)
- [**REST CookBook**](http://restcookbook.com/)
- [**Build APIs You Won't Hate**](https://apisyouwonthate.com/)
- [**Introduction to REST and .net Web API**](https://blogs.msdn.microsoft.com/martinkearn/2015/01/05/introduction-to-rest-and-net-web-api/)
- [**JSON**](http://www.json.org/json-pt.html)
- [**JSON API**](http://jsonapi.org/)
---
class: vintage, middle, center
# Obrigado 😄
