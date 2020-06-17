# Python, Tipos & Segurança
Como _type hinting_ e análise estática podem ajudar você e sua equipe <!-- .element: class="small" -->

Note:
Bom dia a todos <etc>

Hoje nós vamos discutir um pouco sobre tipos de dados, análise estática de código
e as funcionalidades que temos para lidar com esses conceitos em Python



### Oi, eu sou o (Felipe) Bidu!

* [github.com/fbidu](https://github.com/fbidu)
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

― Guido van Rossum, Ivan Levkivskyi - [PEP 483](https://www.python.org/dev/peps/pep-0483/#background)

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



# Ferramentas sozinhas não fazem nada!
Precisamos de **métodos** <!-- .element: class="small -->
