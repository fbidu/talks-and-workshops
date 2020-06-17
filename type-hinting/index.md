# Python, Tipos & Pessoas

Note:
* Bom dia a todos, bem vindos! É muito bom estar aqui mais uma vez junto da comunidade
python. A última conferência que eu estive foi na Python Sudeste e eu não consegui
ir ao Caipyra desse ano. Antes de começar eu queria saber quem aqui tá na primeira python brasil? Muito bom, sejam bem vindos! Uma das coisas mais legais e mais importantes
de Python é isso, a nossa comunidade. Eu espero que vocês tenham uma ótima experiência
na Pybr e voltem sempre! Agora, quem aqui já usou de Type hinting em Python?

* Hoje nós vamos discutir um pouco sobre tipos de dados, análise estática de código
e as funcionalidades que temos para lidar com esses conceitos em Python

* O título original dessa palestra era Python, Tipos e Segurança. Eu decidi mudar
esse título por razões que vão ficar mais claras ao final



Aperte a tecla `"s"` para ver as notas de apresentação!



### Oi, eu sou o (Felipe) Bidu!

* [github.com/fbidu](https://github.com/fbidu)
* Instituto de Computação - UNICAMP
* Desenvolvedor Back End
* Arquiteto de Infra no [Poppin](https://poppin.app)



# O que é um tipo?
Note:
Para iniciar nossa discussão, vamos primeiro definir o que  _é_ um tipo



# 01100001
- Qual o significado dessa cadeia binária? <!-- .element: class="fragment" data-fragment-index="2" -->
- Em decimal, é o número 97  <!-- .element: class="fragment" data-fragment-index="3" -->
- Na tabela ASCII, é o caractere "a"  <!-- .element: class="fragment" data-fragment-index="4" -->

Note:
* Por baixo dos panos, computadores processam bits, zeros e uns.
* Eventualmente, todo pedaço de informação é convertido para bits
* Imagine que seu computador encontre esses bits enquanto processa dados
* Como que essa sequência pode ser interpretada?
* _abrir resto do slide_
* O fato de que uma informação pode ser vista de duas formas diferentes gera
uma possível ambiguidade
* Computadores não lidam muito bem com ambiguidades!



# Operações

* De acordo com _como_ entendemos uma informação, as operações possíveis
mudam!

Note:
* Se estamos lidando com strings ou inteiros, as coisas que nós podemos
fazer com a informação é diferente



```python
>>> 97 * 10
970

>>> 97 - 55
42

```
`01100001 == 97`?
Note:
* Se esses bits representarem um inteiro, nós podemos fazer operações algébricas
com ele
* Podemos usar essa informação como índice de uma lista, como elemento de comparação
maior-menor com outros números, etc


```python
>>> "a" * 10
'aaaaaaaaaa'

>>> "a".upper()
'A'

>>> "a".isalpha()
True

>>> "a".isdigit()
False
```
`01100001 == "a"`?

Note:
* Por outro lado se essa cadeia de bits for um caractere, as operações possíveis
são bem diferentes
* Nós agora podemos usar todas as operações de string, podemos realizar comparações
com outras strings
* Mas nós não podemos mais usar essa informação como um índice de uma lista, por
exemplo



Tipos permitem definir quais operações podemos ou não aplicar sobre um conjunto de informações!


```python
>>> 80218 + "Python"

TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Note:
* Um Type Error ocorre quando violamos as operações que podem ser aplicadas sobre um tipo
* O que faz com que uma operação cause um type error depende da linguagem


Python:
```python
>>> "Python Brasil " * 2
'Python Brasil Python Brasil '
```
Java:
```java
String a = "Python Brasil ";

a * 2;

----------
|  Error:
|  bad operand types for binary operator '*'
|    first type:  java.lang.String
|    second type: int
|  a * 2
|  ^---^
```
Note:
* Python, por exemplo, permite que a gente multiplique uma string por um número
a operação é considerada válida e não causa problemas
* Em Java isso já não é possível. Aplicar o operador * entre strings e inteiros
causam um type error


> "[...] A type is a set of values and a set of functions that one can apply to these values."

― Guido van Rossum, Ivan Levkivskyi - [PEP 483 - The Theory of Type Hints](https://www.python.org/dev/peps/pep-0483/#background)

Note:
* Existem alguns PEPs que são importantes para a discussão de hoje.
* O [PEP 484](https://www.python.org/dev/peps/pep-0484/) define os Type Hints
que iremos tratar em breve e o PEP 483 lida com a teoria por trás disso tudo
* No PEP 483 os autores usam essa definição "um tipo é um conjunto de valores
e um conjunto de funções que alguém pode aplicar nesses valores"
* Nesse mesmo PEP, os autores explicam que existem _diversas_ definições de tipos
na literatura de teoria da computação. De fato, é uma área grande e com bastante
trabalho feito.
* No entanto, na palestra de hoje, eu vou lidar com a parte mais instrumental e
mais prática de tipos e tipagem no Python



# Sistemas de Tipos
* Diversos nomes diferentes
* Estático vs. Dinâmico <!-- .element: class="fragment" data-fragment-index="3" -->
* Forte vs. Fraco <!-- .element: class="fragment" data-fragment-index="4" -->
* Explícito vs. Implícito <!-- .element: class="fragment" data-fragment-index="5" -->
* (autor A) vs. (autor B) <!-- .element: class="fragment" data-fragment-index="6" -->

Note:
* Em termos de sistemas de tipos e como as linguagens de programação se comportam
existe uma coleção considerável de nomenclaturas
* _exibir todo slide_


# Estático vs. Dinâmico
O tipo de uma variável pode mudar?<!-- .element: class="small -->

Note:
* Estático: Variáveis mantém o mesmo tipo durante toda a vida.
* Estático: A checagem de tipos é feita normalmente antes da execução
* Em linhas gerais, uma linguagem com tipagem estática não permite que o tipo
de uma variável mude


# Forte vs. Fraco
Quão "chata" a linguagem é com tipos? <!-- .element: class="small -->

Note:
* Forte: diversas definições! Muitas delas são informais
* Quanto mais uma linguagem garante que operações só possam ser aplicadas para certos tipos,mais "forte" ela é
* Ponteiros como em C, que apontam para regiões arbitrárias da memória "enfraquecem" o sistema de tipos


# Explícito vs. Implícito
Você consegue saber o tipo de uma variável só lendo o código? <!-- .element: class="small -->

Note:
* Numa linguagem com tipagem explícita, existem palavras reservadas obrigatórias
que declaram o tipo. C, Java e Pascal são assim
* Já na tipagem implícita, o tipo de uma variável é inferido do contexto



Python tem um sistema de tipos **implícito**:
```python
>>> ano = 2019
```


Python tem um sistema de tipos implícito, **dinâmico**:
```python
>>> ano = 2019
>>> ano = str(ano)
```


Python tem um sistema de tipos implícito, dinâmico e **forte**:
```python
>>> ano = 2019
>>> ano = str(ano)
>>> ano / 10

TypeError: unsupported operand type(s) for /: 'str' and 'int'
```



# Análise Estática & Tipagem Dinâmica

Juntando dois pedaços da conversa de hoje <!-- .element: class="small -->

Note:
* Definido o sistema de tipos do Python em linhas gerais, podemos agora começar
a considerar outra coisa importante na conversa de hoje, análise estática

* Olhando para os termos "estática" e "dinâmica" em cada lado desse título,
dá pra sentir que teremos alguns problemas


## Podemos checar código de duas formas

1. Lendo o código <!-- .element: class="fragment" data-fragment-index="2" -->
2. Rodando o código<!-- .element: class="fragment" data-fragment-index="3" -->

Note:
* Em linhas gerais, nós podemos testar e validar coisas no nosso código de duas formas,
lendo o código e acompanhando o que acontece e executando o código


| Método de Análise | Tipo     |
|-------------------|----------|
| Leitura           | Estática |
| Execução          | Dinâmica |

Note:
* Quando uma ferramenta - ou você! - tira conclusões do código sem executá-lo,
temos uma análise estática

* Por outro lado, quando o código é de fato executado, a análise é dinâmica

* As duas formas de análise tem seus méritos e seus usos. Hoje vou focar nas
vantagens da análise estática


## Análise Estática

1. Livre de efeitos do código <!-- .element: class="fragment" data-fragment-index="2" -->
2. Mais rápida de definir e executar <!-- .element: class="fragment" data-fragment-index="3" -->
3. A cobertura é sempre 100% <!-- .element: class="fragment" data-fragment-index="4" -->

Note:
* A primeira vantagem da análise estática é que ela e livre de qualquer efeito
que o código tem. Como o código não será executado, você não precisa se preocupar
com o código apagar um arquivo, escrever num banco de dados, lançar um míssil, etc

* Uma análise estática costuma ser rápida para ser definida - basta você escolher
sua ferramenta favorita de análise e configurar algumas coisinhas. Ela também
é mais rápida de ser executada que a dinâmica. Uma análise dinâmica em geral depende
de testes escritos por humanos que flexionam as partes do sistema para serem testadas

* No momento que um código existe, ele pode ser testado pelo seu analisador estático!
Sem você ter que se preocupar com tocar no código através de testes ou coisa assim



## ⚠️⚠️ ALERTA ⚠️⚠️

Análise️ Dinâmica é MUITO importante, ela só não é o foco de hoje!

Note:
* Só um breve comentário - eu estou focando em análise estática por uma escolha
didática e por conta do tempo que a gente tem. Análise dinâmica é também muito
importante!



Análise Estática é muito boa, muito legal, mas...

Note:
* Voltando para análise estática, ela realmente é uma coisa muito boa,
mas...



...ela depende do quanto a linguagem sozinha consegue contar pra ela
Note:
* Ela é fundalmentamente limitada pelo que a linguagem consegue contar para
o analisador sem de fato rodar o código



Tome esse pedaço de código em Java, por exemplo
```java
int some_function(int a, int b) {
    return a.toUpperCase();
}
```
Note:
* A gente nem precisa conhecer java pra estranhar o método "to upper case" sendo
aplicado num inteiro. Esse é um nome de um método típico de strings e ali na
declaração da função, eu to contando que "a" é um inteiro


Porém em Python...
```python
def some_function(a, b):
    return a.upper()
```
Note:
* Nesse caso, nem eu, nem você e nem ninguém tem a menor condição de saber se
aquele pedaço de código faz sentido por conta da natureza dinâmica dos tipos
em Python

* A ausência de documentação também não ajuda



**_ALERTA DE FLAME WAR_**

# Tipagem Dinâmica é um problema?

Questão de design intrínseco à linguagem!<!-- .element: class="small -->

Note:
* Esse tipo de pergunta é uma das famosas flame wars - brigas que acontecem
normalmente na internet entre pessoas que tem opiniões muito muito fortes sobre
assuntos muito muito específicos e normalmente 100% subjetivos

* A tipagem dinâmica oferece uma série de benefícios, como deixar o código
mais claro, mais legível e sem ficar parecendo um monte de instruções burocráticas

* A flexibilidade da tipagem dinâmica nos permite criar ferramentas complexas
de metaprogramação, graças ao maior nível de introspecção que a linguagem ganha

* Honestamente, cada sistema de tipos tem suas vantagens assim como cada linguagem
de programação tem seus casos de uso ótimos e péssimos. Não existe uma linguagem
ótima. Perguntar qual linguagem é melhor é uma pergunta fundamentalmente incompleta.
Nós precisamos considerar diversos aspectos do contexto antes de respondê-la.
Se o seu prazo é curto e a urgência é grande, a melhor linguagem de programação
é aquela que você sabe.



## Juntando os dois mundos

Como casar o dinamismo de um lado com a riqueza de informações do outro?<!-- .element: class="small -->

Note:
* Apesar das vantagens da tipagem dinâmica, a tipagem estática também possui
vantagens importantes.

* Num sistema de tipos estáticos, é possível detectar de forma mais rápida erros
e bugs que podem ter impacto significativo na estabilidade e segurança do sistema

* Será que tem como juntar um pouco esses dois mundos?


# Gradual Typing!

Dinâmico quando desejado, estático quando necessário <!-- .element: class="small fragment" data-fragment-index="2" -->

[Jeremy Siek, 2006](http://wphomes.soic.indiana.edu/jsiek/what-is-gradual-typing/)<!-- .element: class="small fragment" data-fragment-index="3" -->

Ótima referência para aprofundar na teoria de Gradual Typing <!-- .element: class="small fragment" data-fragment-index="4" -->

Note:

* Mais ou menos em 2006, Jeremy Siek definiu o conceito de gradual typing, que
permite combinar no código elementos dos dois mundos

* Apesar de ter sido definido formalmente em 2006, gradual typing é uma coisa
que já acontecia de formas diferentes antes disso


## No mundo Python...

* Debates sobre isso acontecem desde o ano 2000 <!-- .element: class="small fragment" data-fragment-index="2" -->
* Referência legal:<!-- .element: class="small fragment" data-fragment-index="4" --> [GvR - Type Hints - PyCon 2015](https://www.youtube.com/watch?v=2wDvzy6Hgxg) <!-- .element: class="small fragment" data-fragment-index="4" -->

Note:
* Dentro da comunidade Python, debates sobre essa questão remetem ao ano 2000 com
uma primeira implementação de alguma coisa próxima de gradual typing vindo
no PEP 3107, de 2006
* Eu não vou entrar em detalhes sobre o PEP 3107 porque ele não cumpre de fato
com a noção atual de type hinting. Ele na verdade permite que a gente anote funções
e seus argumentos com informações arbitrárias, que podem ser usadas como hints



# Type Hints
_Dicas_ sobre o tipo<!-- .element: class="small" -->

Note:
* E vamos finalmente chegar no filé dessa minha palestra, a noção de Type Hint
em si
* Type Hint é como implementamos a noção de gradual typing em Python
* Ou seja, é o que permite que a gente marque o tipo quando for conveniente


Qual assinatura de uma função `user_age` que recebe um ID do usuário e retorna sua idade?

`user_id = int, user_age = int` <!-- .element: class="small fragment" data-fragment-index="2" -->

`user_id = string, user_age = int` <!-- .element: class="small fragment" data-fragment-index="3" -->

`user_id = ObjectID, user_age = string` <!-- .element: class="small fragment" data-fragment-index="4" -->

Note:
* Considere o problema de montar uma função que recebe o ID de um usuário e
retorna sua idade. Nós podemos pensar em diversas assinaturas para essa função

* ID sendo inteiro, retornando inteiro, ID sendo string retornando inteiro,
se vc lida com bancos de dados Mongodb talvez seu ID seja um ObjectID e sei lá
porque você faria isso mas vc pode resolver retornar a idade como uma string


Podemos resolver isso com docstrings, documentação, etc. Porém Type Hints
oferecem uma forma estruturada e poderosa de lidar com isso!

```python
def user_age(user_id: str) -> int: (...)

def some_function(a: int, b: int): -> str (...)
```


### TÃO ACABANDO COM O MEU PYTHOOOON
![pinguim_desesperado](ping.jpeg)

Como assim tipo estático?? E os meus códigos???? Vou ter que mudar tudo
de novo? A migração Python 2 - 3 nem acabou ainda!! aaaAAAaaaaa


## Caaalma!

* Anotação de tipos em Python é totalmente opcional! <!-- .element: class="fragment" data-fragment-index="2" -->
* Código anotado e não anotado pode viver tranquilamente no mesmo projeto <!-- .element: class="fragment" data-fragment-index="3" -->
* É possível colocar anotações num arquivo separado (spoiler) <!-- .element: class="fragment" data-fragment-index="4" -->
* Não vai quebrar o código de ninguém <!-- .element: class="fragment" data-fragment-index="5" -->
* E Python não vai deixar de ter tipagem dinâmica! <!-- .element: class="fragment" data-fragment-index="6" -->


> It should also be emphasized that Python will remain a dynamically typed language,
and the authors have no desire to ever make type hints mandatory, even by convention.

― [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)



# Como Anotar Tipos

Note:
* Nos slides anteriors vimos um dos exemplos mais simples de anotação de tipos,
após o argumento da função, colocamos dois pontos e o tipo
* Porém existem mais formas de fazer essa anotação de tipos


### 3 Formas diferentes:
1. Function Annotations, como já vimos <!-- .element: class="fragment" data-fragment-index="2" -->
2. Stub Files. Anotações que ficam num arquivo separado <!-- .element: class="fragment" data-fragment-index="3" -->
3. Type Comments. Anotações que ficam em comentários com um formato específico <!-- .element: class="fragment" data-fragment-index="4" -->



# Function Annotations
Quando a tipagem vive junto dos argumentos, dentro da declaração<!-- .element: class="small -->


* Forma mais simples e direta de anotar tipos
* Compatível com o PEP-3107
* Não é compatível com outras versões do Python antes da 3.5
* Se você não tiver necessidade de suportar versões antes da 3.5, comece por aqui!

Note:
* Bem, function annotations são a estrutura que eu mostrei para vocês nos
slides anteriores
* Ela se beneficia de uma estrutura montada anteriormente, no PEP 3107. Esse PEP
permite que a gente defina anotações genéricas nos argumentos de uma função, mas
não define nenhum significado pra essas anotações.
* Com o PEP 484 e os type hints, essas anotações ganham um significado
* Nossos colegas que lidam com teoria de linguagem de programação diriam que o
PEP 3107 definiu uma sintaxe, uma estrutura e o PEP 484 definiu uma semântica ou
seja, anexou um significado à estrutura


## O Módulo `typing`

* Define diversas entidades que nos permitem fazer anotações ricas de tipos <!-- .element: class="fragment" data-fragment-index="2" -->
* Quer definir que uma função retorna uma lista contendo apenas números? <!-- .element: class="fragment" data-fragment-index="3" -->
* Quer especificar que o argumento de uma função deve ser uma outra função
que retorna um tipo em especial? <!-- .element: class="fragment" data-fragment-index="4" -->
* Quer garantir que o tipo de retorno de uma função é o mesmo tipo de retorno
da entrada, mesmo sem definir qual tipo é esse? <!-- .element: class="fragment" data-fragment-index="5" -->


# O módulo `typing` é a solução!


* A API do módulo `typing` é rica!
* Recomendo bastante dar uma lida no PEP-484, especialmente [na seção sobre ele](https://www.python.org/dev/peps/pep-0484/#the-typing-module)
* Nos próximos slides vou mostrar alguns exemplos de uso


```python
from typing import TypeVar, Iterable, Tuple

Number = TypeVar('Number', int, float)
Point = Tuple[Number, Number]
Space = Iterable[Point]

def center_of_mass(points: Space) -> Point:
    (...)

def distance(point_a: Point, point_b: Point) -> Number:
    (...)

def mean_distance(*points: Point) -> Number:
    (...)
```
Note:
* Bom, vamos relembrar um pouco dos nossos momentos felizes nas aulas de Física.
Um ponto no espaço é um conjunto ordenado de números, no plano de duas dimensões,
são dois números. Um espaço no caso eu to definindo como sendo uma iterável
qualquer, como uma lista, de pontos

* Na linha number = ... eu defino um tipo novo, o tipo Number e eu digo que
um number pode ser um inteiro ou um float. Logo em seguida eu defino um Point
como sendo uma tupla com dois Numbers. Finalmente eu defino um espaço como sendo
um iterável contendo apenas pontos

* O centro de massa de um conjunto de pontos é mais ou menos o ponto onde o
conjunto se equilibra. Em resumo se vc colocar seu dedo na direção do centro de
massa do seu notebook, você consegue equilibrar ele na ponta do dedo. Eu não
vou fazer isso ao vivo porque na chance de eu errar, o custo é meio alto.

* Mas enfim, a função centro de massa ela deve receber um espaço contendo vários
pontos e então ela vai retornar um outro ponto, que é a localização desse centro.
Vocês podem ver na definição da função center_of_mass como as anotações foram
usadas para expressar esse significado

* A distância entre dois pontos é simplesmente um número. A função "distance"
usa das anotações para mostrar que ela aceita dois argumentos, do tipo Point
e retornará um número

* E finalmente o último exemplo desse slide mostra como podemos combinar anotações
com a sintaxe de argumentos arbitrários. Essa última função nos indica que ela
aceita uma quantidade arbitrária de pontos e retornará um número, que representa
a distância média entre esses pontos


### Tarefa Para Casa

(Para os que tão achando tudo isso daqui legal) <!-- .element: class="small -->

Você poderia passar um argumento do tipo `Space` na última função?

Teste com as ferramentas que veremos em breve e veja a definição de "is consistent"
no PEP 483 ou no artigo sobre Gradual Typing


```python
from typing import TypeVar
from bson import ObjectId

UserID = TypeVar("UserID", str, ObjectId)

def user_age(user_id: UserID) -> int:
    (...)
```
Note:
* Aqui nós temos revisitamos o exemplo da idade do usuário. Considere que a sua
função user_age pode aceitar o argumento user_id como sendo uma String ou um
ObjectId conforme definido na biblioteca BSON.

* Você pode então definir um tipo arbitrário chamado UserID e definir sua função
dessa forma


```python
from typing import Callable

BinaryOp = Callable[[int, int], int]
GenericOp = Callable[..., int]

def is_commutative(operation: BinaryOp) -> bool:
    (...)

def register_callback(callback: GenericOp):
    (...)
```
Note:
* Nesse slide nós vemos como definir assinaturas de função que serão usadas como
argumentos de outras funções. Ou seja, vamos passar uma função como parâmetro

* Pra isso nós usamos o tipo Callable. Na linha Binary.. eu defino uma operação
binária. Uma operação binária é uma função que aceita dois inteiros e retorna
outro inteiro. Operações como soma, subtração, multiplicação, são exemplos

* A sintaxe de um Callable é essa que está apresentada, o primeiro argumento
é uma lista contendo o tipo de todos os argumentos usados, seguido de um último
argumento que é o tipo de retorno.

* Na linha genericOp = ... eu defino uma operação genérica que aceita um número
indefinido de argumentos de tipo também indefinido mas que retorna sempre um
inteiro. Para definir esses argumentos genéricos nós usamos o operador "ellipsis"
que são 3 pontos. Note que nesse caso os argumentos da função não são separados
por colchetes.



# Stub Files
Para quando você não pode ou não quer adicionar anotações no seu código!
Note:
* Tudo isso de type hint através de anotações é muito bom, muito legal mas em
alguns casos a gente simplesmente não pode aceitar só versões mais novas de
Python. As vezes precisamos manter compatibilidade com versões anteriores a
3.5 e etc. Como usar de tipos então?


Stub Files são anotações de tipo que ficam num arquivo `.pyi`


* Útil para quando o código em si é rodado também por interpretadores incompatíveis <!-- .element: class="fragment" data-fragment-index="2" -->
* Quando você quer dar anotações de tipos para algum código que não é seu <!-- .element: class="fragment" data-fragment-index="3" -->
* Quando a equipe não quer "sujar" o código com anotações <!-- .element: class="fragment" data-fragment-index="4" -->
* Quando você quer liberar anotações de tipo gradativamente <!-- .element: class="fragment" data-fragment-index="5" -->


Stub:
```python
from typing import TypeVar
from bson import ObjectId

UserID = TypeVar("UserID", str, ObjectId)

def user_age(user_id: UserID) -> int: ...
```
Implementação:
```python

def user_age(user_id):
    pass
```
Note:
* Quem aqui já trabalhou com C/C++ talvez reconheça alguma semelhança entre essa
estrutura e os headers dessas linguagens. Basicamente nós vamos criar um arquivo
com extensão .pyi que irá conter todas as anotações de tipos
* Num arquivo paralelo manteremos a implementação em si, em Python puro


Desenvolvedores podem publicar anotações de tipos para outras libs

Veja o [PEP 561](https://www.python.org/dev/peps/pep-0561) para mais informações sobre como distribuir esses arquivos

Note:
* Stub files permitem que desenvolvedores distribuam anotações de tipos para
bibliotecas escritas por terceiros, que podem ou não ainda ser mantidas.

* Esse é um padrão que permite ainda mais gradatividade na adoção de type hints,
diminuindo a pressão para liberação e modificação de código



# Variable Annotations
Type Hinting para variáveis também!


* O PEP 484 definia uma sintaxe baseada em comentários para anotar tipos de
variáveis

```python
euclidean = [] # type: List[Points]
```


* Essa sintaxe era dada como uma forma de facilitar o processamento do tipo de
variáveis em casos complexos.

* No fim do PEP 484, os autores deixam o seguinte comentário


> If type hinting proves useful in general, a syntax for typing variables may be provided in a future Python version.


* De fato, um novo PEP foi escrito para lidar com variáveis

* No Python 3.6 ele foi implementado – [PEP 526](https://www.python.org/dev/peps/pep-0526/)


"Ah, que fantástico"

"Tudo o que eu queria, MAIS uma sintaxe nova"


* Felizmente, a sintaxe usada é herdada daquela que nós já vimos!

```python
users: List[User]
age: int = 19
is_valid: bool
name: str = "Felipe"
```



Então Python agora me permite explicitar tipos?


# Sim!


E agora o Python me retorna um erro assim que alguma invocação errada acontece?


# Não

Note:
* Mostrar o conteúdo e a execução de sample1_correct.py


...

então??


Python agora oferece uma forma centralizada de explicitar informações de
tipos onde a desenvolvedora do código desejar.


### Pra quê serve então?

* Essa informação pode ser capturada de forma automática <!-- .element: class="fragment" data-fragment-index="2" -->
* Podemos construir ferramentas de checagem mais complexas (e completas!)<!-- .element: class="small fragment" data-fragment-index="3" -->
* Editores de texto e IDEs podem oferecer sugestões melhores <!-- .element: class="small fragment" data-fragment-index="4" -->

Note:
* Nós podemos ficar na dúvida do que podemos fazer com isso então

* A grande questão é que com um padrão bem estruturado para oferecer essa
informação, nós podemos escrever analisadores estáticos que são capazes de
pegar erros que podem ter passado despercebidos pela equipe de dev.

* Isso tudo nos permite pegar toda uma família de bugs com mais agilidade e
antes que esses bugs sejam colocados no ar



# Analisadores


* Existem várias ferramentas que podem checar suas anotações de tipos!
* A mais famosa – e que deu origem a tudo isso, de certa forma – é o [mypy](http://www.mypy-lang.org/)
* Outra que tem ganho relevância especialmente em projetos grandes é o [Pyre](https://pyre-check.org/)


* Pyre foi criado pelo Facebook para ser usado na base de código do Instagram, uma
base Python com milhões de linhas de código feitas por diversos programadores
* Recomendo a talk [Shannon Zhu - Leveraging the Type System to Write Secure Applications - PyCon 2019](https://www.youtube.com/watch?v=ZplZ8ZBwu0Q) sobre o assunto



# Ferramentas sozinhas não fazem nada!
Precisamos de **métodos** <!-- .element: class="small -->

Note:
* E finalmente minha última dica é sobre esse monte de ferramentas que a gente tem


* Engenharia de Software é tão legal que ela consegue se introspectar<!-- .element: class="fragment" data-fragment-index="2" -->
* Tem um problema com desenvolvimento de software? <!-- .element: class="fragment" data-fragment-index="3"-->
* Construa outro software pra resolver!<!-- .element: class="fragment" data-fragment-index="4" -->
* git, Jira, pylint, ... <!-- .element: class="fragment" data-fragment-index="5" -->


![so-many-tips](so-many.jpg)

Note:
* É normal a gente sair de conferências se sentido sobrecarregados de dicas
e ferramentas e técnicas novas


* Ter uma ampla carta de opções é fantástico <!-- .element: class="fragment" data-fragment-index="2" -->
* Nos permite fazer muita coisa legal <!-- .element: class="fragment" data-fragment-index="3" -->
* Mas, especialmente numa equipe, consistência é fundamental! <!-- .element: class="fragment" data-fragment-index="4" -->


* Liste as opções, discuta com a sua equipe e defina um padrão<!-- .element: class="fragment" data-fragment-index="2" -->
* Não se preocupe em definir tudo, não se preocupe em acertar de primeira. Defina
algumas linhas gerais<!-- .element: class="fragment" data-fragment-index="3" -->
* Qual analisador vocês vão usar? Com quais configurações? <!-- .element: class="fragment" data-fragment-index="4" -->
* E então recolha feedback da sua equipe quanto ao uso, modifique seus padrões
se necessário<!-- .element: class="fragment" data-fragment-index="5" -->


* Como de fato _usar_ um analisador estático no desenvolvimento?
* Ferramentas instaladas que não são usadas não servem pra nada!
* Minha sugestão: _hooks pre-commit_ e _CI_
Note:
* Uma questão que fica é como usar de fato essas coisas
* Se você abrir o meu computador e o de muito dev por aí, você provavelmente vai
encontrar um monte de ferramenta X que a gente instalou achando que ia ser
a solução dos nossos problemas e que nunca usamos de fato
* No caso de analisadores estáticos em geral, eu gosto de uma abordagem em duas
camadas, hooks pre-commit e scripts no servidor de CI


### Hooks Pre-Commit
* Códigos que o `git` pode invocar _antes_ de arquivos sofrerem commit
* Recomendo o uso do [pre-commit](https://pre-commit.com/) para gerenciar hooks
* Executam na máquina do desenvolvedor
* Evita que código não-conformante vá para o repositório

Note:
* Eu gosto muito da ideia de hooks pre-commit porque eles são executados antes do
código ser submetido e, caso eles falham, o código não passa
* Isso mantém o repositório limpo pois é preventivo. Você não precisa fazer
um outro commit que vai corrigir alguma coisa que uma ferramenta pegou dps
* O problema de hooks pre-commit normais é que eles não são registrados como
arquivos no git, então é difícil mantê-los de forma igual por toda uma equipe
* Eu gosto bastante do projeto pre-commit porque ele te apresenta uma forma
estruturada de colocar seus hooks dentro do projeto
* Você pode colocar uma execução do seu analisado estático favorito aqui e todo
mundo que mexer no projeto vai ter acesso as configurações


### Servidor de CI
* CI é a prática de manter toda uma base de código íntegra<!-- .element: class="fragment" data-fragment-index="2" -->
* Em geral existe um servidor em algum roda tarefas em cima do código novo como testes e
verificações<!-- .element: class="fragment" data-fragment-index="3" -->
* Eu gosto de colocar todos os analisadores estáticos ali também<!-- .element: class="fragment"data-fragment-index="4" -->
* Evita que um dev que não configurou pre-commit ou não está acostumado com a
equipe viole o estilo que foi combinado<!-- .element: class="fragment" data-fragment-index="5" -->


* Erros no servidor de CI são uma ótima forma de disseminar boas práticas!<!-- .element: class="fragment" data-fragment-index="2" -->
* Ao invés de simplesmente colocar um erro cru, coloque alguma referência sobre
a documentação de boas práticas ou até mesmo o contato de alguém mais sênior
que pode ajudar com o problema <!-- .element: class="fragment" data-fragment-index="3" -->
Note:
* Isso é uma coisa que eu gosto bastante mas não vejo muita gente usando
* Erros no servidor de CI podem ser usados para disseminar as boas práticas
da equipe
* Se as mesmas ferramentas são executadas no pre-commit e no CI e o código de
alguém quebrou por conta de alguma coisa no pre-commit, isso indica que a pessoa
não configurou direito o próprio ambiente
* O erro do CI é uma ótima oportunidade de colocar um texto claro sobre o que aconteceu,
sobre as boas práticas e até mesmo colocar o contato de alguém mais sênior que se
disponibilize a ajudar os colegas nessa situação



# Informação, Segurança & Produtividade
Note:
* Nessa parte da minha palestra eu vou tocar por cima de alguns pontos que eu
acho relevantes nessa discussão


* Desenvolver Software é uma tarefa humana
* Software é feito por humanos, muitas vezes para humanos
* Muitos problemas em Engenharia de Software são problemas de comunicação

Note:
* Uma coisa que muitas vezes passa despercebida é como programação e produção
de software é uma tarefa criativa, lotada de fatores humanos

* Por algum tempo - e algumas pessoas até hoje pensam assim - pensava-se que o
software era uma coisa absolutamente objetiva, livre das "impurezas" dos humanos
envolvidos no seu desenvolvimento

* Isso não poderia estar mais longe da verdade. O desenvolvimento de software é
uma tarefa bastante criativa e que sofre bastante influência dos fatores humanos
no processo

* Muitas vezes, equipes de software enroscam e não conseguem atingir sua eficiência
máxima não por conta de razões técnicas, por que algum treinamento ou conhecimento
está faltando ou coisa assim

* Muitas vezes as equipes acabam sofrendo muito com problemas que são relacionados
com a interação entre as pessoas. Com atritos, com problemas de comunicação,
com ego, com problemas em ouvir opiniões diferentes e etc


* Ferramentas estáveis, que tiram do programador pesos desnecessários são bem vindas  <!-- .element: class="fragment" data-fragment-index="2" -->

* Cada minuto economizado deixando de caçar por erros "bobos" pode ser usado para
fazer outra coisa, trabalhar em outra tarefa, descansar, etc <!-- .element: class="fragment" data-fragment-index="3" -->


* Nenhuma ferramenta é perfeita
* Mas quando adotamos práticas e técnicas que nos ajudam a lidar melhor com o
próprio trabalho, todo mundo ganha


* Existe uma série de problemas de segurança que foram causados por erros tecnicamente
pequenos

* Mas que vieram a existir por conta de programadores cansados, sobrecarregados,
etc

* [Heartbleed](http://www.pl-enthusiast.net/2014/07/01/how-did-heartbleed-remain-undiscovered-and-what-should-we-do-about-it/) [foi um ótimo](https://www.schneier.com/blog/archives/2014/04/heartbleed.html) [exemplo](https://www.zdnet.com/article/heartbleed-open-sources-worst-hour/)


* Type Hinting pode nos ajudar com isso <!-- .element: class="fragment" data-fragment-index="2" -->
* Quanto maior a base de código, mais essa técnica pode se tornar útil <!-- .element: class="fragment" data-fragment-index="3" -->
* Nem ela – e nem nada – vai capturar e evitar todos os bugs <!-- .element: class="fragment" data-fragment-index="4" -->
* Mas dando mais informações de uma forma elegante e organizada, podemos capturar
mais bugs e nos ajudar a cometer menos erros <!-- .element: class="fragment" data-fragment-index="5" -->



# Lembre-se dos humanos
"Mind the human" <!-- .element: class="small -->


* Programar em Python é divertido
* O que fez Python ser o que é somos nós, as pessoas


![programming-is-fun-again](xkcd353.png)


> Programming is fun again!

― [xkcd 353](https://xkcd.com/353/)


* Na hora de escolher entre técnicas e ferramentas <!-- .element: class="fragment" data-fragment-index="2" -->
* Na hora de revisar o código de um colega <!-- .element: class="fragment" data-fragment-index="3" -->
* Na hora de contratar alguém novo <!-- .element: class="fragment" data-fragment-index="4" -->


# Lembre-se dos humanos!


* Type Hinting ― ou qualquer outra técnica ― ajudam quando elas ajudam os seres humanos por trás do código


![us](us.jpeg)

Note:
* O legal de uma python brasil é isso - a união da comunidade
* Ontem, por exemplo, eu tive o prazer de me juntar a essas pessoas
fantásticas para jantar e conversar
* E entre tudo o que a gente falou, uma coisa todos nós concordamos que Python é o que é e chegou onde chegou por conta da preocupação com as pessoas
* Isso é uma coisa que todos nós devemos nos lembrar e praticar no
nosso dia-a-dia, na nossa comunidade local, nas nossas empresas, etc
* E eu quero agradecer muito a Carol Willing, Melissa Weber, João
Bueno, Lorena Mesa e Luciano Ramalho por terem também me lembrado
disso
* E eu quero agradecer a todos vocês por estarem aqui e me ouvido nesse tempo. Somos nós quem formamos essa comunidade incrível e somos nós que tornamos tudo isso possível



# Muito obrigado!

* felipe@felipevr.com
* [github.com/fbidu](https://github.com/fbidu)
* Twitter @fevir0